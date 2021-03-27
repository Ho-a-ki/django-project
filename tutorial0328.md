# ✔ 장고 튜토리얼 03 28 

### 짧은 복습 😊

프로젝트 만들기 (가장 큰 뿌리)
앱 만들기 (여러개 만들 수 있지)
뷰 만들기

모델 만들기 (SQLite 사용하기)
모델을 생성된 앱에 추가하기.
모델을 만들었을 때 해야하는 3가지 액션 
관리자 생성하기.
관리사이트에서 APP 추가하기.


## PART3
https://docs.djangoproject.com/ko/3.1/intro/tutorial03/

> 투표 어플리케이션에 공개 인터페이스인 《뷰(view)》를 추가해 보겠습니다.
우리가 만드는 poll 어플리케이션에서 다음과 같은 네개의 view 를 만들어 보겠습니다.

> 질문 《색인》 페이지 – 최근의 질문들을 표시합니다.
질문 《세부》 페이지 – 질문 내용과, 투표할 수 있는 서식을 표시합니다.
질문 《결과》 페이지 – 특정 질문에 대한 결과를 표시합니다
투표 기능 – 특정 질문에 대해 특정 선택을 할 수 있는 투표 기능을 제공합니다.

> In Django, web pages and other content are delivered by views. Each view is represented by a Python function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).

장고에서는, 웹페이지를 보여주기 위해서 views를 사용하며 각각의 view는 하나의 function으로 연결된다. 

* 뷰 추가하기

> 작동하는 방식 
사용자가 웹사이트의 페이지를 요청할 때, 예로 《/polls/34/》를 요청했다고 하면, Django는 mysite.urls 파이썬 모듈을 불러오게 됩니다. ROOT_URLCONF 설정에 의해 해당 모듈을 바라보도록 지정되어 있기 때문입니다. mysite.urls에서 urlpatterns라는 변수를 찾고, 순서대로 패턴을 따라갑니다. 'polls/'를 찾은 후엔, 일치하는 텍스트("polls/")를 버리고, 남은 텍스트인 "34/"를 〈polls.urls〉 URLconf로 전달하여 남은 처리를 진행합니다. 거기에 '<int:question_id>/'와 일치하여, 결과적으로 detail() 뷰 함수가 호출됩니다.

* 뷰가 실제로 무엇인가 하게 만들기

* 템플릿을 생성하자.

> Within the templates directory you have just created, create another directory called polls, and within that create a file called index.html. In other words, your template should be at polls/templates/polls/index.html. Because of how the app_directories template loader works as described above, you can refer to this template within Django as polls/index.html.

템플릿 안에 polls 폴더를 만들고 거기 안에 다시 html을 만들어야함 (안바뀌었네 여직)

index에서는 그냥 list 그 자체를 받은 후에, 그걸 templates에다가 넘기면 템플릿에서 loop를 돌면서 li를 생성하는 방식으로 진행됨

> 지름길: render()
템플릿에 context 를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문은 자주 쓰는 용법입니다. 따라서 Django는 이런 표현을 쉽게 표현할 수 있도록 단축 기능(shortcuts)을 제공합니다. index() 뷰를 단축 기능으로 작성하면 다음과 같습니다.

>지름길: get_object_or_404()
만약 객체가 존재하지 않을 때 get() 을 사용하여 Http404 예외를 발생시키는것은 자주 쓰이는 용법입니다. Django에서 이 기능에 대한 단축 기능을 제공합니다. detail() 뷰를 단축 기능으로 작성하면 다음과 같습니다.

1. 꼭 굳이 이 템플릿을 써야하나 ???
2. 템플릿에서 하드코딩된 url 제거하기 이부분

## 중요한 방향성.
프론트엔드단의 html 파일을 생성하는 것에 대해서
vue.js를 추가할 것인가.
jquery + js로만 해도 될것인가??

* 여기서의 방식은 php의 방식과 비슷한것 (구식이라는 거지)
* 미래를 위해선 DRF + vue 등의 선택이 합리적이라고 생각된다는거

닭 잡는데 소 잡는 칼을 쓰지 말자는 격언을 되뇌이자.


## TO Do
* 튜토리얼 복습하면서 짧은 게시판 하나 만들기.

