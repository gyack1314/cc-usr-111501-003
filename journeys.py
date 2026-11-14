from common import unique,number
from requests import requests
def outcomes(data):
    req=requests(data);rows=unique(data['journeys'],'journey_id');by={}
    for r in rows.values():
        if r['request_id'] not in req or r['status'] not in ('completed','cancelled','observed'):raise ValueError('出行结果状态非法')
        if r['end'] is not None and r['end']<req[r['request_id']]['at']:raise ValueError('结局早于请求')
        by.setdefault(r['request_id'],[]).append(r)
    if set(by)-set(req):raise ValueError('请求关联非法')
    return {'rows':rows,'requests_with_journey':sorted(by),'end_states':{k:sum(r['status']==k for r in rows.values()) for k in ('completed','cancelled','observed')}}
