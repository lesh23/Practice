""" 다이나믹 프로그래밍 """

# 피보나치 수열 : 재귀함수로 구현(x가 커지면 연산이 비약적으로 증가)
def fibo(x) :
    if x==1 or x==2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))


# 메모이제이션 기법을 사용한 피보나치 수열
d = [0] * 100

def fino(x):
    if x==1 or x==2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

# 피보나치 수열 : 바텀업
d = [0]*100

d[1]=1
d[2]=1
n=99

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])



''' 1로 만들기 '''
x= int(input('x 입력'))

d = [0]+30001

for i in range(2, x+1):
    d[i] = d[i-1] +1
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] +1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] +1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] +1)

print(d[x])



''' 식량 털기 '''
n = int(input('식량창고 개수'))

array = list(map(int, input('식량 저장량').split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(d[0], array[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+array[i])
    
print(d[n-1])



''' 바닥 공사 '''
n = int(input('가로의 길이'))

d=[0]*1001

d[1] =1
d[2]=3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2])
    
print(d[n]%796796)



''' 효율적인 화폐 구성 '''
n,m = map(int, input().split())

array = []

for i in range(n):
    array.append(int(input()))
    
d = [10001] * (m+1)

d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])




































