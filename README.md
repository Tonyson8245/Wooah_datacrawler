# 우아 데이터수집 서버
우아-우리들의아름다움을 개발하면서 사용한 데이터 수집 서버 레포지토리입니다.

### 사용 언어
- Python

### 사용 기술
- Python
- selenium
- beatifulsoup4
- Numpy
- Pandas


### 환경
Ubuntu 22.04.01 LTS / Chrome : 106.5249.xx.xx

1. 최신 크롬 설치
2. [https://chromedriver.storage.googleapis.com](https://chromedriver.storage.googleapis.com/index.html) 에서 현재 크롬 버전에 맞춰(Major version) 다운로드하기
3. beatifulsoup4 설치 : *pip install beutifulsoup4*
4. selenium 설치 : *pip install selenium==3.14.1*
→ 구버전으로 작성!!
5. webdriver_manager 설치 : *pip install webdriver-manager*
6. /var/gucci/Instagram 경로에서 *python3 InstagramCrawler.py* 실헹

### 수정시 주의 할점

- driver 객체는 사용이 끝나면, driver.quit 을 통해 필히 종료 시킬 것!!

### 에러

- `ModuleNotFoundError: No module named 'bs4’`
    
    *pip install beutifulsoup4*
    
    [No Module Named bs4 beautifulsoup python 파이썬](https://studyhard24.tistory.com/235)
    
- pip 미설치시
    
    *sudo apt install python3-pip*
    
- `ModuleNotFoundError: No module named 'selenium’`
    
    *pip install selenium*
    
    [셀레니움 모듈 에러, ModuleNotFoundError: No module named 'selenium' 해결](https://shwank77.tistory.com/1588)
    
- `ModuleNotFoundError: No module named 'webdriver_manager’`
    
     *pip install webdriver-manager*
    
- `ModuleNotFoundError: No module named 'packaging’`
    
    *pip3 install packaging*
    
    [No module named packaging](https://stackoverflow.com/questions/42222096/no-module-named-packaging)
    
- `DeprecationWarning: executable_path has been deprecated, please pass in a Service object`
    
    구버전으로 작성 필요
    ex) *pip install selenium==3.14.1*
    
    [[셀레니움 기초] executable_path has been deprecated, please pass in a Service object 에러 해결 방법](https://yeko90.tistory.com/entry/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EA%B8%B0%EC%B4%88-executablepath-has-been-deprecated-please-pass-in-a-Service-object-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0-%EB%B0%A9%EB%B2%95)
