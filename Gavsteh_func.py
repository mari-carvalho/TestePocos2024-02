import math
import numpy as np

class calculate_gavsteh():
    def gavsteh_param(l, Gavsteh_func, time):
        """l= Numero de coeficientes"""
        t = time
        n = int(l / 2)
        v = []

        # Calcula os coeficientes v[j] usando o método de Gav-Stehfest
        for j in range(1, l + 1):
            z = 0
            for k in range(((j + 1) // 2), min(j, n) + 1):
                z += ((k ** n) * math.factorial(2 * k)) / (
                        math.factorial(n - k) * math.factorial(k) * math.factorial(k - 1) *
                        math.factorial(j - k) * math.factorial((2 * k) - j))
            v.append((-1) ** (j + n) * z)

        # Calcula a transformada inversa de Laplace usando os coeficientes
        somme = 0
        ln2_on_t = np.log(2.0) / t
        for j in range(1, l + 1):
            p = j * ln2_on_t
            somme += v[j - 1] * Gavsteh_func(p)

        ilt = somme * ln2_on_t
        return ilt
