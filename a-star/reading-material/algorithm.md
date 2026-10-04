# A* Algorithm

1. Initialize the open list.
2. Initialize the closed list and place the starting node on the open list.
   - You can leave its `f` value at zero.
3. While the open list is not empty:
   1. Find the node with the lowest `f` value on the open list and call it `q`.
   2. Remove `q` from the open list.
   3. Generate `q`'s 8 successors and set their parent to `q`.
   4. For each successor:
      1. If the successor is the goal, stop the search.
      2. Otherwise, compute both `g` and `h` for the successor:
         - `successor.g = q.g + distance(successor, q)`
         - `successor.h = distance(goal, successor)`
         - This can be computed using several heuristics, such as Manhattan, Diagonal, or Euclidean distance.
         - `successor.f = successor.g + successor.h`
      3. If a node with the same position as the successor is already in the open list and has a lower `f` value, skip this successor.
      4. If a node with the same position as the successor is already in the closed list and has a lower `f` value, skip this successor.
      5. Otherwise, add the node to the open list.
   5. Push `q` onto the closed list.

```text
Initialize the open list
Initialize the closed list
Put the starting node on the open list (you can leave its f at zero)

while the open list is not empty:
    q = node with the lowest f on the open list
    pop q off the open list

    generate q's 8 successors and set their parents to q

    for each successor:
        if successor is the goal:
            stop search
        else:
            successor.g = q.g + distance(successor, q)
            successor.h = distance(goal, successor)
            successor.f = successor.g + successor.h

        if a node with the same position as successor is in the OPEN list
           with a lower f than successor:
            skip this successor

        if a node with the same position as successor is in the CLOSED list
           with a lower f than successor:
            skip this successor
        else:
            add the node to the open list

    push q onto the closed list
```