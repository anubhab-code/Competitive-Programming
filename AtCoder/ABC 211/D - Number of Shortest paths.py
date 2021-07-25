from typing import Counter
import sys
from collections import defaultdict as dd
from math import *
from collections import deque

def vinp():
    return map(int,input().split())
def linp():
    return list(map(int,input().split()))
def sinp():
    return input()
def inp():
    return int(input())
def mod(f):
    return f % 1000000007
def pr(*x):
    print(*x)
def finp():
    f=open("input.txt","r")
    f=f.read().split("\n")
    return f
def finp():
    f=open("input.txt","r")
    f=f.read().split("\n")
    return f
def fout():
    return open("output.txt","w")
def fpr(f,x):
    f.write(x+"\n")
def csort(c):
    sorted(c.items(), key=lambda pair: pair[1], reverse=True)
def indc(l,n):
    c={}
    for i in range(n):
        c[l[i]]=c.get(l[i],[])+[i+1]
    return c
mod = int(1e9+7)
maxsize=sys.maxsize

def BFS(adj,src,dist,paths,n):
    visited = [False] * n
    dist[src] = 0
    paths[src] = 1
    q = deque()
    q.append(src)
    visited[src] = True
    while q:
        curr = q[0]
        q.popleft()
        for x in adj[curr]:
            if not visited[x]:
                q.append(x)
                visited[x] = True
            if dist[x] > dist[curr] + 1:
                dist[x] = dist[curr] + 1
                paths[x] = paths[curr]
            elif dist[x] == dist[curr] + 1:
                paths[x] += paths[curr]

def findShortestPaths(adj, s, n):
    dist = [maxsize] * n
    paths = [0] * n
    BFS(adj, s, dist, paths, n)
    pr(paths[-1] % mod)

if __name__ =="__main__":
    n, m = vinp()
    adj = [0] * n
    for i in range(n):
        adj[i] = []
    for i in range(m):
        a, b = vinp()
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    findShortestPaths(adj, 0, n)