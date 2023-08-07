import json
import time
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


@api_view(['GET'])
def get_sites(request, *args, **kwargs):
    if request.method == 'GET':
        if request.GET.get("from") and request.GET.get("to"):
            from_d = request.GET.get("from")
            to_d = request.GET.get("to")
        else:
            from_d = 0
            to_d = 99999999999
        keys = redis_instance.keys("*")
        res_set = set()
        for key in keys:
            if int(from_d) <= float(key.decode('utf-8')) <= int(to_d):
                now_val = redis_instance.get(key).decode('utf-8')
                now_str = ''
                for i in now_val:

                    if i == '\n':
                        res_set.add(now_str)
                        now_str = ''
                        continue
                    now_str += i
        response = {"domain": [*res_set], "status": status.HTTP_200_OK}
        return Response(response, status=200)


@api_view(['POST'])
def append_sites(request, *args, **kwargs):
    if request.method == 'POST':
        res_str = str()
        item = json.loads(request.body)
        res_key = time.time()
        res_values = set()
        for key in list(item.keys()):
            value = item[key]
            if type(value) == list:
                for i in value:
                    value = i.split("www.")[-1].split("//")[-1].split('?')[0].split("/")[0]
                    res_values.add(value)
            else:
                value = value.split("www.")[-1].split("//")[-1]
                res_values.add(value)
        for i in res_values:
            res_str += i + '\n'

        redis_instance.set(res_key, res_str)
        return Response({"status": status.HTTP_201_CREATED})
