# spanning tree : 신장트리
# mst : minimum spanning tree : 최소 신장 트리
from sys import stdin

def goTravel():
  # 첫 번째 줄에는 테스트 케이스의 수 T(T ≤ 100)가 주어지고,
  T = int(stdin.readline()) # 테스트 케이스 수

  for _ in range(T):
    # 첫 번째 줄에는 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 가 주어진다.
    N, M = map(int, stdin.readline().split()) # N:국가 수, M:비행기 종류

    for _ in range(M):
      # 이후 M개의 줄에 a와 b 쌍들이 입력된다. a와 b를 왕복하는 비행기가 있다는 것을 의미한다. (1 ≤ a, b ≤ n; a ≠ b) 
      a, b = map(int, stdin.readline().split())
    # 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.
    print(N-1)

""""
파이썬 입출력은
input() 보다 
from sys import stdin
n = int(stdin.readline()) 가 더 빠름
stdin.readline().split()
""""
