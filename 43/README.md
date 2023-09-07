# 43. Field Lookup을 사용한 구독 페이지 구현

## 학습내용
- about Filter
- Model.objects.filter(pk=xxx, user=xxx) 
- 모델 안에 객체르 접근하고 filter
- (pk=xxx, user=xxx)
- 이 값들은 AND Function임
- What about Where statement in SQL?
- 구독 앱을 만들어야 하는데
1. Find User subscripted Projects
2. Find articles in projects
- 이 두가지를 나눠서 구현할 예정
- Articles.objects.filter(pk=xxx, user=xxx)
- Articles.objects.filter(project__in=projects) -> 이제 이렇게
- 이것이 FieldLookup
- 이 구문이 SELECT ... WHERE project IN(...);


## 현재 모습
- ![](https://github.com/KangminNa/Django_Pinterest/blob/main/43/1.png?raw=true)
- ![](https://github.com/KangminNa/Django_Pinterest/blob/main/43/2.png?raw=true)
- 구독한 프로젝트에 대한 article을 보여줌!