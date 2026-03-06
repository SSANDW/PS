L, C = map(int, input().split())
chars = input().split()
chars.sort()

def dfs(start, path):
    if len(path) == L:
        if (sum(1 for c in path if c in 'aeiou') >= 1 and       ''' 모음이 1개 이상 그리고 '''
            sum(1 for c in path if c not in 'aeiou') >= 2):     ''' 자음이 2개 이상 이라면 '''
            print(''.join(path))
        return

    for i in range(start, C):
        dfs(i + 1, path + [chars[i]])                           ''' 깊이 우선 탐색과 백트래킹 '''

dfs(0, [])
