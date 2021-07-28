from typing import List
from sys import maxsize

def cheapest_flight(costs: List, a: str, b: str) -> int:
    destinations = findAllDestionations(costs)
    destinationValued = {}
    for i in destinations: # Create empty sets with non valued cost of destionation (Key,Value) - (Destination,Cost)
      if i != a:
        destinationValued.setdefault(i, maxsize)
      else: 
        destinationValued.setdefault(i,0)
  
    visitedDestionations = list()
    controledDestinations = list()
    visitedDestionations.append(a) # Set starting point
    controledDestinations.append(a) # Control visited
    while len(destinations) > 0: # Dijskra alghorithm 
      if len(visitedDestionations) < 1: # If non exist route - return 0 
        return 0
      for dest in costs:
        if dest[0] == visitedDestionations[0]: #Left side 
          if destinationValued[dest[1]] == maxsize:
            destinationValued[dest[1]] = dest[2] + destinationValued[dest[0]]
          elif destinationValued[dest[1]] > destinationValued[dest[0]] + dest[2]:
            destinationValued[dest[1]] = destinationValued[dest[0]] + dest[2]
          if dest[1] not in controledDestinations:
            visitedDestionations.append(dest[1])
            controledDestinations.append(dest[1])
        elif dest[1] == visitedDestionations[0]: # right side 
          if destinationValued[dest[0]] == maxsize:
            destinationValued[dest[0]] = dest[2] + destinationValued[dest[1]]
          elif destinationValued[dest[0]] > destinationValued[dest[1]] + dest[2]:
            destinationValued[dest[0]] = destinationValued[dest[1]] + dest[2]
          if dest[0] not in controledDestinations:
            visitedDestionations.append(dest[0])
            controledDestinations.append(dest[0])
      visited = visitedDestionations[0] # Add visited nodes from starting point
      destinations.remove(visited)
      visitedDestionations.pop(0)
      

    return destinationValued[b] # Return destionation what u wish

def findAllDestionations(destinations):
  empty = [row[i] for row in destinations for i in range(2) if row[i]]
  unique = set(empty)
  return unique #Select all unique destinations 

#Test cases 
print(cheapest_flight([["A","C",100],["A","B",20],["D","F",900]],"A","F"))
print(cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C'))