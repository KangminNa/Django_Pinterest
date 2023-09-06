# 36. ListView, Pagination 소개 및 적용

## 수업내용
- CRUD에 해당하는 app을 만듬
- article, account, profile app에다가 적용함
- account는 단일 개체만 확인하면 됐음.
- 게시판은 multiple object를 다룰 수 있는 객체가 필요함
- List view 로 해결하면 됨!
- 중요한 파라미터만 정해주면 됨
- + pageination도 해야함
![](https://github.com/KangminNa/Django_Pinterest/blob/main/36/1.png?raw=true)
- 리스트 뷰 코드의 형태

- Pagination은?
- Generate Page of Objects
- 페이지에 객체를 생성하는 것
- ex: Google에서 검색한 이후에 하단에 번호가 붙어져 있는 것을 Paination임
- 무한 스크롤 생성

## 현재화면
![](https://github.com/KangminNa/Django_Pinterest/blob/main/36/2.png?raw=true)