environment={'A': 'Dirty', 'B': 'Dirty'}
location='A'
action_table={
    ('A','Dirty'):'SUCK',
    ('A','Clean'):'MOVE_RIGHT',
    ('B','Dirty'):'SUCK',
    ('B','Clean'):'MOVE_LEFT'}

while True:
    print("Location:",location)
    print("Environment:",environment)
    
    if environment['A']=='Clean' and environment['B']=='Clean':
        print("Action: STOP")
        break
        
    percept=(location, environment[location])
    action=action_table[percept]
    
    print("Selected Action:",action)

    if action=='SUCK':
        environment[location]='Clean'
    elif action=='MOVE_RIGHT':
        location='B'
    elif action=='MOVE_LEFT':
        location='A'
        
    print("-"*40)

print("\nAnalysis")
print("The table-driven agent always chooses an action")
print("based on the current percept stored in the table.")
print("Hence it behaves rationally in this environment.")