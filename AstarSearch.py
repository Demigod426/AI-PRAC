import heapq

GOAL_STATE=(1,2,3,4,5,6,7,8,0)

def heuristic(state):
    misplaced=0
    for i in range(9):
        if state[i]!=0 and state[i]!=GOAL_STATE[i]:
            misplaced+=1
    return misplaced

def get_neighbors(state):
    neighbors=[]
    state=list(state)
    zero_index=state.index(0)
    row,col=divmod(zero_index,3)
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    for dr,dc in moves:
        new_row,new_col=row+dr,col+dc
        if 0<=new_row<3 and 0<=new_col<3:
            new_index=new_row*3+new_col
            new_state=state.copy()
            new_state[zero_index],new_state[new_index]=new_state[new_index],new_state[zero_index]
            neighbors.append(tuple(new_state))
    return neighbors

def a_star(start_state):
    open_list=[]
    heapq.heappush(open_list,(heuristic(start_state),0,start_state,[start_state]))
    visited=set()
    while open_list:
        f,g,current_state,path=heapq.heappop(open_list)
        if current_state==GOAL_STATE:
            return path,g
        if current_state in visited:
            continue
        visited.add(current_state)
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                new_g=g+1
                new_f=new_g+heuristic(neighbor)
                heapq.heappush(open_list,(new_f,new_g,neighbor,path+[neighbor]))
    return None,-1

def print_state(state):
    for i in range(0,9,3):
        row=state[i:i+3]
        print(" ".join(str(x) if x!=0 else "_" for x in row))
    print()

if __name__=="__main__":
    start_state=(1,2,3,4,0,6,7,5,8)
    print("Start State:")
    print_state(start_state)
    print("Goal State:")
    print_state(GOAL_STATE)
    solution_path,moves=a_star(start_state)
    if solution_path:
        print(f"Solved in {moves} moves!\n")
        for step,state in enumerate(solution_path):
            print(f"Step {step}:")
            print_state(state)
    else:
        print("No solution found.")