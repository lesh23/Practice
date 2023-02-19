""" 최단 경로 """
## 다익스트라 최단 경로, 플로이드 워셜 알고리즘이 대표적 해결책

## 방법 1) 다익스트라 직관적 코드
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input('n, m 입력').split())
# 시작 노드 번호 입력
start = int(input('시작 노드 번호'))
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문 여부 리스트
visited = [False]*(n+1)
# 최단 거리 테이블 초기화
distance = [INF] * (n+1)


# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input('a번 노드에서 b번 노드로 가는 비용이 c').split())
    graph[a].append((b,c))
    
# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start]= True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now] :
            cost = distance[now] + j[1]
            
            if cost<distance[[j[0]]]:
                distance[j[0]] = cost
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF :
        print('INFINITY')
    else :
        print(distance[i])
            
    


## 방법 2) 다익스트라 개선된 코드
import heapq
import sys
input = sys.stdin.readline()
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력받기
n ,m = map(int, input('노드의 개수와 간선의 개수를 입력').split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])



''' 플로이드 워셜 알고리즘 '''
INF = int(1e9)

n = int(input('노드 개수').split())
m = int(input('간선 개수').split())

# 2차원 리스트 만들고 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] =0
        
# 각 간선에 대한 정보 입력
for _ in range(m):
    a,b,c = map(int, input('a에서 b로 가는 비용은 c').split())
    graph[a][b]=c
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print('INFINITH', end=' ')
        else : 
            print(graph[a][b], end=' ')

print()



''' 미래 도시 '''
INF = int(1e9)

n ,m = map(int, input('노드의 개수와 간선의 개수를 입력').split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] =0
            
for _ in range(m):
    a, b = map(int, input('a에서 b로 가는 간선 존재').split())
    graph[a][b], graph[b][a] = 1, 1

x, k = map(int, input('최종목적지(x), 소개팅 회사(k)').split())

for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k])
    
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else : 
    print(distance)    
    


''' 전보 '''
# 풀이 1) 플로이드 이용
INF = int(1e9)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

start=int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i ==j:
            graph[i][j]=0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b]=c

for k in range(1, n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1,n+1):
    if graph[start][i] == INF or graph[start][i]==0:
        pass
    else : 
        print(graph[start][i], end=' ')



# 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distnace = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dij(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q: #q가 비어있지 않다면
        dist, nod = heapq.heappop(q)
        if distance[nod] < dist :
            continue
        for i in graph[nod]:
            cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q,(cost, i[0]))
    
dij(start)

count=0

max_distance = 0
for d in distance :
    if d!=INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1,max_distance)

        
        










































