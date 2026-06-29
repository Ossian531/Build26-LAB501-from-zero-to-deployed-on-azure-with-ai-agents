import logging
import urllib.parse
import urllib.request
from flask import Flask, render_template, request, abort, Response, jsonify
from dotenv import load_dotenv

import data

load_dotenv()
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

ITEMS_PER_PAGE = 24


@app.route("/healthz")
def healthz():
    """Diagnostic endpoint: reports where the catalog is loaded from."""
    return jsonify(status="ok", data=data.source_info())


@app.route("/")
def home():
    # Featured sets — large popular sets
    featured = data.featured(limit=8)
    return render_template(
        "home.html",
        featured=featured,
        total_sets=data.total_sets(),
        total_themes=data.total_themes(),
    )


@app.route("/browse")
def browse():
    search = request.args.get("q", "").strip()
    theme = request.args.get("theme", "").strip()
    year = request.args.get("year", "").strip()
    sort = request.args.get("sort", "name")
    page = request.args.get("page", 1, type=int)
    if page < 1:
        page = 1

    sets, total_items, total_pages, page = data.browse(
        search=search,
        theme=theme,
        year=year,
        sort=sort,
        page=page,
        per_page=ITEMS_PER_PAGE,
    )

    # Get all themes for the filter dropdown
    themes = data.all_themes()

    return render_template(
        "browse.html",
        sets=sets,
        themes=themes,
        search=search,
        selected_theme=theme,
        selected_year=year,
        sort=sort,
        page=page,
        total_pages=total_pages,
        total_items=total_items,
    )


@app.route("/set/<set_id>")
def detail(set_id):
    lego_set = data.get_by_id(set_id)
    if not lego_set:
        abort(404)

    # Get related sets from the same theme
    related = data.related(lego_set["theme_name"], set_id, limit=6)
    return render_template("detail.html", set=lego_set, related=related)


@app.route("/image-proxy")
def image_proxy():
    """Proxy remote images (e.g. cdn.rebrickable.com) that are blocked from
    direct browser access in some lab/network environments."""
    url = request.args.get("url", "").strip()
    if not url or not url.startswith(("http://", "https://")):
        abort(400)
    # Only allow proxying from known image hosts to avoid an open proxy.
    allowed_hosts = ("cdn.rebrickable.com", "placehold.co")
    try:
        parsed = urllib.parse.urlparse(url)
    except Exception:
        abort(400)
    if parsed.hostname not in allowed_hosts:
        abort(403)

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "lego-vault-proxy/1.0"})
        with urllib.request.urlopen(req, timeout=10) as upstream:
            data = upstream.read()
            content_type = upstream.headers.get("Content-Type", "image/jpeg")
    except Exception:
        abort(502)

    return Response(data, content_type=content_type, headers={"Cache-Control": "public, max-age=86400"})


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
