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

driver.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(4) > div > label > input').click()

driver.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(4) > div > label > input').send_keys(a)




'''

driver.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(6) > div > label > input').send_keys(userid)

driver.find_element_by_css_selector('#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(6) > div > label > input').send_keys(userid)




driver.find_element_by_css_selector('#agree11').click()  # 동의버튼1
driver.find_element_by_css_selector('#agree21').click()  # 동의버튼2
driver.find_element_by_css_selector(
    '#fregister > div > input').click()  # 마지막확인버튼
div = random.randrange(1, 4)
sex = random.randrange(1, 3)




def like():

    driver.get("http://www.steamcup.org/ko/service/robot_gallery_view.php?gal_idx=2299830")
    driver.find_element_by_css_selector(
        '#bo_v_atc > table > tbody > tr:nth-child(9) > td > button').click()
    print("추천 완료!")


def st_login():

    driver.switch_to.window(driver.window_handles[2])

    # driver.get('http://www.steamcup.org/ko')
    driver.find_element_by_css_selector(
        '#nav > div.gnb.dis_web > div.gnb_body > div > ul > li:nth-child(3) > a > b').click()
    driver.find_element_by_css_selector('#login_id').click()
    driver.find_element_by_css_selector('#login_id').send_keys(userid)
    driver.find_element_by_css_selector('#login_pw').click()
    driver.find_element_by_css_selector('#login_pw').send_keys(password)
    driver.find_element_by_css_selector(
        '#container > div.body_wrap.loginskin > section.sub_2_col.clearfix > div > div > form > div.login_btn_box > input').click()
    print("로그인 성공!")


def mail_open():
    driver.execute_script('window.open("https://www.ruu.kr")')
    print("ruu.kr 접속 성공!")
    # ==========================================
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(0.5)
    driver.find_element_by_css_selector('#id').click()
    driver.find_element_by_css_selector('#id').send_keys(userid)
    time.sleep(2)
    driver.find_element_by_css_selector('#mailList').click()
    time.sleep(3)
    driver.find_element_by_css_selector(
        '#mail > table > tbody > tr > td:nth-child(2) > font').click()
    time.sleep(1)

    driver.find_element_by_xpath("""//*[@id="view"]/div/div/p/a""").click()
    driver.switch_to.window(driver.window_handles[2])
    da.accept()
    print("창 닫기 완료")


def stranger():

    driver.find_element_by_css_selector('#reg_mb_name').click()
    driver.find_element_by_css_selector('#reg_mb_name').send_keys(name)
    driver.find_element_by_css_selector('#reg_mb_id').click()
    driver.find_element_by_css_selector('#reg_mb_id').send_keys(userid)
    driver.find_element_by_css_selector('#reg_mb_password').click()
    driver.find_element_by_css_selector('#reg_mb_password').send_keys(password)
    driver.find_element_by_css_selector('#reg_mb_password_re').click()
    driver.find_element_by_css_selector(
        '#reg_mb_password_re').send_keys(password)
    driver.find_element_by_css_selector('#reg_mb_sosok').click()
    driver.find_element_by_css_selector('#reg_mb_sosok').send_keys("무소속")
    driver.find_element_by_css_selector('#reg_mb_hp').click()
    driver.find_element_by_css_selector('#reg_mb_hp').send_keys(num)
    driver.find_element_by_css_selector('#reg_mb_email').click()
    driver.find_element_by_css_selector(
        '#reg_mb_email').send_keys(userid+'@ruu.kr')
    bd = random.randrange(1980, 2002)*10000 + \
        random.randrange(1, 13)*100 + random.randrange(1, 28)
    driver.find_element_by_css_selector('#mb_birth').click()
    driver.find_element_by_css_selector('#mb_birth').send_keys(bd)
    driver.find_element_by_css_selector('#reg_mb_mailling').click()
    driver.find_element_by_css_selector('#reg_mb_sms').click()
    driver.find_element_by_css_selector('#fregisterform > div > a').click()


def parent():
    driver.find_element_by_css_selector('#reg_mb_name').click()
    driver.find_element_by_css_selector('#reg_mb_name').send_keys(name)
    driver.find_element_by_css_selector('#reg_mb_id').click()
    driver.find_element_by_css_selector('#reg_mb_id').send_keys(userid)
    driver.find_element_by_css_selector('#reg_mb_password').click()
    driver.find_element_by_css_selector('#reg_mb_password').send_keys(password)
    driver.find_element_by_css_selector('#reg_mb_password_re').click()
    driver.find_element_by_css_selector(
        '#reg_mb_password_re').send_keys(password)
    driver.find_element_by_css_selector('#reg_mb_sosok').click()
    driver.find_element_by_css_selector('#reg_mb_sosok').send_keys("학부모")
    driver.find_element_by_css_selector('#reg_mb_hp').click()
    driver.find_element_by_css_selector('#reg_mb_hp').send_keys(num)
    driver.find_element_by_css_selector('#reg_mb_email').click()
    driver.find_element_by_css_selector(
        '#reg_mb_email').send_keys(userid+'@ruu.kr')
    bd = random.randrange(1980, 1990)*10000 + \
        random.randrange(1, 13)*100 + random.randrange(1, 28)
    driver.find_element_by_css_selector('#mb_birth').click()
    driver.find_element_by_css_selector('#mb_birth').send_keys(bd)
    driver.find_element_by_css_selector('#reg_mb_mailling').click()
    driver.find_element_by_css_selector('#reg_mb_sms').click()
    driver.find_element_by_css_selector('#fregisterform > div > a').click()


def student():

    driver.find_element_by_css_selector('#reg_mb_name').click()
    driver.find_element_by_css_selector('#reg_mb_name').send_keys(name)
    driver.find_element_by_css_selector('#reg_mb_id').click()
    driver.find_element_by_css_selector('#reg_mb_id').send_keys(userid)
    driver.find_element_by_css_selector('#reg_mb_password').click()
    driver.find_element_by_css_selector('#reg_mb_password').send_keys(password)
    driver.find_element_by_css_selector('#reg_mb_password_re').click()
    driver.find_element_by_css_selector(
        '#reg_mb_password_re').send_keys(password)
    driver.find_element_by_css_selector('#reg_mb_sosok').click()
    driver.find_element_by_css_selector('#reg_mb_sosok').send_keys("고등학교")
    driver.find_element_by_css_selector('#reg_mb_hp').click()
    driver.find_element_by_css_selector('#reg_mb_hp').send_keys(num)
    driver.find_element_by_css_selector('#reg_mb_email').click()
    driver.find_element_by_css_selector(
        '#reg_mb_email').send_keys(userid+'@ruu.kr')
    bd = random.randrange(2002, 2005)*10000 + \
        random.randrange(1, 13)*100 + random.randrange(1, 28)
    driver.find_element_by_css_selector('#mb_birth').click()
    driver.find_element_by_css_selector('#mb_birth').send_keys(bd)
    driver.find_element_by_css_selector('#reg_mb_mailling').click()
    driver.find_element_by_css_selector('#reg_mb_sms').click()
    driver.find_element_by_css_selector('#fregisterform > div > a').click()

'''


