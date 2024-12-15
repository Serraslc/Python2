import math
def euclideanDistance(p1,p2):
   return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

points = [(1, 2), (4, 6)]
distances = []
for i in range(len(points)):
   for j in range(i + 1,len(points)):
      distance = euclideanDistance(points[i], points[j])
      distances.append(distance)
min_distance = min(distances)
print(f"The minimum Euclidean distance is: {min_distance}") 
