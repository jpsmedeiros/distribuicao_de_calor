import pprint
from src.fatoracao_lu import fatoracao_lu
from src.fatoracao_lu import resolve_lu

def main():
    A = [[4, 7, 2, 1], [8, 1, 3, 6], [5, 9, 2, 7], [3, 2, 8, 0]]
    B = [1, 2, 3, 4]
    L, U = fatoracao_lu(A)
    print("A")
    pprint.pprint(A)
    print("L")
    pprint.pprint(L)
    print("U")
    pprint.pprint(U)

    print(resolve_lu(A, B))


if __name__ == "__main__":
    main()
