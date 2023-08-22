# 14. Model, DB 연동 - makemigrations, migrate

## model
- django <=> database 연동시켜주는 작업
- 장고에서 모델을 가지고 데이터베이스와 연동을 하면서
- 디비에 대한 자세한 내용을 알지 않아도 컨트롤 가능
- row <=> attribute

python manage.py makemigrations
- model에다가 연동된 데이터베이스를 파일로 만들어주는 명령어

python manage.py migrate
- 마이그레이션을 한 이후에 연동을 위한 명령어
- 이러면 db랑 연동이 된겁니다.
- 너무 편하다.

DB 관련 정보
- setting.py 안에 DATABASES={'안에 정보가 들어 있음'}
- 현재는 db.sqlite3 기본이고 현재 연동됨
- 현재는 이걸로 진행하지만 배포할떄는 바꿀거임


## 이런 오류가 발생!!
- 명령어 입력 : python manage.py makemigrations
- 이후 오류 내용 : No changes detected
- setting.py에서 INSTALLED_APPS=['프로젝트이름'] 을 작성
- 그리고 ./manage.py makemigrations '프로젝트이름'을 명령어를 쳐주면 됨!
- migration을 초기에 되지 않았다면 init해주는 상황이 필요함.
- 변경사항이 감지되지 않거나, 누락으로 인해 마이그레이션이 안될 수도 있어서 일어나는 상황. 마이그레이션은 항상 한번에 되는 꼴을 못봄.

