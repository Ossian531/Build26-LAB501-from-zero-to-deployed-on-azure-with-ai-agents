"""Local data layer backed by a bundled JSON dataset.

This replaces the original Azure Cosmos DB access layer so the app can run
standalone (e.g. as an AWS Lambda) with no external database. The functions
here implement the same queries the routes need: featured sets, totals,
browse with search/filter/sort/paging, lookup by id, and related sets.
"""

import json
import os

_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "lego_sets.json")

_SETS = None


def _all():
    """Load and cache the dataset."""
    global _SETS
    if _SETS is None:
        with open(_DATA_PATH, encoding="utf-8") as f:
            _SETS = json.load(f)
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
