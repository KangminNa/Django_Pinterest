# 29. superuser, media 관련 설정

## 수업내용
- 실습 X
- 프로파일 앱을 만들기 이전에 사전에 세팅할 부분들 공부
- superuser, media 관련 설정
- 기본적으로 /admin 으로 들어가서 관련설정을 만질 수 있음
- $ python3 manage.py createsuperuser 명령어를 통해 admin 아이디 및 비밀번호 설정
- $ python manage.py runserver 실행
- /admin으로 들어가서 설정한 아이디와 비밀번호 설정
- port가 이미 먹혀서 안되는 경우라면
- $ lsof -i:8000 사용하고자 하는 포트를 입력
- $ kill -9 PID 명령어를 침
- 나같은 경우에는 PID가 5개의 숫자로 이루어진 하나의 프로세스를 PID부분에 입력하니 사라짐
- 이후에 다시 하면 admin 접속이 가능
- admin 계정을 제외하고 다 제거
- 이후 media 관련 설정
- $ pip install pillow -> 이미지 관리 라이브러리 설치 명령어


