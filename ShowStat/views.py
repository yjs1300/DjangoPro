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
   
    with open('C:\\Users\\outlo\\Desktop\\biket1\\DjangoPro\\hangjeongdong_.json',mode='rt',encoding='utf-8') as f:
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
        fill_opacity=0.7,
        line_opacity=0.7,
        color = 'black',
        legend_name='대여소 분포',
    ).add_to(m)
    
    maps1 = m._repr_html_()
        # 서울시 지자체별 파일("code":"11250","name":"강동구","name_eng":"Gangdong-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":)
    state_geo = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
    # 서울시 유동인구 파일(행정구역별,나이대별,총이동)
    df = pd.read_csv('C:\\Users\\outlo\\Desktop\\biket1\\DjangoPro\\seoul_float_pop_age.csv',encoding='utf-8')
    p=df[['행정구역별','총이동']]
    # 서울시 위도
    # latitude = 37.541
    # 서울시 경도
    # longitude = 126.986

    # 지도 생성함    
    elec_district_geo_map = folium.Map(location=[latitude, longitude], tiles="OpenStreetMap", zoom_start=10)
    
    # 시각화 
    folium.Choropleth(
        geo_data=state_geo,
        name='자치구 별 유동인구',
        data=p,
        columns=('행정구역별','총이동'),
        key_on='feature.properties.name',
        fill_color='Greens',
        fill_opacity = 0.7,
        line_opacity = 0.7,
        color = 'black',
        legend_name = '유동인구 수'
    ).add_to(elec_district_geo_map)

    maps2 = elec_district_geo_map._repr_html_()
    return render(request,"Chorop.html",{"maps1":maps1,"maps2":maps2})

# 서울시 자전거 대여소 수 
# def rentalcount(request):
    # df = pd.read_csv('./rental3.csv',encoding="cp949")
    # df['대여소_ID'] = range(0, 3225)
    # # df.set_index("시군구")
    # # index_list = []
    # # for index in range(0, 3224):
    # #     index_list.append(index)
    # # return index_list
        
    
    # # df['대여소_ID'] = df['대여소_ID'].replace(index_list)
    # print(df.head())
    # print(df.info())
    # print(df.isnull())
    
    # # 지도의 기준이 되는 위도 경도 
    # # 서울의 위도 경도이다.
    # latitude = 37.562225
    # longitude = 126.978555
    
    # # 지도 생성함
    # m  = folium.Map(
    #     location= [latitude, longitude],
    #     zoom_start=10, # 줌
    #     tiles= "OpenStreetMap",
    # )
    
    # # geojsondata
   
    # with open('./hangjeongdong_.json',mode='rt',encoding='utf-8') as f:
    #     geo = json.loads(f.read())    
    
    # for feature in geo['features']:
    #     code = feature['properties']['code']
    #     name = feature['properties']['name']
    #     print(code) 
    #     print(name)
    #     f.close()
    
    # # folium.GeoJson(
    # #     geo,
    # #     name='seoul_municipalities'
    # #     ).add_to(m)
    
    
    # folium.Choropleth(
    #     geo_data= geo,
    #     name='choropleth',
    #     data=df, 
    #     columns=['시군구코드','대여소_ID'], # 데이터프레임의 컬럼들
    #     key_on='feature.properties.code', # geojson 피처의 키
    #     fill_color='YlGn',
    #     fill_opacity=0.5,
    #     line_opacity=0.7,
    #     color = 'black',
    #     legend_name='대여소 분포',
    # ).add_to(m)
    
    # maps = m._repr_html_()
   
    # return render(request,"statistic.html", {"maps1":maps1})

# 유동인구 데이터 시각화
# def MovePeople(request):
#     # 서울시 지자체별 파일("code":"11250","name":"강동구","name_eng":"Gangdong-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":)
#     state_geo = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
#     # 서울시 유동인구 파일(행정구역별,나이대별,총이동)
#     df = pd.read_csv('C:\\Users\\outlo\\Desktop\\biket1\\DjangoPro\\seoul_float_pop_age.csv',encoding='utf-8')
#     p=df[['행정구역별','총이동']]
#     # 서울시 위도
#     latitude = 37.541
#     # 서울시 경도
#     longitude = 126.986

#     # 지도 생성함    
#     elec_district_geo_map = folium.Map(location=[latitude, longitude], tiles="OpenStreetMap", zoom_start=11)
    
#     # 시각화 
#     folium.Choropleth(
#         geo_data=state_geo,
#         name='자치구 별 유동인구',
#         data=p,
#         columns=('행정구역별','총이동'),
#         key_on='feature.properties.name',
#         fill_color='Greens',
#         fill_opacity = 0.7,
#         line_opacity = 1,
#         color = 'black',
#         legend_name = '유동인구 수'
#     ).add_to(elec_district_geo_map)

#     # elec_district_geo_map.save('ShowStat/templates/seoul_map.html')  # 지도를 HTML 파일로 저장
#     maps2 = elec_district_geo_map._repr_html_()
#     return render(request, 'statistic.html',{'maps2':maps2})









