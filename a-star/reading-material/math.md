# Manhattan distance
 
Calculate the total distance horizontally and vertically

```math
(|x₁ - x₂| + |y₁ - y₂|)
```

```python
def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
```

# Weighted graph
A weighted graph is a graph where every edge has a number, called a weight—that represents a quantity like distance, cost, or time

# Time Complexity Breakdown

The total worst-case time complexity of A* on a grid is $O(V \log V + E)$, where:

- **$V$** = Total number of walkable nodes (grid cells, up to $N \times N$)
- **$E$** = Total number of edges (connections between neighboring cells, up to $4V$ for a 4-directional grid)

When written strictly in terms of grid dimensions for an $N \times N$ grid (where $V = N^2$), it simplifies to $O(N^2 \log(N^2))$, which is equivalent to $O(N^2 \log N)$.