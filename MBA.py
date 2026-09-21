from collections import deque

grid=[
    ['S',0,0,'X'],
    [0,'X',0,0],
    [0,0,0,'X'],
    ['X',0,0,'G']
]
rows=len(grid)
cols=len(grid[0])
start=(0,0)
goal=(3,3)
queue=deque([(start,[start])])
visited=set()
visited.add(start)
directions=[(-1,0),(1,0),(0,-1),(0,1)]
print("Grid Navigation Begins\n")
final_path=None

while queue:
    current,path=queue.popleft()
    print("Current Position:",current)
    print("Visited:",visited)
    if current==goal:
        final_path=path
        print("\nGoal Reached!")
        break
    for dr,dc in directions:
        nr=current[0]+dr
        nc=current[1]+dc
        if 0<=nr<rows and 0<=nc<cols:
            if grid[nr][nc]=='X':
                continue
            if (nr,nc) in visited:
                continue
            visited.add((nr,nc))
            queue.append(((nr,nc),path+[(nr,nc)]))

print("\n============================")
if final_path:
    print("Path Found:")
    print(final_path)
else:
    print("No path exists.")

print("\nRational Behaviour Analysis")
print("1. The agent remembers visited cells.")
print("2. It never revisits explored locations.")
print("3. It avoids obstacles.")
print("4. It systematically searches for the goal.")
print("Hence, it behaves as a Model-Based Intelligent Agent.")