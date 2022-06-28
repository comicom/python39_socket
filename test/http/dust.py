# ref. https://www.data.go.kr/data/15073885/openapi.do

import time
import datetime

import urllib
from urllib import parse
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus

from bs4 import BeautifulSoup

class searchDust:
  def __init__(self,url:str, key:str):
    self.url = url
    self.key = key
    # self.today = 
    # self.tag = {
    #             # "저번주": -7,
    #             "어제": -1,
    #             "오늘": 0,
    #             "내일": 1,
    #             #  "다음주": 7,
    #             }
    self.result = []
  
  def Setup(self,location:str, date:str) -> None:
    self.location = location
    # if date in self.tag:
    #   self.date = self.tag[date]
    #   print("Set {}".format(date))
    # else:
    #   self.date = self.tag["오늘"]
    #   print("Set 오늘")
    year, month, day = date.split("-")
    self.date = date
    
    # today = datetime.datetime.today()
    # self.today = datetime.datetime(today.year, today.month, today.day + self.date)
    self.today = datetime.datetime(year, month, day)
  
  def Search(self) -> list:
    queryParams = '?' + urlencode({quote_plus('servicekey'): key,
                                  quote_plus('returnType'): 'XML',
                                  quote_plus('numOfRows'): '10',
                                  quote_plus('pageNo'): '1', 
                                  quote_plus('year'): self.today.year,
                                  #  quote_plus('itemCode'): 'PM10',
                                  })
    request = urllib.request.Request(url+unquote(queryParams))
    # print('Request:\n'+url+queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()

    soup = BeautifulSoup(response_body, "html.parser")
    tags = soup.find_all('item')
    
    result = []
    flag = 0
    for i in tags:
        # print('지역명 : {}'.format(i.select('districtname')[0].text))
        # print('발령일 : {}'.format(i.select('datadate')[0].text))
        # print('발령농도 : {} ug/m3'.format(i.select('issueval')[0].text))
        # print('발령시간 : {}'.format(i.select('issuetime')[0].text))
        # print('해제일 : {}'.format(i.select('cleardate')[0].text))
        # print('해제시간 : {}'.format(i.select('cleartime')[0].text))
        # print('경보단계 : {}'.format(i.select('issuegbn')[0].text))
        if i.select('districtname')[0].text == self.location and i.select('datadate')[0].text == self.date:
          flag=1
          dummy = {"location":i.select('districtname')[0].text,
                   "datadate":i.select('datadate')[0].text,
                   "issuegbn":i.select('issuegbn')[0].text}
          result.append(dummy)
        elif flag==0:
          pass
        else:
          return result
      # return result

  def Run(self,location:str, date:str) -> dict:
    self.Setup(location, date)
    self.result = self.Search()
    return self.result
