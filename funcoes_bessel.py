import numpy as np
import matplotlib.pyplot as plt
from scipy.special import k0, k1, i0, i1

# Definição do intervalo de valores de x:
x = np.linspace(0, 4, 40)

# Calcular as funções de Bessel Modificadas de Primeira (I0 e I1) e Segunda (K0 e K1) Espécie:
K0 = k0(x) # Função de Bessel Modificada de Segunda Espécie K0
K1 = k1(x) # Função de Bessel Modificada de Segunda Espécie K1
I0 = i0(x) # Função de Bessel Modificada de Primeira Espécie I0
I1 = i1(x) # Função de Bessel Modificada de Primeira Espécie I1

# Plotar as Funções:
plt.figure(figsize=(8,6))
plt.plot(x, K0, label=r'$K_0(x)$', color='#1abc9c', linestyle='-')
plt.plot(x, K1, label=r'$K_1(x)$', color='#e67e22', linestyle='--')
plt.plot(x, I0, label=r'$I_0(x)$', color='#3498db', linestyle='-')
plt.plot(x, I1, label=r'$I_1(x)$', color='#e84393', linestyle='--')

# Configurações do Gráfico:
plt.title("Funções de Bessel de Primeira e Segunda Espécie $K$ e $I$")
plt.xlabel('x')
plt.ylabel('K e I')
plt.legend()
plt.grid(True)
plt.show()
