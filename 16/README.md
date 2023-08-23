# 16. GET, POST 프로토콜 실습

## 실습 내용 
- Post를 보낼 땐  {% csrf_token %} 항상 이 구문을 선언해야함.
- token은 장고에서 제공하는 보안 기능 중 하나
- 항상 적어야 post가 작동함.
- 이제 정상적으로 돌아감.
- accountapp/view.py에서 get과 post를 정의 한 이후 text를 html에서 전송한다면!
-![](https://github.com/KangminNa/Django_Pinterest/blob/main/16/1.png?raw=true)
이런 화면이 만들어짐 