# Python 1일차

## 숫자형
```python
a = 1 # int 형으로 생성됨
a = 1.0 # float형으로 생성됨
```
* python은 정수형을 미리 정의해주지 않아도 값을보고 자동적으로 정수형을 설정해준다.
```python
a=1
b=1.0
if(a==b):
    print("둘이 같아요요") # 출력 잘됨
if(a is b):
    print("둘이 같아영") # 출력 안됨
```
* is는 단순히 값만을 비교하는 것이 아닌 형까지 비교를 해주기에 2번째 if문은 출력이 되지 않는다.
* if문은 나중에 자세히 다룬다.

## 자료형
### 문자열 자료형
```python
a='python'
b="python2"
```
* python은 문자열도 정의해주지 않고 ''와 ""로 정의를 해줄 수 있다.
* ''를 통해서 만들어주면 다음에는 ''로 만들어 줄 수 없다.
```python
 mutiline= '''
 hello,wolrd!
 i'm python
 have a nice day~!
 '''
```
* 만약 여러개의 문장을 넣고싶을때에는 '''나 """를 사용하여 문장을 넣어주면 된다.

### 문자열의 연산
* 문자열의 연산은 간단하다!
```python
a='hello!'
a = a * 2
print(a)
>>> hello!hello!
```
* 만약 문자열을 2번 print하고 싶을시에는 간단하게 *2를 해주면 print가 된다.

```python
a='hello'
b="world!"
print(a+b)
>>>helloworld!
```
* 문자열들끼리 더해주게 되면 helloworld!라는 결과를 출력할 수 있다.