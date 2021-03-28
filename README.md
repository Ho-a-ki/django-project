

# 새로운 곳에서 처음 시작할 때의 세팅

1. 콘다 설치
2. 깃 설치
3. VS code 설치


## GIT
1. git clone
2. git config

## VS CODE
1. python extension 설치.
2. markdown preview (Yiyi Wang)

## CONDA
1. conda create -n gh-django python=3.8
2. conda activate gh-django
3. pip install -r requirements.txt
4. pip freezee > requirements.txt

## django
1. 처음 시작할 떄 DB가 생성되어있지 않아서 마이그레이션을 해줘야함
```
python manage.py sqlmigrate polls 0001
python manage.py migrate
```

2. 역시 새로 설치할 경우 DB가 다 날아가기 때문에, 새로 만들어줘야함
3. superuser도 마찬가지
```
python manage.py createsuperuser
```




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
어느새 3.~ 버전이 나왔구나..

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
[tutorial.md](./tutorial.md) 참고


### 무엇을 만들것인가?
[commute_check.md](./commute_check.md) 참고


### 참고해보기
django with jquery.
php, jquery 배우기 정말 싫은데
jquery > js로 그냥 하는 이슈에 대해서

https://wayhome25.github.io/django/2017/06/25/django-ajax-like-button/

https://heiswed.tistory.com/entry/%EC%9E%A5%EA%B3%A0Django-%EA%B0%9C%EB%B0%9C-JQuery%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-Ajax%EC%99%80-Autocomplete-%EC%98%88%EC%A0%9C

