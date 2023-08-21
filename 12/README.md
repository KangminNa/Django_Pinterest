# 12. CSS 핵심 - display 속성 및 Size 단위 px, em, rem, %

## 개념 공부
- CSS란?
- Cascading Style Sheet
- HTML을 꾸미긴 위한 디자인 언어 묶음
- ESSENTIALS
- DISPLAY attribute
- 디스플레이 설정들이 화면을 구성하는 부분을 어떤 원리로 돌아가는지를 디자인을 할 수 있기 때문에 속성을 배울거임!

## Display Attribute
- block
![](https://github.com/KangminNa/Django_Pinterest/blob/main12/1.png?raw=true)
- inline
![](https://github.com/KangminNa/Django_Pinterest/blob/main12/2.png?raw=true)
- inline-block
![](https://github.com/KangminNa/Django_Pinterest/blob/main12/3.png?raw=true)
- None : 그냥 없어요. 있긴 있는데 없어요

## Visibility Attribute
- Hidden
![](https://github.com/KangminNa/Django_Pinterest/blob/main12/4.png?raw=true)
- 보이지만 않을 뿐 그냥 투명하게 됨. 자리를 차지함, None과는 반대임. 그냥 없음.

## SIZE Attribute
- Resonsive
    - 우리는 반응형으로 만들어야함
    - 크기가 어떻게 변하는지 알아야 통제력을 가져야 함
    - 반응형 때문에 Size를 공부함.
- px
    - 자기 갈길 가는 친구.
    - 부모가 어떻게 되든 무조건 100px을 가짐
    - Parent의 폰트 사이즈가 커지든 작든 상관 없음

- em
    - 부모와 함께 사이즈가 커짐
    - child도 사이즈가 Parent로 따라감
    - 부모가 작아져도 child도 작아짐
    - em을 잘 안사용하는 이유는
    - 부모가 여러개일때 문제가 생김
    - 여러가지 부모가 있으면 2배씩 부모가 커지면 맨 안에 있는 child 4배로 늘어남. 부모마다 거치는 크기만큼 맨 마지막 child는 모두 곱한 값으로 늘어나게 됨.

- rem : 이게 최고! 이유는?
    - root-html은 기본적으로 적용되어 있는 16px 고정되어 있음
    - 이 값을 기본으로 적용
    - 만약 24xp 커진다면 똑같이 비율로 커지게 됨

- %
    - 이 친구도 rem과 마찬가지임
    - 그래서 우리는 rem과 %를 사용할거임!

- 정리
![](https://github.com/KangminNa/Django_Pinterest/blob/main12/5.png?raw=true)
