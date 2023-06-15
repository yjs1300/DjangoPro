# /**
#  * @author jujuclubw
#  * @email dlrkdwn428@gmail.com
#  * @create date 2023-06-13 11:11:22
#  * @modify date 2023-06-13 11:11:22
#  * @desc ShowStat 통계페이지 앱 생성
#  */
from django.shortcuts import redirect, HttpResponse, HttpResponseRedirect, render
from django.http import JsonResponse
import json
import folium
from folium.plugins import MarkerCluster,FastMarkerCluster
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def showstat(request):
    return render(request,"statistic.html")

# 서울시 자전거 대여소 수 
def rentalcount(request):
    df = pd.read_csv('./rental3.csv',encoding="cp949")
    df['대여소_ID'] = range(0, 3225)
    # df.set_index("시군구")
    # index_list = []
    # for index in range(0, 3224):
    #     index_list.append(index)
    # return index_list
        
    
    # df['대여소_ID'] = df['대여소_ID'].replace(index_list)
    print(df.head())
    print(df.info())
    print(df.isnull())
    
    # 지도의 기준이 되는 위도 경도 
    # 서울의 위도 경도이다.
    latitude = 37.562225
    longitude = 126.978555
    
    # 지도 생성함
    m  = folium.Map(
        location= [latitude, longitude],
        zoom_start=10, # 줌
        tiles= "OpenStreetMap",
    )
    
    # geojsondata
   
    with open('./hangjeongdong_.json',mode='rt',encoding='utf-8') as f:
        geo = json.loads(f.read())    
    
    for feature in geo['features']:
        code = feature['properties']['code']
        name = feature['properties']['name']
        print(code) 
        print(name)
        f.close()
    
    # folium.GeoJson(
    #     geo,
    #     name='seoul_municipalities'
    #     ).add_to(m)
    
    
    folium.Choropleth(
        geo_data= geo,
        name='choropleth',
        data=df, 
        columns=['시군구코드','대여소_ID'], # 데이터프레임의 컬럼들
        key_on='feature.properties.code', # geojson 피처의 키
        fill_color='YlGn',
        fill_opacity=0.5,
        line_opacity=0.7,
        color = 'black',
        legend_name='대여소 분포',
    ).add_to(m)
    
    maps = m._repr_html_()
   
    return render(request,"Chorop.html", {"maps":maps})
    
    