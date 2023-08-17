# 🚥 Beaconomic
## 서울시 치안 종합지도와 112 신고건수 예측을 통한 범죄수요 예측

![image](https://github.com/theci/multicampus-semi-project/assets/110512212/42573c59-2d2f-49da-961d-d35b51c78a4d)


## :bulb: 서비스 및 프로젝트 소개
### 치안 안전 지도 <br>
![image](https://github.com/theci/multicampus-semi-project/assets/110512212/33765d0d-3eef-41a9-ab32-cfb4de373d73)
[공공데이터포털](https://www.data.go.kr/) 사이트에서 서울시 행정구별 치안 데이터를 수집하고 전처리하여 시각화했습니다. <br>
치안 안전 지수를 산출하는 계산식을 파이썬 함수로 만들고 전처리한 변수들의 상관관계를 계산해 변수로 사용해 종합 치안 지수를 산출하였습니다.


### 112 신고 건수를 통해 범죄수요 예측 <br>
![image](https://github.com/theci/multicampus-semi-project/assets/110512212/60ad9221-67b7-4c02-86b5-2850aa722301)
회귀 분석 모델을 이용해 112 신고 건수의 증감을 예측하는 모델링했습니다. <br>
그렇게 예측한 값으로 각 행정구별 범죄 수요를 예측했습니다.


## :wrench: 사용 기술 스택
- Python 1.8
- scikitLearn
- MySQL 8.0
- Django
- Pandas
- folium


