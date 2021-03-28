
# 장고걸스 블로그 만들기 튜토리얼
https://tutorial.djangogirls.org/ko/django_installation/



--- 


## 장고 모델 
https://tutorial.djangogirls.org/ko/django_models/


```
Post(게시글)
--------
title(제목)
text(내용)
author(글쓴이)
created_date(작성일)
published_date(게시일)
```


* 출석 체크 모델
```
Work(출석)
-------
person(출근자)
created_time(생성일)
on(출근)
off(퇴근)
work_tiem(일한시간)
```

> 대신 모델의 필드와 정의하는 방법에 궁금하다면 장고 공식 문서를 꼭 읽어보길 바랍니다.
https://docs.djangoproject.com/ko/3.0/ref/models/fields/#field-types


```
python manage.py makemigrations blog
python manage.py migrate blog
```

> **장고 폼**
한 가지만 더 하면 웹사이트가 완성됩니다. 바로 블로그 글을 추가하거나 수정하는 멋진 기능을 추가하는 것이죠. 장고의 관리자 기능도 충분히 멋있기는 하지만, 좀 더 입맛에 맞게 바꾸고 예쁘게 꾸미기에는 좀 한계가 있습니다. 폼(양식, forms)으로 강력한 인터페이스를 만들 수 있어요. - 우리가 상상할 수 있는 거의 모든 것을 할 수 있거든요!

