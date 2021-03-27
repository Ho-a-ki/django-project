# 장고 튜토리얼

https://docs.djangoproject.com/ko/3.1/intro/tutorial01/
간단한 설문조사 만들기.

### 고려해볼 만 한 것
코딩 그자체로.
* 테스트 케이스의 작성
* python 타입힌트의 설정(그나마 이게 제일)
* OOP로 작성.


## 첫번째 장고 앱 작성하기.
### part1
https://docs.djangoproject.com/ko/3.1/intro/tutorial01/


* 프로젝트 대 앱
What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

```
python manage.py startapp polls
```

앱을 여러가지 생성할 수 있다는 거.


* 첫번째 뷰 생성 view.py 수정
* URLconf의 존재. > app에서 사용하기 위해선 urls.py를 생성해야함.
* urls.py에서 쓰이는 path 함수의 4가지 인수


### part2

데이터베이스를 설치하고 첫 모델을 생성한 후, Django에서 자동 생성되는 관리자 사이트에 대해 짧게 소개합니다.

django에서 생성하는 admin이 굉장히 편하다는 이슈가 있지 암.

> mysite/settings.py를 편집할 때, 당신의 시간대에 맞춰 TIME_ZONE 값을 설정하세요.
* TIME_ZONE = 
* LANGUAGE_CODE = 'ko

https://devlog.jwgo.kr/2019/12/24/django-3-language-code-error/'

---

또한, 이 파일의 윗쪽에 있는 INSTALLED_APPS 에 대해 언급하자면, 이 파일은 현재 Django 인스턴스에서 활성화된 모든 Django 어플리케이션들의 이름이 담겨 있습니다. 앱들은 다수의 프로젝트에서 사용될 수 있고, 다른 프로젝트에서 쉽게 사용될 수 있도록 패키징하여 배포할 수 있습니다.

기본적으로는, INSTALLED_APPS는 Django와 함께 딸려오는 다음의 앱들을 포함합니다.


이러한 기본 어플리케이션들 중 몇몇은 최소한 하나 이상의 데이터베이스 테이블을 사용하는데, 그러기 위해서는 데이터베이스에서 테이블을 미리 만들 필요가 있습니다. 이를 위해, 다음의 명령을 실행해봅시다.

```
python manage.py migrate
```

모델 만들기

이제, 모델을 정의해 보겠습니다. 본질적으로, 모델이란 부가적인 메타데이터를 가진 데이터베이스의 구조(layout)를 말합니다.

모델(《model》)은 데이터에 관한 단 하나의, 가장 확실한 진리의 원천입니다. 이것은 당신이 저장하는 데이터의 필수적인 필드들과 동작들을 포함하고 있습니다. Django 는 DRY 원칙 을 따릅니다. 이 원칙에 따라 데이터 모델을 한곳에서 정의하고, 이것으로부터 자동으로 뭔가를 유도하는 것이 목표입니다.

* polls/models.py 수정

모델의 활성화¶
모델에 대한 이 작은 코드가, Django에게는 상당한 양의 정보를 전달합니다. Django는 이 정보를 가지고 다음과 같은 일을 할 수 있습니다.

이 앱을 위한 데이터베이스 스키마 생성(CREATE TABLE 문)
Question과 Choice 객체에 접근하기 위한 Python 데이터베이스 접근 API를 생성
그러나, 가장 먼저 현재 프로젝트에게 polls 앱이 설치되어 있다는 것을 알려야 합니다

앱을 현재의 프로젝트에 포함시키기 위해서는, 앱의 구성 클래스에 대한 참조를 INSTALLED_APPS 설정에 추가해야 합니다. PollsConfig 클래스는 polls/apps.py 파일 내에 존재합니다. 따라서, 점으로 구분된 경로는 'polls.apps.PollsConfig'가 됩니다. 이 점으로 구분된 경로를, mysite/settings.py 파일을 편집하여 INSTALLED_APPS 설정에 추가하면 됩니다. 이는 다음과 같이 보일 것입니다.

* 셋팅에 설치된 앱에 polls를 추가한 후에
* 장고에게 이 앱이 추가됐다는 것을 알려줌
```
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
python manage.py migrate
```

### 모델을 만드는 3가지 순서

1. (models.py 에서) 모델을 변경합니다.
2. python manage.py makemigrations을 통해 이 변경사항에 대한 마이그레이션을 만드세요.
3. python manage.py migrate 명령을 통해 변경사항을 데이터베이스에 적용하세요.


* 대화식 API 사용하기
```
python manage.py shell
```
다음의 명령어를 통해 shell로 접속하여 장고와 실시간으로 터미널로 소통가능
DB에 접근해서 특정 데이터를 생성하든지 수정하든지 등등.

* 파이썬에서 시간대 다루기
https://docs.djangoproject.com/ko/3.1/topics/i18n/timezones/


* 관리자 생성하기
```
python manage.py createsuperuser
```

관리자 어떻게 지우냐 ? > 사용자들 들어가서 지우면됨. 진짜 기본적인게 되어있어서 편하네


* 관리 사이트에서 poll app 을 변경가능하도록 만들기
그런데, poll app 이 관리 인덱스 페이지에서 보이지 않네요. 어디에 있을까요?

Only one more thing to do: we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py file, and edit it to look like this:

polls/admin.py¶
from django.contrib import admin

from .models import Question

admin.site.register(Question)

> 와 이건 진짜 편하다..

---
일단 오늘은 여기까지 2021 03 27