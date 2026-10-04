from collections import deque

GOAL=(1,2,3,4,5,6,7,8,0)

def get_neighbors(state):
    neighbors=[]
    i=state.index(0)
    row,col=i//3,i%3
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    for dr,dc in moves:
        r,c=row+dr,col+dc
        if 0<=r<3 and 0<=c<3:
            j=r*3+c
            new_state=list(state)
            new_state[i],new_state[j]=new_state[j],new_state[i]
            neighbors.append(tuple(new_state))
    return neighbors

def bfs(start):
    visited={start}
    queue=deque([(start,[])])
    while queue:
        state,path=queue.popleft()
        if state==GOAL:
            return path+[state]
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,path+[state]))
    return None

def print_state(state):
    for i in range(0,9,3):
        print(state[i:i+3])
    print()

if __name__=="__main__":
    start=(5,4,1,8,0,6,2,7,3)
    solution=bfs(start)
    if solution:
        print("Solved in",len(solution)-1,"moves\n")
        for step,state in enumerate(solution):
            print("Step",step)
            print_state(state)
    else:
        print("No solution found")