# 한줄 문자열
# s = ''
# str1 = 'Hello World'
# str2 = "Hello World"
# print(type(s), type(str1), type(str2)
# #print(isinstance(str1,str2))


# 여러 줄 문자열
# str3 = ''' ABC
# DEF
# 가나다라마바사
# 아자차카타파하 '''
# print(str3)

# 여러줄 주석 -> 여러 줄 문자열
#
# '''
# 주석1
# 주석2
# 주석3
# '''

# # escape
# print('hello\nworld\n')
# print("hello \"world\"")
# print("She\'s Mom')
# # print("둘리\010-0000-0000")
#
# print('======= 문자열 연산 ========')
#  s1 = 'First String'
# s2 = 'Second String'
# #
# #반복
# s3 = s1*3
# print(s3)
#
# # + ( 연결. concatenate)
# tpemp = ''
# s4 = s1 + temp = s2
# print(s4)
#
# # 인덱싱(sequence 타입이 가지는 특징)
#  print(s1[0], s1[1], s1[2])
# print(s1[-12], s1[-11], s1[-10])
# # #slicing(sequence 차입이 가지는 특징)
# s7 = s1[2:5]
# print(s7)
# print(s1[2:1])
#
# # 문자열 객체와 정수 객체는 연결(+) 연산을 할 수 없다.
# #print("hello" +2)
#
# print("hello" +str(2))

print('======= 포맷팅 ========')
# tuple
f = "name: %s, age:%d"
print(f % ('둘리',10))

# format() 함수
name = '마이콜'
age = 30
print("name: " + format(name, 's')+", age: "+format(age,'d'))

print('======= 객체 함수 ========')
s8 = 'i like python'
print(s8.upper())
print(s8.lower())
print(s8.swapcase())
print(s8.capitalize())
print(s8.title())


s9 = 'I Like Python, I Like Java Also'
print(s9.count('Like'))
print(s9.find('Like'))
print(s9.find('Like',5))
print(s9.find('JavaScript'))
print(s9.find('Like'))

# str 객체는 변경할 수 없다(불변성, immutable)
# s10 = 'hello'
# s10[0] = 'f'
# print(s10)

# cf list는 변경 가능하다.(mutable)
l1 = ['hello', 'world']
print(l1)
l1[0] = 'HELLO'
print(l1)
l1.append('Python')
print(l1)


