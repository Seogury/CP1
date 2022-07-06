import sys
import os
import pandas as pd
import numpy as numpy

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

#open url.csv
url_df = pd.read_csv('220628_jeju_url.csv')
#create url_list
url_list = url_df['url_id']

#리스트 생성
review_list = []
rating_list = []
name_list = []
title_list = []

#브라우저 생성
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

driver = webdriver.Chrome(chrome_options=chrome_options)


for url in url_list[100:120]:
    
    #페이지 열기
    driver.get(url)
    driver.implicitly_wait(10)

    #전체 페이지
    try:
        num = driver.find_element(By.CLASS_NAME,'Ci')
    except:
        pass
    
    try:
        page = int(int(num.text.split(' ')[3])/10)
    except:
        page = 1

    for i in range(0, page):
        #명소 이름
        name = driver.find_element(By.CSS_SELECTOR,'.fiohW')
        name = name.text

        #명소 평점
        ratingss = driver.find_elements(By.CLASS_NAME, 'LbPSX')
        for rat in ratingss:
            ratings = rat.find_elements(By.CLASS_NAME, 'UctUV')
            for rating in ratings:
                score = rating.get_attribute('aria-label')
                rating_list.append(score.split(' ')[3][0:3])
                

        #리뷰 스크래핑
        reviewss = driver.find_elements(By.CLASS_NAME,'_T.FKffI')
        review_title = driver.find_elements(By.CLASS_NAME, 'biGQs._P.fiohW.qWPrE.ncFvv.fOtGX')
        for rev_t in review_title:
            reviews_t = rev_t.find_elements(By.CLASS_NAME, 'yCeTE')
            for review_t in reviews_t:
                text_t = review_t.text
                title_list.append(text_t)
        for rev in reviewss:
            reviews = rev.find_elements(By.CLASS_NAME, 'yCeTE')
            for review in reviews:
                text = review.text
                review_list.append(text)
                name_list.append(name)
            

        try:
            sample = driver.find_element(By.XPATH,'//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[11]/div[1]/div/div[1]/div[2]/div/a')
            sample.click()
        except:
            pass
    

#딕셔너리 > 데이터프레임
column_name = ['name', 'rating', 'title', 'review']
df = pd.DataFrame(columns = column_name)
df['name'] = name_list
df['rating'] = rating_list
df['title'] = title_list
df['review'] = review_list
df['review'] = df['title'] + ' ' + df['review']
#csv로 저장
df.to_csv('review[100-120].csv', encoding = 'utf-8-sig')


    
    


#리스트 생성
review_list = []
rating_list = []
name_list = []
title_list = []

#브라우저 생성
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

driver = webdriver.Chrome(chrome_options=chrome_options)


for url in url_list[120:140]:
    
    #페이지 열기
    driver.get(url)
    driver.implicitly_wait(10)

    #전체 페이지
    try:
        num = driver.find_element(By.CLASS_NAME,'Ci')
    except:
        pass
    
    try:
        page = int(int(num.text.split(' ')[3])/10)
    except:
        page = 1

    for i in range(0, page):
        #명소 이름
        name = driver.find_element(By.CSS_SELECTOR,'.fiohW')
        name = name.text

        #명소 평점
        ratingss = driver.find_elements(By.CLASS_NAME, 'LbPSX')
        for rat in ratingss:
            ratings = rat.find_elements(By.CLASS_NAME, 'UctUV')
            for rating in ratings:
                score = rating.get_attribute('aria-label')
                rating_list.append(score.split(' ')[3][0:3])
                

        #리뷰 스크래핑
        reviewss = driver.find_elements(By.CLASS_NAME,'_T.FKffI')
        review_title = driver.find_elements(By.CLASS_NAME, 'biGQs._P.fiohW.qWPrE.ncFvv.fOtGX')
        for rev_t in review_title:
            reviews_t = rev_t.find_elements(By.CLASS_NAME, 'yCeTE')
            for review_t in reviews_t:
                text_t = review_t.text
                title_list.append(text_t)
        for rev in reviewss:
            reviews = rev.find_elements(By.CLASS_NAME, 'yCeTE')
            for review in reviews:
                text = review.text
                review_list.append(text)
                name_list.append(name)
            

        try:
            sample = driver.find_element(By.XPATH,'//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[11]/div[1]/div/div[1]/div[2]/div/a')
            sample.click()
        except:
            pass
    

#딕셔너리 > 데이터프레임
column_name = ['name', 'rating', 'title', 'review']
df = pd.DataFrame(columns = column_name)
df['name'] = name_list
df['rating'] = rating_list
df['title'] = title_list
df['review'] = review_list
df['review'] = df['title'] + ' ' + df['review']
#csv로 저장
df.to_csv('review[120-140].csv', encoding = 'utf-8-sig')





#리스트 생성
review_list = []
rating_list = []
name_list = []
title_list = []

#브라우저 생성
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

driver = webdriver.Chrome(chrome_options=chrome_options)


for url in url_list[140:160]:
    
    #페이지 열기
    driver.get(url)
    driver.implicitly_wait(10)

    #전체 페이지
    try:
        num = driver.find_element(By.CLASS_NAME,'Ci')
    except:
        pass
    
    try:
        page = int(int(num.text.split(' ')[3])/10)
    except:
        page = 1

    for i in range(0, page):
        #명소 이름
        name = driver.find_element(By.CSS_SELECTOR,'.fiohW')
        name = name.text

        #명소 평점
        ratingss = driver.find_elements(By.CLASS_NAME, 'LbPSX')
        for rat in ratingss:
            ratings = rat.find_elements(By.CLASS_NAME, 'UctUV')
            for rating in ratings:
                score = rating.get_attribute('aria-label')
                rating_list.append(score.split(' ')[3][0:3])
                

        #리뷰 스크래핑
        reviewss = driver.find_elements(By.CLASS_NAME,'_T.FKffI')
        review_title = driver.find_elements(By.CLASS_NAME, 'biGQs._P.fiohW.qWPrE.ncFvv.fOtGX')
        for rev_t in review_title:
            reviews_t = rev_t.find_elements(By.CLASS_NAME, 'yCeTE')
            for review_t in reviews_t:
                text_t = review_t.text
                title_list.append(text_t)
        for rev in reviewss:
            reviews = rev.find_elements(By.CLASS_NAME, 'yCeTE')
            for review in reviews:
                text = review.text
                review_list.append(text)
                name_list.append(name)
            

        try:
            sample = driver.find_element(By.XPATH,'//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[11]/div[1]/div/div[1]/div[2]/div/a')
            sample.click()
        except:
            pass
    

#딕셔너리 > 데이터프레임
column_name = ['name', 'rating', 'title', 'review']
df = pd.DataFrame(columns = column_name)
df['name'] = name_list
df['rating'] = rating_list
df['title'] = title_list
df['review'] = review_list
df['review'] = df['title'] + ' ' + df['review']
#csv로 저장
df.to_csv('review[140-160].csv', encoding = 'utf-8-sig')







#리스트 생성
review_list = []
rating_list = []
name_list = []
title_list = []

#브라우저 생성
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

driver = webdriver.Chrome(chrome_options=chrome_options)


for url in url_list[160:180]:
    
    #페이지 열기
    driver.get(url)
    driver.implicitly_wait(10)

    #전체 페이지
    try:
        num = driver.find_element(By.CLASS_NAME,'Ci')
    except:
        pass
    
    try:
        page = int(int(num.text.split(' ')[3])/10)
    except:
        page = 1

    for i in range(0, page):
        #명소 이름
        name = driver.find_element(By.CSS_SELECTOR,'.fiohW')
        name = name.text

        #명소 평점
        ratingss = driver.find_elements(By.CLASS_NAME, 'LbPSX')
        for rat in ratingss:
            ratings = rat.find_elements(By.CLASS_NAME, 'UctUV')
            for rating in ratings:
                score = rating.get_attribute('aria-label')
                rating_list.append(score.split(' ')[3][0:3])
                

        #리뷰 스크래핑
        reviewss = driver.find_elements(By.CLASS_NAME,'_T.FKffI')
        review_title = driver.find_elements(By.CLASS_NAME, 'biGQs._P.fiohW.qWPrE.ncFvv.fOtGX')
        for rev_t in review_title:
            reviews_t = rev_t.find_elements(By.CLASS_NAME, 'yCeTE')
            for review_t in reviews_t:
                text_t = review_t.text
                title_list.append(text_t)
        for rev in reviewss:
            reviews = rev.find_elements(By.CLASS_NAME, 'yCeTE')
            for review in reviews:
                text = review.text
                review_list.append(text)
                name_list.append(name)
            

        try:
            sample = driver.find_element(By.XPATH,'//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[11]/div[1]/div/div[1]/div[2]/div/a')
            sample.click()
        except:
            pass
    

#딕셔너리 > 데이터프레임
column_name = ['name', 'rating', 'title', 'review']
df = pd.DataFrame(columns = column_name)
df['name'] = name_list
df['rating'] = rating_list
df['title'] = title_list
df['review'] = review_list
df['review'] = df['title'] + ' ' + df['review']
#csv로 저장
df.to_csv('review[160-180].csv', encoding = 'utf-8-sig')






#리스트 생성
review_list = []
rating_list = []
name_list = []
title_list = []

#브라우저 생성
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

driver = webdriver.Chrome(chrome_options=chrome_options)


for url in url_list[180:200]:
    
    #페이지 열기
    driver.get(url)
    driver.implicitly_wait(10)

    #전체 페이지
    try:
        num = driver.find_element(By.CLASS_NAME,'Ci')
    except:
        pass
    
    try:
        page = int(int(num.text.split(' ')[3])/10)
    except:
        page = 1

    for i in range(0, page):
        #명소 이름
        name = driver.find_element(By.CSS_SELECTOR,'.fiohW')
        name = name.text

        #명소 평점
        ratingss = driver.find_elements(By.CLASS_NAME, 'LbPSX')
        for rat in ratingss:
            ratings = rat.find_elements(By.CLASS_NAME, 'UctUV')
            for rating in ratings:
                score = rating.get_attribute('aria-label')
                rating_list.append(score.split(' ')[3][0:3])
                

        #리뷰 스크래핑
        reviewss = driver.find_elements(By.CLASS_NAME,'_T.FKffI')
        review_title = driver.find_elements(By.CLASS_NAME, 'biGQs._P.fiohW.qWPrE.ncFvv.fOtGX')
        for rev_t in review_title:
            reviews_t = rev_t.find_elements(By.CLASS_NAME, 'yCeTE')
            for review_t in reviews_t:
                text_t = review_t.text
                title_list.append(text_t)
        for rev in reviewss:
            reviews = rev.find_elements(By.CLASS_NAME, 'yCeTE')
            for review in reviews:
                text = review.text
                review_list.append(text)
                name_list.append(name)
            

        try:
            sample = driver.find_element(By.XPATH,'//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[11]/div[1]/div/div[1]/div[2]/div/a')
            sample.click()
        except:
            pass
    

#딕셔너리 > 데이터프레임
column_name = ['name', 'rating', 'title', 'review']
df = pd.DataFrame(columns = column_name)
df['name'] = name_list
df['rating'] = rating_list
df['title'] = title_list
df['review'] = review_list
df['review'] = df['title'] + ' ' + df['review']
#csv로 저장
df.to_csv('review[180-200].csv', encoding = 'utf-8-sig')