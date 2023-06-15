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
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def showstat(request):
    df2 = pd.read_csv("월별이용건수.csv", encoding="UTF-8")
    chartdata2 = df2.to_json(orient='records',force_ascii=False)  
    chartdata2 = json.dumps(chartdata2) # 디코딩
    chartdata2 = json.loads(chartdata2) # 인코딩

    df3 = pd.read_csv("월별 신규가입자수.csv", encoding="UTF-8")
    chartdata3 = df3.to_json(orient='records',force_ascii=False)  
    chartdata3 = json.dumps(chartdata3) # 디코딩
    chartdata3 = json.loads(chartdata3) # 인코딩
    
    df4 = pd.read_csv("연도별 제주관광객수.csv", encoding="UTF-8")
    chartdata4 = df4.to_json(orient='records',force_ascii=False)  
    # chartdata = json.dumps(chartdata, ensure_ascii=False)
    chartdata4 = json.dumps(chartdata4) # 디코딩
    chartdata4 = json.loads(chartdata4) # 인코딩



    context= {'chartdata2':chartdata2,'chartdata3':chartdata3,'chartdata4':chartdata4}
    return render(request,"statistic.html", context)
