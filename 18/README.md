# 18. DB 정보 접근 및 장고 템플릿 내 for loop

## 목표
- db에 접근하여 모든 데이터를 display할 예정
- HelloWorld.objects.all() 전체 데이터를 긁어올 수 있음
- HttpResposeRedirect(reverse)를 통해서 새로고침을 할때마다 POST가 호출되어서 데이터가 반복되는 현상을 막음
![](https://github.com/KangminNa/Django_Pinterest/blob/main/18/1.png?raw=true)
현재 화면
- 텍스트 박스에 글을 작성하고 POST를 누르면 DB에 저장하고 그 이후 값을 밑에 출력하게 만듬.
- for loop를 이용함.
