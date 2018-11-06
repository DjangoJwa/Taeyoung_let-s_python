# 거북이로 그림그리기 첫번째
# import turtle as t
# angle=89
# t.color("blue")
# t.shape("turtle")
# t.speed(0)
# t.begin_fill()
# for x in range(500):
#     t.forward(x)
#     t.left(angle)
# t.mainloop()

# 20초 시간 맞추기 게임
# import time
# input("시간세기 시작! 엔터를 누르면 20초를 셉니다.")
# start=time.time()
# input("10초 뒤에 시간을 셉니다.")
# end=time.time()
# et=end-start
# print(et)

# 거북이로 그림그리기 두번째
# import turtle as t
# import random
# t.shape("turtle")
# t.speed(0)
# for x in range(500):
#     a=random.randint(1,5000)
#     t.setheading(a)
#     t.forward(10)

# 더하기 함수
# def plus(a,b):
#     return a+b
# a=int(input())
# b=int(input())
# print(plus(a,b))

# 팩토리얼 함수
# def factorial(n):
#     fact=1
#     for x in range(1,n+1):
#         fact=fact*x
#     return fact
# a=int(input("팩토리얼할 숫자 입력해주세요"))
# print(factorial(a))

# 거북이로 함수 그리기 마지막
# import turtle as t
# t.bgcolor("black")
# t.speed(0)
# t.shape("turtle")
# for x in range(200):
#     if x%3==0:
#         t.color("red")
#     if x%3==1 :
#         t.color("yellow")
#     if x%3==2:
#         t.color("blue")
#     t.forward(x*2)
#     t.left(119)
# t.mainloop()

# 타자치기 게임
# import time
# w="""
# 동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세
# 무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세
# """
# start=time.time()
# x=input()
# if w==x:
#     print("통과!")
# else:
#     print("오타 다시도전")
# end=time.time()
# et=end-start
# et=format(et,"2f")