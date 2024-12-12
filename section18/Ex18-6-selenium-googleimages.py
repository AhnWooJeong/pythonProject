'''
파일 명: Ex18-6-selenium-googleimages.py

selenium 패키지
    어플리케이션 테스트하기 위한 프레임웍 이다.
    웹 어플리케이션 다양한 브라우저 동작 테스트용!
    웹 크롤링으로 많이 사용된다.

# 브라우저 컨트롤 패키지
pip install selenium
# selenium 에서 사용하는 브라우저 드라이버 자동관리 도구
pip install webdriver-manager
'''

import os
import  time
import  urllib.request
from ast import Bytes
from re import search

from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

# Chrome driver 자동 설치 및 서비스 생성
service = Service(ChromeDriverManager().install())

# Chrome 드라이버 인스턴스 생성
driver = webdriver.Chrome(service=service)

# 드라이버를 통해 Google 페이지 접속
driver.get("https://images.google.com/")

# 키워드
keyword = 'cute cat'

# 검색어 입력
search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys(keyword)
search_bar.send_keys(Keys.RETURN)

thumbnails = driver.find_element(By.CSS_SELECTOR)

time.sleep(3000)

# 드라이버 종료
driver.quit()













