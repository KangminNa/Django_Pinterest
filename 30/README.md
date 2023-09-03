# 30. Profileapp 시작 그리고 ModelForm

## 수업내용
- account app 이후에 profileapp 만들기
- 지금 detail page를 보면 superuser로 되어 있음
- 아이디가 노출되어 있음
- 해킹에 매우 취약한 상태
- 닉네임으로 바꾸는 과정
- 만들고자 하는 사이트에 닉네임과 프로필 사진이 있음.(한줄소개)
- 프로필 앱을 따로 만들 예정
- Profile : Account <-> 1 : 1 하나의 계정에 하나의 프로필을 만들 예정
- Profile Image, Nickname, Message
- Delete View, Detail View는 만들지 않을 예정
- $ python3 manage.py startapp profileapp 이 명령어로 app 생성

## Form
![](https://github.com/KangminNa/Django_Pinterest/blob/main/30/1.png?raw=true)
- Profile Form은 어떻게 만들까?
- 작성한 Model을 바탕으로 Form을 만들어야할 거 같은데
- Model Form을 활용하면 저절로 해준다!
![](https://github.com/KangminNa/Django_Pinterest/blob/main/30/2.png?raw=true)
- 이게 정말 미쳤다. 장고는 미쳤다
- 개발자경험이 정말 미쳤다,,, 대학생이라면 무조건 장고를 배워야할거같다.
