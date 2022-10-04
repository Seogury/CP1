# CP1
## 프로젝트 문제   
카테고리 별 제주도 여행지 추천 구현
### 가설
여행지 추천을 통해 사용자는 좀 더 다양하고 새로운 테마 여행 명소를 쉽게 찾을 수 있다. 즉 사용자의 편의성을 증대시킴으로써 기업의 매출 상승을 기대할 수 있다.
  
## 해결과정
1. 데이터셋 구현을 위해 tripadviser리뷰 크롤링
2. 데이터셋 전처리
3. okt 활용 형태소 분석
4. word2vec 사용 vector화
5. 테마 별 코사인 유사도 0.8 이하 단어 0 처리
6. counter vecterizer를 활용 DTM 생성
7. (테마 * 단어) @ DTM 
8. 감성분석리스트 활용 감성분석 실시
9. 명소 별 score = (1.2 * 연관도 * 감성점수) + (0.1 * 평점) + (0.0005 * 리뷰 수)

## 프로젝트 진행과정
  **6/24(금):** 7팀 첫 미팅 관심 분야 및 주제 선정 조사, 간단한 일상 소통

  **6/25(토)~6/27(월):** 프로젝트 주제 선정 및 방향성, 데이터 선정, 직무 공유

  **6/28(화)~6/30(목):** 데이터 확보를 위해 크롤링, 수정 & 아이디어 제시 &  모델링 공부

  **7/1(금):** 크롤링 데이터 전처리, 시각화 및 모델링 공부,테스트, 발생되는 이슈 수정

  **7/2(토)~7/3(일):** 두 가지 모델링 테스트 후 한 가지 모델 선정

  **7/4(월) :** 중간 점검 피드백, 모델링 점검, 서비스 구현 테스트 및 점검

  **7/5(화) ~ 7/6(수) :** 발표 자료 준비 및 영상 녹화 제출

  **7/7(목) :** 프로젝트 피드백
  
##  
