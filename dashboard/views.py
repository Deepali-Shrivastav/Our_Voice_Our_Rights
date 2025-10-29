from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.shortcuts import render
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
        with open(static_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return HttpResponse(content, content_type='text/html')
    except Exception as e:
        return HttpResponse(f"Page could not be loaded: {str(e)}", status=500)


def api_cache(request):
    cache = load_cache()
    return JsonResponse(cache, safe=False)
