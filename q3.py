def calculateInDegrees(gp):
    inD = {}

    for i in gp.keys():
        inD[i] = 0
        for j in gp.keys():
            for k in gp[j]:
                if k == i:
                    inD[i] += 1
    
    return inD


def foo(graph): 
    inDegrees = calculateInDegrees(graph)
    
    independent = [ x for x in inDegrees.keys() if inDegrees[x] == 0]
    print(inDegrees)
    print(independent)

    visited = independent.copy()
    queue = independent.copy()
    queue.append(-1)

    trav = []
    lvl = []
    ans = [independent]

    while len(queue):
        fnt = queue[0]

        print(f'{queue}  {lvl}  {ans}')

        if fnt == -1:
            queue.pop(0)
            if len(queue) == 0:
                break
            queue.append(-1)
            ans.append(lvl)
            lvl = []     
            continue

        trav.append(fnt)
        queue.pop(0)

        for i in graph[fnt]:
            if i not in visited:                
                inDegrees[i] -= 1

                if inDegrees[i] == 0:
                    lvl.append(i)
                    visited.append(i)
                    queue.append(i)
    
    print(trav)
    print(ans)
    return len(ans)


def main():
    graph = {
        1 : [2, 3],
        2 : [4],
        3 : [6, 8],
        4 : [5], 
        5 : [6],
        6 : [7],
        7 : [],
        8 : []
    }

    print(foo(graph))

main()