

import numpy as np



def main():
    n1=np.mat("4 11 14 5;8 7 -2 6")
    U, Sigma, V = np.linalg.svd(n1, full_matrices=False)
    print("U")
    print(U)
    print("Sigma")
    print(Sigma)
    print("V")
    print(V)
    print(U*np.diag(Sigma)*V)


if __name__ == '__main__':
    main()