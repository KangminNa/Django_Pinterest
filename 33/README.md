# 33. get_success_url 함수 그리고 리팩토링

## 수업내용
- 저번시간에 만들었던 profileapp을 리팩토링 시간
- 프로필을 edit하고 다시 profile 화면을 보여줘야함
- 문제는 int:pk를 받고 있는 detail에서 꼭 pk를 보내줘야 하는 상황이 발생
- 이를 위해 get_success_url 함수를 만들어서 pk 인자를 보냄
