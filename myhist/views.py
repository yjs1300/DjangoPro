from django.shortcuts import render, redirect
import pandas as pd
import io
from datetime import datetime
from myhist.models import MemberHist
from django.http.response import HttpResponse
import json
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

# 회원의 분석결과 저장 기록 확인 페이지
def myhistFunc(request):
    return render(request, "memhist.html")

def histSaveFunc(request):
    dataframe_str = request.POST.get('dataframe')

    # 문자열을 데이터프레임으로 변환
    df = pd.read_csv(io.StringIO(dataframe_str), delim_whitespace=True)

    print(df)

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # 데이터프레임의 각 행을 Django 모델로 변환하여 저장
    for _, row in df.iterrows():
        model_obj = MemberHist(fk_m_id=request.session['user'], addr=row['장소명'], bike_load=row['자전거도로'], \
                               transport=row['지하철역'], park=row['공원'], tour=row['관광지'], \
                                school=row['대학'], pred=row['예측값'], reg_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        model_obj.save()

    return redirect("/myhist")

def histFunc(request):

    data = MemberHist.objects.filter(fk_m=request.session['user']).order_by('-reg_date')
    paginator = Paginator(data, 3)
    page = request.GET.get("page")
    
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)

    data_res = []
    for s in datas:
        dic = {'id':s.id,'addr':s.addr, 'bike':s.bike_load, 'transport':s.transport, 'park':s.park, \
               'tour':s.tour, 'school':s.school, 'pred':s.pred, 'date':s.reg_date.strftime("%Y-%m-%d %H:%M:%S")}
        data_res.append(dic)
    # print(data_result)

    
    # 페이징 처리

    # 현재 페이지
    now_page = datas.number
    tot_page = datas.paginator.num_pages

    if datas.has_previous():
        # 이전 페이지 존재할 경우
        pre_page = datas.previous_page_number()
    else:
        # 없을 경우
        pre_page = "f"
    
    if datas.has_next():
        # 다음 페이지 존재할 경우
        next_page = datas.next_page_number()
    else:
        # 없을 경우
        next_page = "f"
    
    page_res = []
    pages = {'now':now_page, 'tot':tot_page, 'pre':pre_page, 'next':next_page}
    page_res.append(pages)

    data_result = {'res':data_res, 'pages':page_res}
        

    return HttpResponse(json.dumps(data_result), content_type="application/json")

#  * @author jujuclubw
#  * @email dlrkdwn428@gmail.com
#  * @create date 2023-06-21 12:21:06
#  * @modify date 2023-06-21 12:21:06
#  * @desc [add chart]
def chartFunc(request):
    print(request.GET['id'])
    data = MemberHist.objects.get(id=request.GET['id'])
    dic = {'cycle':data.bike_load, 'train':data.transport, 'park':data.park, \
               'tour':data.tour,'school':data.school,}
    return HttpResponse(json.dumps(dic), content_type="application/json")