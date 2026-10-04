CAP_A=9
CAP_B=8
GOAL=7

def get_neighbors(state):
    a,b=state
    neighbors=[]
    neighbors.append((CAP_A,b))
    neighbors.append((a,CAP_B))
    neighbors.append((0,b))
    neighbors.append((a,0))
    pour=min(a,CAP_B-b)
    neighbors.append((a-pour,b+pour))
    pour=min(b,CAP_A-a)
    neighbors.append((a+pour,b-pour))
    return neighbors

def dfs(start):
    visited=set()
    stack=[(start,[start])]
    while stack:
        state,path=stack.pop()
        if state[0]==GOAL or state[1]==GOAL:
            return path
        if state in visited:
            continue
        visited.add(state)
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor,path+[neighbor]))
    return None

if __name__=="__main__":
    start=(0,0)
    solution=dfs(start)
    if solution:
        print("Solution found:\n")
        for step,state in enumerate(solution):
            print("Step",step,"-> Jug A:",state[0],", Jug B:",state[1])
    else:
        print("No solution found")