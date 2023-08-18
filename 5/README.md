# 5. 첫 앱 시작, 그리고 기본적인 view 만들기

## 실습
1. 터미널 실행
2. python manage.py startapp accountapp
3. pragmatic/setting 들어가서 INSTALLED_APPS = ['accountapp] 설정하기
4. accountapp/view.py에서 실습 시작

## 코드
1. pragmatic/urls.py 에서 path를 통해 accountapp/view.py에서 사용할 url를 설정해준다.
2. accountapp/view.py에서 HttpResponse를 이용하여 "Hello World"라고 출력되는 view를 구성한다.
3. accountapp/urls.py를 하나 만들고 여기에 view.py가 이용할 url에 대한 설정을 제공 
4. http://127.0.0.1:8000/account/hello_world/ 해당 url로 넘어가면 view에서 작성한 화면이 보임
![](https://github.com/KangminNa/Django_Pinterest/blob/main/5/1.png?raw=true)