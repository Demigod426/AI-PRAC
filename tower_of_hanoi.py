from collections import deque

start=((3,2,1),(),())
goal=((),(),(3,2,1))
queue=deque()
queue.append((start,[]))
visited=set()
visited.add(start)

def get_next_states(state):
    next_states=[]
    rods=[list(rod) for rod in state]
    for i in range(3):
        if not rods[i]:
            continue
        disk=rods[i][-1]
        for j in range(3):
            if i==j:
                continue
            if not rods[j] or rods[j][-1]>disk:
                new_rods=[r[:] for r in rods]
                moved_disk=new_rods[i].pop()
                new_rods[j].append(moved_disk)
                new_state=tuple(tuple(r) for r in new_rods)
                move_text=f"Move disk {disk} from Rod {i+1} to Rod {j+1}"
                next_states.append((new_state,move_text))
    return next_states

while queue:
    state,path=queue.popleft()
    if state==goal:
        print("Solution found using BFS:\n")
        for step in path:
            print(step)
        print("\nFinal State:")
        print(state)
        break
    for next_state,move in get_next_states(state):
        if next_state not in visited:
            visited.add(next_state)
            queue.append((next_state,path+[move]))