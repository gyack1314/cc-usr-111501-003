from common import unique,number
def requests(data):
    out=unique(data['requests'],'request_id')
    for r in out.values():
        if r['passenger_id'] not in data['passengers'] or r['at']<0:raise ValueError('请求身份或时刻非法')
        if r['retry_of'] is not None and r['retry_of'] not in out:raise ValueError('重试来源不存在')
    return out
