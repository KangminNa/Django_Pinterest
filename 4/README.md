# 4. django 개발패턴

## MVC? MVT?
- Model, View, Template(Controller)
- 말이 다를뿐 역할은 같다.

## Model
- django 와 database의 상호작용을 담당
- 객체를 데이터베이스에 저장하는 과정에서 편리하기 담당하는 친구
- 굳이 db쪽 언어를 사용하지 않아도 간단하게 수정하고 삭제 등등 여러 기능들을 담당
- 예를 들어서 데이터 베이스는 Row, Columns, Item, Atrriutres
- 게시글을 예시로 article 하나 있다면 title, article, image가 있다면 columns로 데이터 베이스에 들어가는걸 담당해줍니다.
- 모델만 설정만 해주면 crud는 장고에서 쉽게 건들 수 있음

## view
- 장고의 계산하는 부분을 담당
- 유저와 서버의 요청 관계에서 사용
- 유저는 서버에 요청을 하면 서버는 응답을 하기위한 절차들을 함.
- 그 과정에서 check if authenticated
- check request valid
- collect data from db
- render response
- 위 4가지 과정을 서버에서 하는 처리를 뷰에서 담당

## template
- 유저가 User Interface를 봄
- UI 안에 있는 생성에 대한 해결책
- 유저가 한 게시글에 대한 내용을 보고 싶음'
- 서버에 요청
- 위에 작성한 기능을 서버가 처리
- 중간에 HTML 내부에서 게시글을 구현해줄 만들어줄 작업을 처리해주는 template
- 새로운 내용을 자체적으로 생산할 수 없으니 템플릿을 이용해서 보여줌
```
<title>{{Article.title}}</title>
이런식으로 사용 가능

<body>
    {%for article in article_list%}
        <p>{{article.title}}</p>
    {%endfor%}
</body>
여러개의 요청을 이렇게 처리


<body>
    {% if article %}
        <p>Article exists!</p>
    {% endif %}
</body>
조건문도 있음
```

## 정리
![](https://github.com/KangminNa/Django_Pinterest/blob/main/4/1.png?raw=true)
