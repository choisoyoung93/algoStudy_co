import sys
# 기본적으로, 반복은 1000회로 되어 있기 때문에, sys.setrecursionlimit(10**9)로 늘려줬다.
sys.setrecursionlimit(10**9)

def DFS(start, tree, parents) :
    # 연결된 노드들부터 parents[i]의 부모가 없으면 부모 설정 -> DFS
    for i in tree[start] :
        if parents[i] == 0 :
            parents[i] = start
            DFS(i, tree, parents)

def getParentNode():
  # 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
  N = int(sys.stdin.readline())
  # 트리생성
  Tree = [[] for _ in range(N+1)]

  # 부모노드 저장
  Parents = [0 for _ in range(N+1)]

  # 트리 구조 입력
  # 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
  for _ in range(N-1) :
    a, b = map(int, sys.stdin.readline().split())
    Tree[a].append(b)
    Tree[b].append(a)
  
  DFS(1, Tree, Parents)

  # 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
  for i in range(2, N+1) :
    print(Parents[i])
