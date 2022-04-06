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

total_page = 54

for idx in range(1, total_page + 1):  # 페이지를 띄우는 작업을 페이지 인덱스 마다 반복
    idx_str = str(idx).zfill(4)  # 0001, 0002, 0003 ... 등의 형태로 문자열을 변환
    driver.execute_script(f'window.open("https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2022040610595166300/assets/page-images/page-9aa9a3c9-51dc16b0-{idx_str}");')  #자바 스크립트 형태로 새 탭을 띄워 주는 형식
    sleep(0.5)
```



## 결론

완벽한 자동화에는 실패했지만, 그래도 강의 시작하기 몇 분 전쯤에 강의 노트를 다운 받을 수 있게 되었다. 시행착오가 있었던 덕분에 BeautifulSoup, Selenium, urllib.request, HTML, 네트워크 방식 등 여러 도메인을 건들어 볼 수 있었다. 난 이제 SSAFY HW하러 가야지... 총총총