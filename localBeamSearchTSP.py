import random

def tour_length(tour,dist):
    return sum(dist[tour[i]][tour[(i+1)%len(tour)]] for i in range(len(tour)))

def neighbors(tour):
    result=[]
    for i in range(len(tour)):
        for j in range(i+1,len(tour)):
            new_tour=tour[:]
            new_tour[i],new_tour[j]=new_tour[j],new_tour[i]
            result.append(new_tour)
    return result

def local_beam_search(cities,dist,k=4,iterations=100):
    beams=[random.sample(cities,len(cities)) for _ in range(k)]
    for _ in range(iterations):
        candidates=[]
        for tour in beams:
            candidates.extend(neighbors(tour))
        candidates.sort(key=lambda t:tour_length(t,dist))
        beams=candidates[:k]
    best=min(beams,key=lambda t:tour_length(t,dist))
    return best,tour_length(best,dist)

cities=['A','B','C','D','E']
dist={
    'A':{'A':0,'B':2,'C':9,'D':10,'E':7},
    'B':{'A':2,'B':0,'C':6,'D':4,'E':3},
    'C':{'A':9,'B':6,'C':0,'D':8,'E':5},
    'D':{'A':10,'B':4,'C':8,'D':0,'E':6},
    'E':{'A':7,'B':3,'C':5,'D':6,'E':0}
}

best_tour,best_len=local_beam_search(cities,dist)
print("Best tour found:",best_tour)
print("Total tour length:",best_len)