# 8. 장고 Template extends include 구문, render

## 깃
- gitignore 수정
- 불필요한 cache 추적 취소에 대한 내용

## 장고 템플릿
- 자주쓰이는 문법
- extends / include
- extends : pre-made, Template, html
- html 처럼 구조를 가져와서 사용
- include : 어디선가 가져와서 붙이는
![](https://github.com/KangminNa/Django_Pinterest/blob/main/8/1.png?raw=true)
- 이런 차이
- extends, include에 대한 실습

## 템플릿 생성
- 폴더 생성
- 이후 base.html 생성
- accountapp/views.py에서 return값 변경(render)
![](https://github.com/KangminNa/Django_Pinterest/blob/main/8/2.png?raw=true)
- 이 이미지의 문제를 해결하기 위해서는
- setting.py에서 꼭 TEMPLATES=[os.path.join 작성해주기.]
![](https://github.com/KangminNa/Django_Pinterest/blob/main/8/3.png?raw=true)
