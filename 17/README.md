# 17. POST 통신을 이용한 DB 데이터 저장 실습

## DB에 데이터 저장 실습
- hello_world.html에서 화면 구성
- accountapp/models.py에 구성한 hello_world() model 사용
- accountapp/views.py에서 temp에 Post.get에 input=name작성
- new_hello_world = HelloWorld()구문을 통해 model 불러오기
- new_hello_world.save()를 통해 database에 저장
- 현재 화면
![](https://github.com/KangminNa/Django_Pinterest/blob/main/17/1.png?raw=true)