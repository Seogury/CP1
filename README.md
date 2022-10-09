# CP1
## 프로젝트 문제   
카테고리 별 제주도 여행지 추천 구현
### 가설
여행지 추천을 통해 사용자는 좀 더 다양하고 새로운 테마 여행 명소를 쉽게 찾을 수 있다. 즉 사용자의 편의성을 증대시킴으로써 기업의 매출 상승을 기대할 수 있다.

## 데이터셋 설명
  ![image](https://user-images.githubusercontent.com/97610185/193881431-1e27acab-f03b-4d6e-97ca-42a8cd801682.png)  
  colunms = name,	rating,	title, review (4)  
  row = 11494  
  data = (11494,4)   
  출처 : https://www.tripadvisor.co.kr/


## 해결과정
1. 데이터셋 구현을 위해 tripadviser 리뷰 크롤링
2. 데이터셋 전처리
3. okt 활용 형태소 분석
4. word2vec 사용 vector화
5. 테마 별 코사인 유사도 0.8 이하 단어 0 처리
  ![image](https://user-images.githubusercontent.com/97610185/193880094-6d8ad527-5061-443f-9b9d-03e06ae427b1.png)
6. counter vecterizer를 활용 DTM 생성
7. (테마 * 단어) @ DTM 
8. 감성분석리스트 활용 감성분석 실시
  ![image](https://user-images.githubusercontent.com/97610185/193880414-5ceb0494-26ec-421e-a910-4ca92eab136b.png)
9. 종합  
  ![image](https://user-images.githubusercontent.com/97610185/193993957-e48827d6-3662-4bbe-ba9c-13a4b9eeb25d.png)


## 결과
- 명소 score = (1.2 * 연관도 * 감성점수) + (0.1 * 평점) + (0.0005 * 리뷰 수)  
- '독특한' 테마를 선택 시 나오는 top5 명소
  ![image](https://user-images.githubusercontent.com/97610185/193880626-f77b5392-17c4-4be1-86bb-548aeb35ddf2.png)    


## 프로젝트 진행과정
  **역할:** 추천 모델링, 감성분석, 크롤링, 전처리, 웹구현 (기본) 
  
  **6/24(금):** 7팀 첫 미팅 관심 분야 및 주제 선정 조사, 간단한 일상 소통

  **6/25(토)~6/27(월):** 프로젝트 주제 선정 및 방향성, 데이터 선정, 직무 공유

  **6/28(화)~6/30(목):** 데이터 확보를 위해 크롤링, 수정 & 아이디어 제시 &  모델링 공부

  **7/1(금):** 크롤링 데이터 전처리, 시각화 및 모델링 공부,테스트, 발생되는 이슈 수정

  **7/2(토)~7/3(일):** 두 가지 모델링 테스트 후 한 가지 모델 선정

  **7/4(월) :** 중간 점검 피드백, 모델링 점검, 서비스 구현 테스트 및 점검

  **7/5(화) ~ 7/6(수) :** 발표 자료 준비 및 영상 녹화 제출

  **7/7(목) :** 프로젝트 피드백
  

## 한계점 및 해결방안
### 한계점
  1. 웹구현까지의 파이프라인이 제대로 구현되지 않았다.
  2. 점수 체계의 구체화
### 해결방안
  ![image](https://user-images.githubusercontent.com/97610185/193965314-5a42b333-fe50-4bc5-a44b-a9c5a4f28962.png)  
  - 현재는 이런 방식으로 진행하기 때문에 한 번 밖에 사용하지 못하는 파이프라인이다. 지속적으로 사용 가능하게 하기 위해서는  
  크롤링 > db적재 > 전처리 > NLP > db적재 > flask 이렇게 되어야한다.
