import pandas as pd                 # 데이터 저장하고 가공처리
import matplotlib as mpl            # 그래프 그리기
import matplotlib.pyplot as plt     # 그래프 그리기


# csv 파일 읽어 dataFrame 객체 만들고 , 인덱스 컬럼 point 설정
df = pd.read_csv('weather.csv',index_col='point', encoding='euc-kr')
# print(df)
# df.loc(label-location)을 이용해 특정 인덱스의 데이터만 가져오도록 함
city_df = df.loc[['서울','인천','대전','대구','광주','부산','울산']]
print(city_df)

# 데이터의 폰트를 설정한다
# matplotlib에서는 기본적으로 한글 표시가 되지 않으므로 한글 폰트를 지정 설정한다
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 차트 종류 제목 크기 범례 폰트 크기 설정
ax = city_df.plot(kind='bar', title='날씨', figsize=(12,4), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)
ax.set_ylabel('기온/습도', fontsize=12)
ax.legend(['기온','습도'], fontsize=12)

plt.show()
