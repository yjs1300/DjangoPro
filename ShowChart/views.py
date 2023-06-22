from django.shortcuts import render
import folium
import pandas as pd
import json
from django.http import JsonResponse
from folium.plugins import MarkerCluster
import numpy as np
import matplotlib.pyplot as plt


# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,"register.html")
def err(request):
    return render(request,"404.html")
def card(request):
    return render(request,"cards.html")
def forgotpw(request):
    return render(request,"forgot-password.html")

def charts(request):
    
    df = pd.read_excel("./rental3.xlsx")
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
    
    with open('./hangjeongdong_.json',mode='rt',encoding='utf-8') as f:
        geo = json.loads(f.read())    
    
    for feature in geo['features']:
        code = feature['properties']['code']
        name = feature['properties']['name']
        # print(code) 
        # print(name)
        f.close()

    folium.Choropleth(
        geo_data= geo,
        name='choropleth',
        data=df, 
        columns=['지역번호','대여소갯수'], # 데이터프레임의 컬럼들
        key_on='feature.properties.code', # geojson 피처의 키
        fill_color='Reds',
        fill_opacity=0.7,
        line_opacity=0.7,
        color = 'black',
        overlay="True",
        legend_name='대여소 분포',
    ).add_to(m)
    
    maps1 = m._repr_html_()
    
        # 서울시 지자체별 파일
    state_geo = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
    
    # 서울시 유동인구 파일(행정구역별,나이대별,총이동)
    df = pd.read_csv('./seoul_float_pop_age.csv',encoding='utf-8')
    p=df[['행정구역별','총이동']]

    # 지도 생성함    
    elec_district_geo_map = folium.Map(location=[latitude, longitude], tiles="OpenStreetMap", zoom_start=10)
    
    # 시각화 
    folium.Choropleth(
        geo_data=state_geo,
        name='자치구 별 유동인구',
        data=p,
        columns=('행정구역별','총이동'),
        key_on='feature.properties.name',
        fill_color='Reds',
        fill_opacity = 0.7,
        line_opacity = 0.7,
        color = 'black',
        legend_name = '유동인구 수'
    ).add_to(elec_district_geo_map)

    maps2 = elec_district_geo_map._repr_html_()

#--------------------------------------------------------------------

    df = pd.read_csv('./rental.csv',encoding='cp949')
    df1 = df[(df['위도'] != 0) & (df['경도'] != 0)]
    df = df1.reset_index(drop=True)
    sub = df[['위도','경도']]
    # print(sub)
    
    # # 서울시 위도
    # latitude = 37.541
    # # 서울시 경도
    # longitude = 126.986
    
    # 지도 생성
    m = folium.Map(
        location=[latitude, longitude],
        zoom_start=10,
    
    )
    
    coords = sub
    # marker cluster 객체를 생성
    marker_cluster = MarkerCluster().add_to(m)
   
    
    # 데이터의 위도, 경도를 받아서 마커를 생성함.
    for lat, long in zip(coords['위도'], coords['경도']):
        folium.Marker([lat, long], icon = folium.Icon(color="green")).add_to(marker_cluster)
    
    # 템플릿에 보내기 위해서 사용함.
    maps3 = m._repr_html_()
    
    
    # 제주도 자전거 데이터
    
    df = pd.read_csv('./rentaljeju.csv', encoding='cp949')
    sub2 = df[['위도','경도']]
    # print(sub2)
    
    # 제주도 위도
    latitude1 = 33.499
    # 제주시 경도
    longitude1 = 126.531
    
    # 지도 생성
    m2 = folium.Map(
        location=[latitude1, longitude1],
        zoom_start=10,
    )
    
    coords = sub2
    # marker cluster 객채를 생성
    marker_cluster = MarkerCluster().add_to(m2)
    
    # 데이터의 위도, 경도를 받아서 마커를 생성함.
    for lat, long in zip(coords['위도'], coords['경도']):
        folium.Marker([lat, long], icon = folium.Icon(color="green")).add_to(marker_cluster)
    
    # 템플릿에 보내기 위해서 사용함.
    maps4 = m2._repr_html_()
    

    return render(request,"charts.html",{"maps1":maps1,"maps2":maps2,"maps3":maps3,"maps4":maps4})

