# Lecture_Note_Downloader

2022.04.06

## 개발 동기와 목적

나는 삼성 청년 SW 아카데미 교육을 받고 있다. 코로나19 때문에 온라인으로 교육이 진행되고 있다. 그런데 굉장히 불만족스러운 사항이 있다. 그것은 바로 절대 강의 노트를 다운 받지 못하게 막아놨다는 것이다. 열람은 가능하지만 pdf, img 형태로 절대 다운 받지 못하게 해놨다. 요즘 같은 Paperless 시대에 강의 노트를 공유하지 않는다는 것이 말이나 되는 소리인가! 강의 노트를 배포하는 것은 불법이겠지만, 나는 강의노트를 열람할 권한을 가진 교육생 신분이니 "나의 강의 수강의 편의"를 위해 크롤링하여 pdf 파일 형태로 다운 받아보려고 한다.



## 사이트 분석

### 강의 노트 페이지

마우스 우클릭, pdf로 내보내기 전부 막아놨다. 그래서 개발자 도구를 이용하여 이미지 경로를 찾아보았다.

src = assets/page-images/page-40ba6a20-b2bfbccd-0001.jpg

이런 형태로 되었다. urllib.request을 이용해서 크롤링하려고 했다.



### 로그인 페이지

로그인 후 작업이 이루어져야했기 때문에 로그인 과정에서 login form 을 찾아나섰다.

다른 사이트들과 다르게 네트워크 창을 아무리 뒤져봐도 login form은 커녕 form 탭을 발견 할 수 없었다. (강력한 삼성... 부들부들)

결국 셀레니움으로 이미지 페이지를 모두 띄워서 수작업으로 다운받는 방법이 내가 생각해낼수 있는 최선의 방법이었다.



### 코드

```python
from selenium import webdriver
from time import sleep

def login(): #  로그인
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
    driver.execute_script(f'window.open("이곳에 강의노트 이미지 주소를 입력하세요-{idx_str}.jpg");')  #자바 스크립트 형태로 새 탭을 띄워 주는 형식
    sleep(0.5)
```



## 결론

완벽한 자동화에는 실패했지만, 그래도 강의 시작하기 몇 분 전쯤에 강의 노트를 다운 받을 수 있게 되었다. 시행착오가 있었던 덕분에 BeautifulSoup, Selenium, urllib.request, HTML, 네트워크 방식 등 여러 도메인을 건들어 볼 수 있었다. 난 이제 SSAFY HW하러 가야지... 총총총



## 사용 환경 및 사용법

### 사용 환경

- python             3.10.4          
- selenium             4.1.0
- chromedriver              # 각 pc환경에 알맞은 버전을 사용



### 사용법

- '이곳에 아이디를 입력하면 됩니다'에 id를 문자열로 작성
- '이곳에 비밀번호를 입력하면 됩니다'에 pw를 문자열로 작성
- '이곳에 강의노트의 총 페이지를 입력하세요'에 총 페이지 수 정수형으로 작성
- 이곳에 강의노트 이미지 주소를 입력하세요에 강의 노트 이미지 주소의 페이지 값을 제외한 부분을 작성
- 실행



## 개선 (2022.04.26)

### 기능

직접 입력장치에 접근하여 띄어놓은 이미지 창을 저장하는 기능 추가

### Code

```python
import pyautogui

for _ in range(1, total_page + 1):  # 이미지를 저장하고 페이지를 제거하는 작업을 페이지 수 만큼 반복
    pyautogui.hotkey('ctrl', 's')   #  페이지 저장 창 띄우기
    sleep(1)
    pyautogui.press('enter')   #  엔터키 누르기
    sleep(1)
    pyautogui.hotkey('ctrl', 'w')   #  크롬 탭 1개 없애기
    sleep(0.5)

```

### 주의사항

입력장치에 직접 접근하여 동작하는 매크로인 만큼 프로그램이 동작하는중에 다른 걸 건들어도 컨트롤S키, 엔터키, 컨트롤W키가 반복해서 눌리니 주의!
다른 동작을 해버려 꼬여버렸다면 프로그램을 종료하자.