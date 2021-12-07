import heapq

def streaming_median(numbers):
    min_heap = []
    max_heap = []
    left = False
    heapq.heappush(min_heap, numbers[0])
    for n in numbers[1:]:
        if left:
            if n < -max_heap[0]:
                v = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, v)
                heapq.heappush(max_heap, -n)
            else:
                heapq.heappush(min_heap, n)
        else:
            if n > min_heap[0]:
                v = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -v)
                heapq.heappush(min_heap, n)
            else:
                heapq.heappush(max_heap, -n)
        left = not left
    if len(min_heap) == len(max_heap):
        return (min_heap[0] + -max_heap[0]) // 2
    else:
        return min_heap[0]
    
def fuel(value, numbers):
    return sum([abs(n-value) for n in numbers])

def fuel2(value, numbers):
    return sum([sum(range(abs(n-value)+1)) for n in numbers])

numbers = [int(e) for e in open('input.txt', 'r').read().strip().split(',')]
median = streaming_median(numbers)
print(fuel(median, numbers))
v = round(sum(numbers)/len(numbers))
print(min(fuel2(v-1, numbers), fuel2(v, numbers), fuel2(v+1, numbers)))
