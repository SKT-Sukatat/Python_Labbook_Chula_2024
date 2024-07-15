n = int(input())
points = []

for i in range(1,n+1):
    point = []
    x, y = [float(p) for p in input().split()]
    distance = (x**2 + y**2)**(0.5)
    point.append(distance)
    point.append(i)
    point.append(x)
    point.append(y)
    points.append(point)

points.sort(key=lambda x: x[0])

print("#"+ str(points[2][1])+ ": "+ "(" + str(points[2][-2]) + " "+ str(points[2][-1]) + ")")
