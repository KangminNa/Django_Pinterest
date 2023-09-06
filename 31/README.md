# 31. Profileapp 구현시작

## 실습내용
- ProfileApp 생성했기 때문에
- 마이그레이션 하기
- 이후 view에서 class 작성하기
- urls.py에서 view path 설정
- 템플릿 만듬! -> accountapp/templates/create.html을 복사한 이후에 글만 수정
- 이후 detail.html에서 target_user의 user id를 얻기 위해 -> 왜냐하면 model에서는 user를 가져오지 않았음
- view -> 서버단에서 user 로직을 처리함.

## 현재까지 페이지 모습
![](https://github.com/KangminNa/Django_Pinterest/blob/main/31/1.png?raw=true)
- 성공하면 profiles/create에서 작성한 닉네임이 보이게 됨
- 실습에서 TEST_NICKNAME으로 했기에 이렇게 나옴