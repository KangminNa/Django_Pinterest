# 32. profileapp 마무리

## 실습내용 
- Profileapp에서 UpdateView 생성
- accountapp에서 updateview를 가져와서 일부 수정
- 그다음 urls.py에서 updateview.as_view() 설정 pk를 가져와야함
- 그리고 제일 중요함!!! 이미지가 보이지 않았기 떄문에 urls 설정을 해야하는데 
- media 설정은 static(conf), settings(conf)를 통해서 설정할 수 있음.
- settings에서 우리가 정의했던 media_url과 root를 설정해줌
- 그러면 이미지가 보이가 detail.html에서 프로필이 보이게 설정하면 끝!

## 현재 화면
![](https://github.com/KangminNa/Django_Pinterest/blob/main/32/1.png?raw=true)
