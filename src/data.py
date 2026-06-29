"""Data layer for the LEGO Set Browser.

The catalog lives as a single JSON object in an S3 bucket (the "database"):
spawned wires the bucket name into the Lambda via a `<NAME>_BUCKET` env var and
grants it read access. The object is fetched once per warm Lambda and cached in
memory; filtering/sorting/paging happen in Python.

To update the catalog, re-upload the JSON to the bucket — no redeploy needed:
    spawned upload <project> --component <bucket> --key lego_sets.json --file data/lego_sets.json

If no bucket is configured (e.g. local development), it falls back to the
bundled data/lego_sets.json so the app still runs.
"""

import json
import logging
import os

log = logging.getLogger("lego.data")

_LOCAL_PATH = os.path.join(os.path.dirname(__file__), "data", "lego_sets.json")
_OBJECT_KEY = os.environ.get("LEGO_DATA_KEY", "lego_sets.json")

_SETS = None


def _bucket_name():
    """Resolve the data bucket from env.

    Prefer an explicit LEGO_DATA_BUCKET, otherwise accept whatever `<NAME>_BUCKET`
    var spawned injected from the Function->Bucket connection.
    """
    explicit = os.environ.get("LEGO_DATA_BUCKET")
    if explicit:
        return explicit
    for key, value in os.environ.items():
        if key.endswith("_BUCKET") and value:
            return value
    return None


def _load_from_s3(bucket):
    import boto3  # imported lazily so local dev needs no AWS deps
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket, Key=_OBJECT_KEY)
    return json.loads(obj["Body"].read())


def _load_from_local():
    with open(_LOCAL_PATH, encoding="utf-8") as f:
        return json.load(f)


def _all():
    """Return the catalog, loading + caching it on first use.

    A successful S3 read is cached for the life of the warm Lambda. A fallback to
    the bundled file is NOT cached, so a later request retries S3 once the bucket
    has been seeded.
    """
    global _SETS
    if _SETS is not None:
        return _SETS

    bucket = _bucket_name()
    if bucket:
        try:
            data = _load_from_s3(bucket)
            log.info("Loaded %d sets from s3://%s/%s", len(data), bucket, _OBJECT_KEY)
            _SETS = data
            return _SETS
        except Exception as exc:  # noqa: BLE001 - degrade gracefully, retry next call
            log.warning("S3 load failed (%s); falling back to bundled data", exc)
            return _load_from_local()

    data = _load_from_local()
    _SETS = data
    return _SETS


def featured(limit=8):
    """Large popular sets — mirrors the original >2000-parts featured query."""
    big = [s for s in _all() if s["number_of_parts"] > 2000]
    big.sort(key=lambda s: s["number_of_parts"], reverse=True)
    return big[:limit]


def total_sets():
    return len(_all())


def total_themes():
    return len({s["theme_name"] for s in _all()})


def all_themes():
    return sorted({s["theme_name"] for s in _all()})


_SORTERS = {
    "name": (lambda s: s["name"].lower(), False),
    "year_desc": (lambda s: s["year_released"], True),
    "year_asc": (lambda s: s["year_released"], False),
    "parts_desc": (lambda s: s["number_of_parts"], True),
    "parts_asc": (lambda s: s["number_of_parts"], False),
}


def browse(search="", theme="", year="", sort="name", page=1, per_page=24):
    """Filtered, sorted, paginated browse. Returns (sets, total_items, total_pages, page)."""
    results = _all()

    if search:
        needle = search.lower()
        results = [s for s in results if needle in s["name"].lower()]
    if theme:
        results = [s for s in results if s["theme_name"] == theme]
    if year:
        results = [s for s in results if s["year_released"] == int(year)]

    key, reverse = _SORTERS.get(sort, _SORTERS["name"])
    results = sorted(results, key=key, reverse=reverse)

    total_items = len(results)
    total_pages = max(1, (total_items + per_page - 1) // per_page)
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages

    offset = (page - 1) * per_page
    page_items = results[offset:offset + per_page]
    return page_items, total_items, total_pages, page


def get_by_id(set_id):
    for s in _all():
        if s["id"] == set_id:
            return s
    return None


def related(theme_name, set_id, limit=6):
    rel = [
        s for s in _all()
        if s["theme_name"] == theme_name and s["id"] != set_id
    ]
    rel.sort(key=lambda s: s["number_of_parts"], reverse=True)
    return rel[:limit]
