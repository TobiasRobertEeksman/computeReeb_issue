I got an error using the computeReeb() function. We were able to create two cases, where one works and one doesn't.
We are using the x-value as the height map and create lowerstar filtrations accordingly. 

For the case:
```python
    V = np.array([[0,0,0], [1,0,0],
                    [2,1,0]])
    F = np.array([[0,1], [0,2], [1,2]])
```
The calculation works and we do get a ReebGraph.

However for the case:
```python
    V = np.array([[0,0,0], [1,0,0],
                    [0,1,0]])
    F = np.array([[0,1], [0,2], [1,2]])
```
The computation doesn't work anymore and we get this error:

```bash
Traceback (most recent call last):
  File "c:\Users\Tobias\OneDrive - Schulen kvBL\Dokumente\ETH\cereeberus\ceREEBerus\test.py", line 223, in <module>
    R1 = computeReeb(st1)
  File "C:\Users\Tobias\AppData\Local\Programs\Python\Python310\lib\site-packages\cereeberus\compute\computereeb.py", line 139, in computeReeb
    R.add_edge(e, nextNodeName)
  File "C:\Users\Tobias\AppData\Local\Programs\Python\Python310\lib\site-packages\cereeberus\reeb\reebgraph.py", line 386, in add_edge
    raise ValueError(
ValueError: The vertex e_0 must be in the Reeb graph to add an edge between them.
```

We think the issue lies in the fact, that in the second case, two of the vertices get the same filtration value. Here's our full implementation for checking:

```python
from cereeberus import LowerStar, computeReeb
import numpy as np
import matplotlib.pyplot as plt

def f_x(pts: np.ndarray) -> np.ndarray:
    return pts[:, 0].astype(float)

def create_lower_star(V,F):
    st = LowerStar()

    for i,v in enumerate(V):
        st.insert([i])

    for face in F:
        st.insert(face)

    for i, v in enumerate(V):
        st.assign_filtration([i], f_x(V)[i])

    return st

if __name__ == "__main__":

    #Example 1: which works
    V = np.array([[0,0,0], [1,0,0],
                    [2,1,0]])
    F = np.array([[0,1], [0,2], [1,2]])

    # # Example 2: which doesn't work
    # V = np.array([[0,0,0], [1,0,0],
    #                 [0,1,0]])
    # F = np.array([[0,1], [0,2], [1,2]])

    st1 = create_lower_star(V,F)
    R1 = computeReeb(st1)
    R1.draw(cpx = 2.0)
    plt.show()
```
