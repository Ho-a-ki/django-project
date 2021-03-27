
# django github

## 시작하기

* 깃 설치
* 깃허브에 repo 생성.
* 이후 로컬 깃에다가 연결 시키기

* 깃허브 관련 참고  https://tagilog.tistory.com/377

### 초기 세팅 관련

* git clone https://github.com/Ho-a-ki/django-project.git 

깃허브에 연결되어있는 깃을 clone하여 시작.

* git config --global user.email 'gh4777@naver.com'
* git config --global user.name 'gh'

* git add *

* git commit -m 'msg'

* git push

---

## python 초기 세팅하기.

### 1. miniconda 설치. > path 추가

### 2. 가상환경 사용하기.
miniconda에서 사용하는 가상환경 사용하기.
https://sdc-james.gitbook.io/onebook/2./2.1./2.1.1./2-conda-virtual-environments

* 가상환경 생성하기
```
conda create -n [name] python=[ver]
conda create -n gh-django python=3.8
```

* 가상환경 활성/비활성
```
conda activate gh-django
conda deactivate
```

### 3. 패키지 관리하는 법
(다음의 링크를 참고 requirements로 관련 관리)
https://itholic.github.io/python-requirements/



* 가상환경 활성한 후에 필요한 패키지들 설치

```
pip install requests
pip install django
```

## django 시작하기
https://docs.djangoproject.com/ko/3.1/intro/
> 어느새 3.~ 버전이 나왔구나..

* 장고 버전 확인
```
python -m django --version
```

* 프로젝트 만들기
```
django-admin startproject mysite
```

* 장고 서버 Run하기
```
python manage.py runserver
python manage.py runserver 0:8000 (로컬 서버에 오픈하고 싶다면)
```
아무런 설정이 안되어있다면 http://127.0.0.1:8000/ 에서 접근 가능

귀찮으니 db는 그냥 가벼운 sqlite3를 쓰자.

* 어드민은 http://127.0.0.1:8000/admin 에서 확인 가능


### tutorial 설문조사 앱 만들어보기.

필요한 것을 만들기 전에 tutorial은 한번 해보자.


### 무엇을 만들것인가?
[commute_check.md](./commute_check.md) 참고