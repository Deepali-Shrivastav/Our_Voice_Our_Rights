from django.http import JsonResponse, HttpResponse, FileResponse
from django.conf import settings
import json
import os

CACHE_FILE = os.path.join(settings.BASE_DIR, 'cache.json')


def load_cache():
    try:
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"districts": [], "data": {}}


def index(request):
    static_path = os.path.join(settings.BASE_DIR, 'static', 'index.html')
    try:
        with open(static_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='text/html; charset=utf-8')
    except Exception as e:
        error_msg = f"Page could not be loaded: {str(e)}"
        return HttpResponse(error_msg.encode('utf-8'), status=500, content_type='text/plain; charset=utf-8')


def api_cache(request):
    cache = load_cache()
    return JsonResponse(cache, safe=False)


def favicon(request):
    favicon_path = os.path.join(settings.BASE_DIR, 'static', 'favicon.ico')
    try:
        return FileResponse(open(favicon_path, 'rb'), content_type='image/svg+xml')
    except Exception:
        return HttpResponse(status=204)
