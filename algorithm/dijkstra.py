dijkstra(Start)

count=0

max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max_(max_distance, d)

print(count - 1, max_distance)