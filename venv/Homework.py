from typing import List, Dict, Tuple

matrixA: List[List[int]] = [[1, 4, 5, 12],
                            [-5, 8, 9, 3],
                            [6, 7, 11, 10]]

matrixB: List[List[int]] = [[3, -4, 3, 6],
                            [4, 7, 9, 3],
                            [2, 9, 1, 4],
                            [7, 7, 5, 2]]

vectorA: List[int] = [1, 4, 6, 2]
vectorB: List[int] = [6, 2, 7, 1]


class Matrix:
    @staticmethod
    def multiple(a: List[List[int]], b: List[List[int]]):
        matrixRes: List = [[0 for i in range(len(b[0]))] for i in range(len(a))]
        for m in range(len(a)):
            if len(a[m]) == len(b):
                for n in range(len(a[m])):
                    if len(b[0]) == len(b[n]):
                        for k in range(len(b[n])):
                            matrixRes[m][k] = matrixRes[m][k] + a[m][n] * b[n][k]
                    else:
                        print('Bledny rozmiar macierzy b')
                        return False
            else:
                print('Bledny rozmiar macierzy a')
                return False
        for x in matrixRes:
            print(x)
        return matrixRes

    @staticmethod
    def transpose(a: List[List[int]]):
        matrixTrans: List = [[0 for i in range(len(a[0]))] for i in range(len(a))]
        for m in range(len(a)):
            if len(a[0]) == len(a[m]):
                for n in range(len(a[m])):
                    matrixTrans[m][n] = a[n][m]
            else:
                print('Bledny rozmiar macierzy')
                return False
        for x in matrixTrans:
            print(x)

    @staticmethod
    def scalar(a: List[int], b: List[int]):
        if len(a) == len(b):
            vector = [sum(a*b for a, b in zip(a,b))]
            print(vector)


Matrix.multiple(matrixA, matrixB)
Matrix.transpose(matrixB)
Matrix.scalar(vectorA, vectorB)

