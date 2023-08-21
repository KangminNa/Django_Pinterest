# 11. Static 설정 및 CSS 파일 분리

## 실습
- CSS파일이란? 10 에서 적용한 style를 통해 속성값을 따로 정의했는데 보통은 HTML은 뼈대만 두고 디자인 요소는 css파일로 나눠서 관리하는게 보통의 개발패턴
- 분리 이전에 static에 대한 설정
- static : 정적 -> css, js, assets, file 바뀌지 않는 친구들을 따로 관리하기 위해 설정을 해야함.
- static 관련 설정에 대한 실습 우선!
- python manage.py collectstatic -> 모든 static 파일을 모아주는 명령어
- STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 모이는 곳에 대한 곳을 정의
- django documentation - Managing static files 를 참고하여 디렉터리를 따로 지정할 수 있음.
- 앱 내부에 static 파일을 기본적으로 찾는데, 앱의 종속적이지 않은 static 파일을 생성할 수 있음

## 개발자 도구 확인
![](https://github.com/KangminNa/Django_Pinterest/blob/main/11/1.png?raw=true)

## 현재까지 진행사항
![](https://github.com/KangminNa/Django_Pinterest/blob/main11/2.png?raw=true)