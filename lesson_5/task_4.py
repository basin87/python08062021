import random
randlist = [random.randint(0, 100) for index in range(10)]
print(randlist)
randlist=list(map(lambda x:0 if x%2!=0 else x,randlist))
print(*randlist)
