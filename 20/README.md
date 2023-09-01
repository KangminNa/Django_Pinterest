# 20강 - Class Based View, 장고의 CRUD

## 수업내용
1. 현재까지 우리가 한 내용들 이론 정리
2. 프로젝트 구조와 작동 원리에 대한 내용
3. 인증에 대한 설명

## 정리
- HelloWorld Function을 만듬.
![](https://github.com/KangminNa/Django_Pinterest/blob/main/20/1.png?raw=true)
- 인증 시스템을 구축해야함.
- 계정이 필요함
- 지금은 누구나 접근 할 수 있기 때문에!

- 현재 우리는 Account App을 만드는게 목적
- 이를 위해서 총 4가지를 만들어야 함
- Siup UP,login,  View Info, Change Info, Quit
- 회원 가입과 로그인 등 Account App이라면 가져가야 하는 기능들

## 장고에서 CRUD란?
- CRUD이란?
- C : Create, R : Read, U : Update, D : Delete
- CRUD를 쉽게 할 수 있는 클래스들을 제공함
- CRUD view : Class Based View <-> Function Based View
- 함수기반의 view
- Class Based View를 모르는 상태로는 가독성이 떨어지는 코드가 생길 수 밖에 없음
![](https://github.com/KangminNa/Django_Pinterest/blob/main/20/2.png?raw=true)
- 이렇게 쉽게 할 수 있음(대박)
- 장고에서 CRUD가 대박인 이유는 이미지에서 끝
- 거의 대부분은 CRUD 사이클에 기능들이 들어가기 때문에 꼭 짚고 넘어가기
![](https://github.com/KangminNa/Django_Pinterest/blob/main/20/3.png?raw=true)
