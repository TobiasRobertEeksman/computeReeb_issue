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