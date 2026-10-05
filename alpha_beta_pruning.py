import math

leaf_values={'D':3,'E':5,'F':6,'G':9,'H':1,'I':2,'J':0,'K':-1}

def node_value(node):
    return leaf_values.get(node,0)

tree={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
}

def alphabeta(node,depth,alpha,beta,maximizing):
    if node not in tree:
        return node_value(node)
    if maximizing:
        value=-math.inf
        for child in tree[node]:
            value=max(value,alphabeta(child,depth-1,alpha,beta,False))
            alpha=max(alpha,value)
            if alpha>=beta:
                print(f"Pruning remaining children of {node} (MAX)")
                break
        return value
    else:
        value=math.inf
        for child in tree[node]:
            value=min(value,alphabeta(child,depth-1,alpha,beta,True))
            beta=min(beta,value)
            if alpha>=beta:
                print(f"Pruning remaining children of {node} (MIN)")
                break
        return value

result=alphabeta('A',3,-math.inf,math.inf,True)
print("\nOptimal value using Alpha-Beta pruning:",result)