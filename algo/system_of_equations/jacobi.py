import numpy as np

def solve(A, b, timeOfIterator):
    for row in A:
        for c in row:
            c = int(c)
    for c in b:
        c = int(c)
    U = np.triu(A, 1)
    L = np.tril(A, -1)
    D = np.diag(np.diag(A))

    TJ = np.linalg.inv(D).dot(L + U)
    bJ = np.linalg.inv(D).dot(b)

    ans = []
    x = np.zeros((A.shape[0],1))

    for i in range(timeOfIterator):
        x = TJ.dot(x) + bJ
        ans.append(x)

if __name__ == "__main__":
    #A = np.array([[1,2,-3], [-4,5,-6], [-7,8,-9]])
    A = np.array([[10, -1, 2, 0],[-1, 11, -1, 3],[2, -1, 10, -1],[0, 3, -1, 8]])
    b = np.array([[6],[25],[-11],[15]])
    solve(A, b)