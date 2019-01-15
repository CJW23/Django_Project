from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from homework.settings import STATIC_ROOT
import os
import pandas as pd
import json

#메인 페이지 불러오는 함수
def index(request):


    index_info = get_info()
    index_career = get_career()
    index_copyright = get_Copyright()
    return render(request, 'portfolio/index.html',
                  {'info': index_info, 'career': index_career, 'copyright': index_copyright})

#나의 정보를 담은객체 반환 함수
def get_info():
    info = {'name': 'ChoiJaeWoo', 'studentID': 2014041005, 'department': 'SoftWare',
            'professor': 'Aziz Nasridinov'}
    return info

#career.csv 파일의 정보를 json으로 변환해 반환
def get_career():
    career = {}

    py = os.getcwd()
    py = py.replace("\\", "/")

    url = py + "/portfolio/static/portfolio/data/career.csv"
    print("123" + url)
    df = pd.read_csv(url, encoding='utf-8', engine='python')
    career = df.to_json(orient='split')
    career = json.loads(career)
    return career

#copyright.csv 파일의 저보를 json으로 변환해 반환
def get_Copyright():
    copyright = {}
    py = os.getcwd()
    py = py.replace("\\", "/")
    url = py + "/portfolio/static/portfolio/data/copyright.csv"
    df = pd.read_csv(url, encoding='utf-8', engine='python')
    copyright = df.to_json(orient='split')
    copyright = json.loads(copyright)
    return copyright
