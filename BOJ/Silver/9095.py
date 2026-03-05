def go(count, sum, goal): ''' 어디까지 임의에 합을 구하고  --1-- '''
    if sum > goal:        ''' goal을 넘어서면 0 반환 (불가능) --3-- '''
        return 0
    if sum == goal:       ''' goal과 같으면 카운트 + 1 --4-- '''
        return 1
    now = 0
    for k in range(1,4):   ''' 1~3을 더하는 중에 --2-- '''
        now += go(count+1, sum+k, goal)
    return now

t = int(input())

for i in range(t):
    n = int(input())
    print(go(0,0,n))
    
