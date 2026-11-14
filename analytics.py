"""当前资料入口；不实现统计分析目标。"""
import json
from common import read
from requests import requests
from dispatch import availability
from journeys import outcomes
def prepare_sources():
    data=read()
    return {'requests': requests(data), 'availability': availability(data), 'outcomes': outcomes(data)}
if __name__=="__main__":print(json.dumps(prepare_sources(),ensure_ascii=False,default=str,indent=2))