from django.shortcuts import render
<<<<<<< HEAD
import pickle
import pandas as pd
import numpy as np

=======
from .models import JejuFacility
import pandas as pd
import numpy as np
>>>>>>> dev

from sklearn.preprocessing import StandardScaler
    # 지도 보여주기 
def showmap(request):
    return render(request, "map.html")

<<<<<<< HEAD

#=================================================================
    
def mapanal(request):
    data_merge = pd.read_csv('C://Users//yjs60//Documents//GitHub//team1_main//ShowMap//static//output//jeju_merged_location.csv', encoding='utf-8')

    knnModel=0
    with open(file='C://Users//yjs60//Documents//GitHub//team1_main//ShowMap//static//output///MLmodel//knn_model_6.h5', mode='rb') as f:
        knnModel=pickle.load(f)
        
    # 결과 데이터프레임 초기화
    #result_data = pd.DataFrame(columns=['장소명', '자전거도로', '정류장', '공원', '관광지','학교','총이동'])
    result_data = pd.DataFrame(columns=['자전거도로','지하철역','공원','관광지','대학','총이동'])
    result_data['총이동']=0
    
    # 거리 계산을 위한 데이터프레임 복사 및 컬럼 추가
    temp_result = data_merge.copy()
    temp_result['최단거리'] = 0.0
    temp_result['총이동'] = 0.0

    print(request.GET['juso1'],request.GET['lat1'],request.GET['lng1'])
    juso1=request.GET['juso1']
    lat1=float(request.GET['lat1'])
    lng1=float(request.GET['lng1'])
    
    temp_result['장소명'] = juso1

    # 유클리드 거리 계산
    temp_result['최단거리'] = np.sqrt(
        np.power(temp_result['경도'] - lat1, 2) +
        np.power(temp_result['위도'] - lng1, 2)
    )
    
    # 주제별 최단거리를 구하기 위해 그룹화하여 최소값 선택
    temp_result = temp_result.groupby(['장소명', '주제'])['최단거리'].min().reset_index()
    temp_result = temp_result.pivot(index='장소명', columns='주제', values='최단거리').reset_index()

    # 결과 데이터프레임에 추가
    result_data = pd.concat([result_data, temp_result], ignore_index=True)

    # 결과 출력
    print(result_data)
    
    res_y=knnModel.predict(result_data)
    
    print(res_y)

    #knnModel.predict()
    return render(request, "map.html")
=======
#  * @author jujuclubw
#  * @email dlrkdwn428@gmail.com
#  * @create date 2023-06-14 14:01:59
#  * @modify date 2023-06-14 14:01:59
#  * @desc [description]
def uclid_process(data_merge,spot_data):
    # 결과 데이터프레임 초기화
    result_data = pd.DataFrame(columns=['장소명', '자전거도로', '지하철역', '공원', '관광지','대학'])
    spot_data['위도'] = spot_data['위도'].astype(float)
    spot_data['경도'] = spot_data['경도'].astype(float)
    for spot_index, spot_row in spot_data.iterrows():
        spot_name = spot_row['장소명']
        spot_longitude = spot_row['경도']
        spot_latitude =  spot_row['위도']

        # 거리 계산을 위한 데이터프레임 복사 및 컬럼 추가
        temp_result = data_merge.copy()
        temp_result['최단거리'] = 0.0
        temp_result['장소명'] = spot_name

        # 유클리드 거리 계산
        temp_result['최단거리'] = np.sqrt(
            np.power(temp_result['경도'] - spot_longitude, 2) +
            np.power(temp_result['위도'] - spot_latitude, 2)

        )

        # 주제별 최단거리를 구하기 위해 그룹화하여 최소값 선택
        temp_result = temp_result.groupby(['장소명', '주제'])['최단거리'].min().reset_index()
        temp_result = temp_result.pivot(index='장소명', columns='주제', values='최단거리').reset_index()

        # 결과 데이터프레임에 추가
        result_data = pd.concat([result_data, temp_result], ignore_index=True)
    return result_data

#  * @author jujuclubw
#  * @email dlrkdwn428@gmail.com
#  * @create date 2023-06-14 11:46:55
#  * @modify date 2023-06-14 11:46:55
#  * @desc [제주 시설 검색]
def jeju_analysis(request):
    
    jeju_facility = list(JejuFacility.objects.all())
    
    #최단 검색용 제주 시설 df
    f_datas = []
    for j in jeju_facility:
        dic = {
            '장소명':j.j_name,
            '위도':j.j_latitude,
            '경도':j.j_longitude,
            '주제':j.j_theme,
            }
        f_datas.append(dic)
        
    jeju_facility_df = pd.DataFrame(f_datas)
    # jeju_facility_df = jeju_facility_df[(jeju_facility_df['경도'] >= -180) & (jeju_facility_df['경도'] <= 180)]
    # print(jeju_facility_df)
    #선택한 제주 위경도
    ping = {
        '장소명':[request.POST['juso1'],request.POST['juso2'],request.POST['juso3']],
        '위도':[request.POST['lat1'],request.POST['lat2'],request.POST['lat3']],
        '경도':[request.POST['lng1'],request.POST['lng2'],request.POST['lng3']],
    }
    spot_data = pd.DataFrame(ping)
    spot_data.replace('', np.nan, inplace=True)
    spot_data.dropna(inplace=True)
    
    result_data = uclid_process(jeju_facility_df,spot_data)

    #모델예측
    # '장소명' 컬럼을 제외한 값 선택
    X = result_data.drop(columns=['장소명'])
    # 데이터 표준화
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # # pkl 파일 경로
    # pkl_file_path = "static/model/knn_model_5.h5"
    # import pickle
    # # pkl 파일 로드
    # with open(pkl_file_path, 'rb') as file:
    #     model = pickle.load(file)
    
    # 모델 로드
    import joblib
    model = joblib.load('static/model/MLP.pkl') 
    # 예측 수행
    y_pred = model.predict(X_scaled)
    df_pred = pd.DataFrame({'예측값': y_pred})
    # X 값과 예측된 y 값을 합치기
    df_result = pd.concat([result_data['장소명'],X, df_pred], axis=1)
    print(df_result)
    
    return render(request,"analysis.html",{'result':df_result.to_html()})
>>>>>>> dev
