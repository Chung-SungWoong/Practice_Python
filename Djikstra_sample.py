"""
개선된 다익스트라 
"""

import heapq
import sys
import sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n + 1)]