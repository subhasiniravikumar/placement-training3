import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print("Heap:", heap)

print("Removed element:", heapq.heappop(heap))
print("Heap after removal:", heap)
