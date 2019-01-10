import numpy as np

def solve(A, b, time):
    U = np.triu(A, 1)
    L = np.tril(A, -1)
    D = np.diag(np.diag(A))

    Tgs = np.linalg.inv(D - L).dot(U)
    bg = np.linalg.inv(D - L).dot(b)

    ans = []
    x = np.zeros((A.shape[0],1))
    for i in range(time):
        x = Tgs.dot(x) + bg
        ans.append(x)
    return ans

"""
if __name__ == "__main__":
    A = np.array([[10, -1, 2, 0],[-1, 11, -1, 3],[2, -1, 10, -1],[0, 3, -1, 8]])
    b = np.array([[6],[25],[-11],[15]])
    solve(A, b)
"""