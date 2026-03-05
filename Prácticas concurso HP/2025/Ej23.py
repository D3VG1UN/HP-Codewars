vines=input().split()

cost=0

while len(vines)>=2:
    if len(vines)==2:
        cost+=sum(map(int, vines))
        vines=[]
    else:
        min_cost=sorted(vines, key=int)[:2]
        vines.remove(min_cost[0])
        vines.remove(min_cost[1])

        newVine=sum(map(int, min_cost))
        cost+=newVine
        vines.append(newVine)

print(cost)