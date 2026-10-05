class GoalStackPlanner:
    def __init__(self,initial_state,goal_stack):
        self.state=set(initial_state)
        self.goal_stack=goal_stack
        self.plan=[]
        
    def achieve(self,goal):
        if goal in self.state:
            return
        block,_,target=goal.partition(' on ')
        action=f"Move({block} -> {target if target else 'Table'})"
        self.plan.append(action)
        self.state={s for s in self.state if not s.startswith(f"{block} on")}
        self.state.add(goal)
        
    def run(self):
        while self.goal_stack:
            goal=self.goal_stack.pop()
            self.achieve(goal)
        return self.plan

initial_state=["A on Table","B on Table","C on A"]
goal_stack=["C on Table","B on C","A on B"]
planner=GoalStackPlanner(initial_state,goal_stack)
plan=planner.run()

print("Generated Plan:")
for step in plan:
    print(step)
print("\nFinal State:",planner.state)