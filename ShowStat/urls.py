    # /**
    #  * @author jujuclubw
    #  * @email dlrkdwn428@gmail.com
    #  * @create date 2023-06-13 11:12:01
    #  * @modify date 2023-06-13 11:12:01
    #  * @desc 통계 메인 url.py 생성
    #  */
from django.urls import path
from ShowStat import views

urlpatterns = [
    path("", views.showstat),
    # path("chart/", views.rentalcount), # 06.15 지도 시각화 진행 
    
    # 서울시 지역구별 유동인구 시각화
    # path("movepeople/",views.MovePeople),
]