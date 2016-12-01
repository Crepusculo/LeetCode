import heapq

matrix = [[90, 75, 75, 80],
          [35, 85, 55, 65],
          [125, 95, 90, 105],
          [45, 110, 95, 115]]

N = 4

initial_status = [sum([min(x) for x in matrix]), [], 0]

pq = []
heapq.heappush(pq, initial_status)

total = sum([sum(x) for x in matrix])

best = [total, [], total]

while pq:
    status = heapq.heappop(pq)
    i = len(status[1])
    if status[0] > best[2]:
        break
    if i == N:
        if status[2] < best[2]:
            best = status
    else:
        for t in range(N):
            if t not in status[1]:
                tst = [status[2] + matrix[i][t] + sum([min(x) for x in matrix[i+1:]]),
                       status[1] + [t],
                       status[2] + matrix[i][t]]
                heapq.heappush(pq, tst)

print(best)