""" 그리디 """

'''큰 수의 법칙'''
### 풀이1)
# N,M,K 공백으로 구분해서 입력
n, m, k = map(int, input('n,m,k를 입력하시오.').split())
# N개의 수 공백으로 구분해서 입력
data = list(map(int, input(f'{n}개의 자연수를 입력하시오.').split()))

data.sort()
first = data[n-1]
second = data[n-2]

result=0

while True :
    for i in range(k):
        if m==0:
            break
        result += first
        m -= 1
    if m==0:
        break
    result += second
    m -= 1
    
print(result)



### 풀이2)
# N,M,K 공백으로 구분해서 입력
n, m, k = map(int, input('n,m,k를 입력하시오.').split())
# N개의 수 공백으로 구분해서 입력
data = list(map(int, input(f'{n}개의 자연수를 입력하시오.').split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = (m//(k+1)) *k
count += m%(k+1)

result=0
result += count * first
result += (m-count) * second

print(result)



''' 숫자 카드 게임 '''
### 풀이1)
n,m = map(int, input('n, m을 입력하세요.').split())

result = 0

for i in range(n) :
    data = list(map(int, input(f'{i+1}행을 입력하세요.').split()))
    min_value = min(data)
    result = max(result, min_value)
    
print(result)



### 풀이2)
n,m = map(int, input('n, m을 입력하세요.').split())

min_value = 0

for i in range(n):
    a = list(map(int, input(f'{i+1}행을 입력하세요.').split()))
    mmin = 10001
    for j in a :
        mmin = min(j, mmin)
    
    min_value = max(mmin,min_value)
    
print(min_value)        



''' 1로 만들기 '''
### 풀이1)
n,k = map(int, input('n, k 입력하세요.').split())
result = 0

while n>=k:
    if n % k != 0:
        result += (n%k)
        n -= n%k
    else : 
        n //= k
        result += 1

while n>1 :
        result += (n%k)-1
        n -= (n%k)-1
        
print(result)



### 풀이2)
n,k = map(int, input('n, k 입력하세요.').split())
result = 0

while n>=k:
    while n%k !=0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n>1:
    n -=1
    result +=1

print(result)
    
    
















































