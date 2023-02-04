import ssl
import time
from typing import List

import aiohttp
import certifi
import django.core.handlers.wsgi
import requests
from django.core import serializers
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

from exp1.models import Company

flow_count: int = 3


def sync_view(request: django.core.handlers.wsgi.WSGIRequest):
    "synchronous view"
    start: float = time.time()
    brewery_list: List = []
    url: str = "https://api.openbrewerydb.org/breweries/random"
    for _ in range(flow_count):
        response: requests.models.Response = requests.get(
            url=url , timeout=30
        )
        brewery_list.append(response.json()[0]['id'])
    count: int = len(brewery_list)
    execution_time: float = time.time() - start
    return render(
        request=request ,
        context={
            'data': brewery_list ,
            'count': count ,
            'time': execution_time
        } ,
        content_type='text/html' ,
        template_name='templates/exp1.html'
    )


async def async_view(request: django.core.handlers.wsgi.WSGIRequest):
    "asyncronous view"
    start: float = time.time()
    brewery_list: List = []

    url: str = "https://api.openbrewerydb.org/breweries/random"
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)
    async with aiohttp.ClientSession(
            connector=conn
    ):
        # for _ in range(flow_count):
        # async with session
        pass

    end: float = time.time() - start


def async_view_actions(request: django.core.handlers.wsgi.WSGIRequest):
    pass


def export(request: django.core.handlers.wsgi.WSGIRequest) -> HttpResponse:
    ids: List[str] = request.GET.get('ids').split(',')
    qs: QuerySet = Company.objects.filter(id__in=ids)
    response: HttpResponse = HttpResponse(
        content_type='application/json' ,
        status=200 ,
        charset='utf-8'
    )
    serializers.serialize(format='json' , queryset=qs , stream=response)
    return response
