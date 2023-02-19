""" 정렬 """

''' 선택 정렬 '''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index=j
    array[i],array[min_index] = array[min_index], array[i]

print(array)



''' 삽입 정렬 '''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]< array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else :
            break
print(array)
            


''' 퀵 정렬 '''
## 큌 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end :
        return
    pivot = start
    left = start + 1
    right = end
    
    while left <= right :
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[right] = array[right], array[left]
            
        
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)



## 파이선 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array) :
    if len(array) <=1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))



''' 계수 정렬 '''
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1
    
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')



''' 정렬 라이브러리 '''
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 방법1
result = sorted(array)

array.sort()
print(array)

array = [('바나나',2), ('사과',5), ('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)




''' 위에서 아래로 '''
array=[]

a= int(input('수열의 개수를 입력하세요'))

for i in range(a):
    array.append(int(input(f'{i+1}번째 원소를 입력하세요')))

array.sort(reverse=True)
print(array)
    


''' 성적이 낮은 순서로 학생 출력 '''
a = int(input('학생 수 입력'))

array=[]
for i in range(a):
    data = input('학생이름과 점수').split()
    array.append((data[0], int(data[1])))

array[1]

def setting(data):
    return data[1]

result = sorted(array, key=setting)

for st in result:
    print(st[0], end= ' ')



''' 두 배열의 원소 교체 '''
n,k = map(int, input('n과 k 입력').split())

a = list(map(int, input(f'{n}개의 배열 A 입력').split()))
b = list(map(int, input(f'{n}개의 배열 B 입력').split()))

a= sorted(a)
b= sorted(b, reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
        
print(sum(a))
    










