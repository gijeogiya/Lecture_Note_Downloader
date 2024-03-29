from selenium import webdriver
from time import sleep

'''
WARNING! 입력장치에 직접 접근하여 동작하는 매크로인 만큼 프로그램이 동작하는중에 다른 걸 건들어도 컨트롤S키, 엔터키, 컨트롤W키가 반복해서 눌리니 주의!
다른 동작을 해버려 꼬여버렸다면 프로그램을 종료하자.
'''

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

total_page = '이곳에 강의노트의 총 페이지를 입력하세요'

for idx in range(1, total_page + 1):  # 페이지를 띄우는 작업을 페이지 인덱스 마다 반복
    idx_str = str(idx).zfill(4)  # 0001, 0002, 0003 ... 등의 형태로 문자열을 변환
    driver.execute_script(f'window.open("이곳에 강의노트 이미지 주소를 입력하세요-{idx_str}.jpg");')  # 자바 스크립트 형태로 새 탭을 띄워 주는 형식
    sleep(0.5)


for _ in range(1, total_page + 1):  # 이미지를 저장하고 페이지를 제거하는 작업을 페이지 수 만큼 반복
    pyautogui.hotkey('ctrl', 's')   #  페이지 저장 창 띄우기
    sleep(1)
    pyautogui.press('enter')   #  엔터키 누르기
    sleep(1)
    pyautogui.hotkey('ctrl', 'w')   #  크롬 탭 1개 없애기
    sleep(0.5)