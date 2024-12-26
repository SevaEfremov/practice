import heapq
from collections import Counter


def huffman_encode(text):
    freq = Counter(text)

    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_codes = dict(heap[0][1:])

    encoded_text = "".join(huffman_codes[char] for char in text)

    print(f"{len(freq)} {len(encoded_text)}")
    for char, code in sorted(huffman_codes.items()):
        print(f"'{char}': {code}")
    print(encoded_text)

text = "Errare humanum est."
huffman_encode(text)