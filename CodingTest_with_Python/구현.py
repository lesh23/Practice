""" 구현 """

''' 상하좌우 '''
n = int(input('크기를 입력하세요.'))
x, y=1,1
plans = input('계획을 입력하세요.').split()

dx = (0,0,-1,1)
dy = (-1,1,0,0)
move = ('L','R','U','D')

for plan in plans :
    for i in range(len(move)):
        if plan == move[i]:
            nx = x+dx[i]
            ny = y+dy[i]
        
    if nx<1 or ny <1 or nx > n or ny>y :
        continue
        
    x, y = nx, ny

print(x,y)



''' 시각 '''
h = int(input('시간을 입력하세요.'))

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
                
print(count)



''' 왕실의 나이트 '''
### 풀이1)
# 먼저 입력 받아서 숫자로 변환
lo = list(map(str, input('위치를 입력하세요')))

en=('a','b', 'c', 'd', 'e', 'f', 'g', 'h')
x = int(lo[1])
y=1

for i in range(len(en)):
    if lo[0] == en[i] :
        y = i+1
        
dx=(-2,-2,2,2,-1,1,-1,1)
dy=(-1,1,-1,1,-2,-2,2,2)
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx<1 or nx>8 or ny<1 or ny>8:
        continue 
    
    count += 1
        
print(count)    



### 풀이2)
input_lo = input('위치를 입력하세요.')

row = int(input_lo[1])
col = int(ord(input_lo[0])-ord('a'))+1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1),(1,2),(-1,2), (-2,1)]

result=0
for step in steps:
    nrow = row+step[0]
    ncol = col+step[1]

    if nrow >=1 and nrow <=8 and ncol >=1 and ncol <=8:
        result +=1

print(result)


















































