# /**
#  * @author jujuclubw
#  * @email dlrkdwn428@gmail.com
#  * @create date 2023-06-13 11:11:22
#  * @modify date 2023-06-13 11:11:22
#  * @desc ShowStat 통계페이지 앱 생성
#  */
from django.shortcuts import render
import folium
import pandas as pd
# import os


def showstat(request):
    return render(request, 'statistic.html')


# 유동인구 데이터 시각화
def MovePeople(request):
    # 서울시 지자체별 파일("code":"11250","name":"강동구","name_eng":"Gangdong-gu","base_year":"2013"},"geometry":{"type":"Polygon","coordinates":)
    state_geo = 'https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json'
    # 서울시 유동인구 파일(행정구역별,나이대별,총이동)
    df = pd.read_csv('C:\\Users\\outlo\\Desktop\\biket1\\DjangoPro\\seoul_float_pop_age.csv',encoding='utf-8')
    p=df[['행정구역별','총이동']]
    # 서울시 위도
    latitude = 37.541
    # 서울시 경도
    longitude = 126.986
    
    elec_district_geo_map = folium.Map(location=[latitude, longitude], tiles="OpenStreetMap", zoom_start=11)
    m=folium.Choropleth(
        geo_data=state_geo,
        name='자치구 별 유동인구',
        data=p,
        columns=('행정구역별','총이동'),
        key_on='feature.properties.name',
        fill_color='Greens',
        fill_opacity = 0.7,
        line_opacity = 1,
        color = 'black',
        legend_name = '유동인구 수'
    ).add_to(elec_district_geo_map)

    elec_district_geo_map.save('ShowStat/templates/seoul_map.html')  # 지도를 HTML 파일로 저장

    return render(request, 'seoul_map.html',{'m':map})
    # return render(request, 'statistic.html',{'map':map})









