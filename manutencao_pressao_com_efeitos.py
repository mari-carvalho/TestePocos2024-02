import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp
from Gavsteh_func import calculate_gavsteh
from matplotlib.ticker import ScalarFormatter

#rD  # Raio do poço cilíndrico
rD = 1
reD = [100, 200 ,300 ,400 ,500 ,600 ,700 ,800 ,900 ,1000,
           1100, 1200, 1300 ,1400, 1500, 1600, 1700, 1800, 1900, 2000, 2500, 3000] # Lista de distâncias reservatório-poçon  # Número de termos no método de Stehfest
l = 10 # número de coeficientes para a aproximação
 # número de pontos do intervalo do tempo
tD = np.logspace(2,8, 40) # Array de tempo adimensionalpD = []
Cd = [1, 10e2, 10e3, 10e4, 10e5]
S = [-1, 0, 5, 10, 20]
pD_cd_list = []  # Lista para armazenar os resultados da pressão para este reD

#  Solução
for cd in Cd:
    pD_s_list = []
    for s in S:
        pD_s = []
        for i in tD:
            # Função de pressão func(u) que será avaliada para cada tempo adimensional:
            func = lambda u: (
                    (sp.k0(rD * np.sqrt(u)) + s * np.sqrt(u) * sp.k1(np.sqrt(u))) / (
                    u * (np.sqrt(u) * sp.k1(np.sqrt(u)) + cd * u * (sp.k0(np.sqrt(u)) + s * np.sqrt(u) * sp.k1(np.sqrt(u)))))) # equação do slide 27
            # Chama a função gavsteh_param para calcular a pressão adimensional:
            pD_s.append(calculate_gavsteh.gavsteh_param(l, func, i))
        pD_s_list.append(pD_s)
    pD_cd_list.append(pD_s_list)

# Plotagem dos gráficos:
plt.figure()
cores = ['#1abc9c', '#e67e22', '#f1c40f', '#e84393', '#3498db'] # Cores para cada valor de S
lines = []

for k in range(len(pD_cd_list)):
    s_plot = pD_cd_list[k]
    for t in range(len(s_plot)):
        t_plot = s_plot[t]
        line, = plt.loglog(tD, t_plot, color=cores[k], linewidth=1)
    lines.append(line)

plt.xlabel('tD')
plt.ylabel('pD')
plt.title('Modelo com Efeitos de Estocagem e Película')
plt.xlim(10**2, 10**8)
plt.ylim(0.1, 100)
plt.grid(color="gray", linestyle='--')

plt.legend(lines, [f'Cd={Cd[k]:.1e}' for k in range(len(Cd))])
plt.show()

