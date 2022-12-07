# 크롬 드라이브 이용해서 크롤링
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()

options.add_argument('leng=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe', options=options)

url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?year=2022$page=1'

