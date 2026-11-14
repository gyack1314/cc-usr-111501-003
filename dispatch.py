from common import unique,number
from requests import requests
def availability(data):
    req=requests(data);slots=unique(data['dispatch'],'dispatch_id')
    for r in slots.values():
        if r['request_id'] not in req or r['available']<0 or r['at']<req[r['request_id']]['at']:raise ValueError('派车状态与请求时序冲突')
    return {'rows':slots,'capacity_minutes':sum(r['available'] for r in slots.values()),'unserved':sum(r['assigned_vehicle'] is None for r in slots.values())}
