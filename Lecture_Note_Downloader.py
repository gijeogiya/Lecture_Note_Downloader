from selenium import webdriver
from time import sleep


def login():  # 로그인
    driver.find_element_by_name('userId').send_keys('이곳에 아이디를 입력하면 됩니다')
    sleep(0.5)
    driver.find_element_by_name('userPwd').send_keys('이곳에 비밀번호를 입력하면 됩니다')
    sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/form/div/div[2]/div[3]/a').click()
    sleep(0.5)


# 에듀 싸피 열기
driver = webdriver.Chrome('절대주소/chromedriver.exe')
driver.get('https://edu.ssafy.com')
sleep(0.5)

login()

total_page = 54

for idx in range(1, total_page + 1):  # 페이지를 띄우는 작업을 페이지 인덱스 마다 반복
    idx_str = str(idx).zfill(4)  # 0001, 0002, 0003 ... 등의 형태로 문자열을 변환
    driver.execute_script(
        f'window.open("https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2022040610595166300/assets/page-images/page-9aa9a3c9-51dc16b0-{idx_str}");')  # 자바 스크립트 형태로 새 탭을 띄워 주는 형식
    sleep(0.5)