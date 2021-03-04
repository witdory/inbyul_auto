from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random
from korean_name_generator import namer
import string
import time
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(
    "/Users/goyoonjae/Desktop/insta_follower/chromedriver")
url = 'http://www.instagram.com'
driver.get(url)
time.sleep(2)
da = Alert(driver)


driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(2) > div > p > a > span').click()  # 회원가입버튼

print("가입하기")

_LENGTH = 12  # 12자리 # 숫자 + 대소문자
string_pool = string.ascii_letters + string.digits +"1"+"e"  # 랜덤한 문자열 생성
result = ""
for i in range(_LENGTH):
    result += random.choice(string_pool)  # 랜덤한 문자열 하나 선택
password = result+"??"  # 비밀번호 생성
result = ""
for i in range(_LENGTH):
    result += random.choice(string_pool)  # 랜덤한 문자열 하나 선택
userid = result  # 아이디 생성

_LENGTH = 8
string_pool = string.digits
result = ""
for i in range(_LENGTH):
    result += random.choice(string_pool)
num = '010'+result

name = namer.generate(True)

a=userid+'@ruu.kr'

print("아이디 이메일 생성 성공")

driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input""").send_keys('dd')

