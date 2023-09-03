# 25. UpdateView를 이용한 비밀번호 변경 구현

## 수업내용
![](https://github.com/KangminNa/Django_Pinterest/blob/main/25/1.png?raw=true)
- 현재까지 21~24까지 구현된 부분
- 25강에서 Change info -> UpdateView로 구현하는 과정

## 실습
![](https://github.com/KangminNa/Django_Pinterest/blob/main/25/2.png?raw=true)
- Mypage를 들어왔을 때 비밀번호를 바꾸는 기능 구현
- 그런데 아이디도 같이 바뀌는 경우가 있기에 이를 막기 위한 실습
![](https://github.com/KangminNa/Django_Pinterest/blob/main/25/3.png?raw=true)
- 개발자 도구로 웹으로 접근 한 이후에 값을 넣을 수 있는 상황도 만들어짐
- 그렇기 때문에 forms.py를 만들어서 서버에 직접적인 영향을 미치지 않게 적용함