""" 이진 탐색 """

''' 순차 탐색 '''
def sequential_search(n, target, array) :
    for i in range(n):
        if array[i] == target:
            return i+1
        
data = input('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력').split()

n=int(data[0])
target=data[1]

array=input(f'{n}개만큼 문자열 입력. 구분은 띄어쓰기').split()

print(sequential_search(n, target, array))



''' 이진 탐색 '''
# 재귀함수로 구현
def binary_search(array, target, start, end):
    if start>end:
        return None
    
    mid = (start+end)//2
    
    if array[mid] == target :
        return mid
    
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)
    
    else :
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input('n, target 입력').split()))    

array= list(map(int, input(f'{n}개 원소 입력').split()))

result = binary_search(array, target, 0, n-1)
        
if result == None :
    print('원소 존재 X')
else :
    print(result+1)
    


# 반복문으로 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
    
        if array[mid] == target :
            return mid
        elif array[mid] > target :
            end = mid -1
        else :
            start = mid +1
    
    return None

n, target = map(int, input('n, target 입력').split())

array= list(map(int, input(f'{n}개 원소 입력').split()))

result = binary_search(array, target, 0, n-1)
        
if result == None :
    print('원소 존재 X')
else :
    print(result+1)


### 빠르게 입력
import sys

data = sys.stdin.readline().rstrip()



''' 부품 찾기 '''
# 이진 탐색

def binary_search(array, target, start, end):
    while start <= end: # 인덱스
        mid = (start+end) // 2
    
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        end = mid -1
    else :
        start = mid +1
    
    return None

n = int(input('부품 개수'))

array= list(map(int, input('부품 번호').split()))
array.sort()

m = int(input('확인 요청 부품 개수'))
x = list(map(int, input('확인 요청 부품 번호').split()))

for i in x:
    result = binary_search(array, i, 0, n-1)

    if result != None:
        print('yes', end=' ')
    else :
        print('no', end=' ')
        


# 계수 행렬 이용
n = int(input())
array = [0]*1000000

for i in input().split():
    array[int(i)] =1

m = int(input())

x= list(map(int, input()))

while i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else :
        print('no', end=' ')



# set()
n = int(input('부품 개수'))
array= set(map(int, input('부품 번호').split()))

m = int(input('확인 요청 부품 개수'))
x = list(map(int, input('확인 요청 부품 번호').split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else :
        print('no', end=' ')



# 떡볶이 떡 자르기
n, m = list(map(int, input('n,m을 입력').split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end :
    total = 0
    mid = (start+end) //2
    
    for x in array:
        if x >= mid:
            total += x-mid
        
    if total < m:
        end = mid-1
    else :
        result = mid
        start = mid+1
        
print(result)

































