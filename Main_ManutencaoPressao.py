import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp
from Gavsteh_func import calculate_gavsteh

#rD  # Raio do poço cilíndrico
rD = 1
reD = [100, 200 ,300 ,400 ,500 ,600 ,700 ,800 ,900 ,1000,
           1100, 1200, 1300 ,1400, 1500, 1600, 1700, 1800, 1900, 2000, 2500, 3000] # Lista de distâncias reservatório-poçon  # Número de termos no método de Stehfest
l = 16 # número de coeficientes para a aproximação
 # número de pontos do intervalo do tempo
tD = np.linspace(10e2,10e6, 10000) # Array de tempo adimensionalpD = []
pD = []

#  Solução
for j in reD:
    pD_reD = []  # Lista para armazenar os resultados da pressão para este reD
    for i in tD:
        # Função de pressão func(u) que será avaliada para cada tempo adimensional:
        func = lambda u: (
                (sp.i0(j * np.sqrt(u)) * sp.k0(rD * np.sqrt(u))) -
                 (sp.i0(rD * np.sqrt(u)) * sp.k0(j * np.sqrt(u)))) / ((
                (u ** (3 / 2)) * (sp.i1(np.sqrt(u)) * sp.k0(j * np.sqrt(u)) + (sp.k1(np.sqrt(u)) * sp.i0(j * np.sqrt(u)))))) # equação do slide 27
        # Chama a função gavsteh_param para calcular a pressão adimensional:
        pD_reD.append(calculate_gavsteh.gavsteh_param(l, func, i))
    pD.append(pD_reD)

# Solução para tempos curtos:
p_wd_short = []
for i in tD:
    p_wd_short.append((np.log(i) + 0.80907)/2)

p_wd_long = []
# Solução para tempos longos:
p_wd_long = [np.log(reD[0]) for _ in tD]

# Plotagem dos gráficos:
fig, ax = plt.subplots()
for k in range(len(pD)):
    ax.plot(tD, pD[k], label=f"reD = {reD[k]}")
ax.set_xscale("log")
ax.set_ylim(3, 9)
ax.grid(color="gray", linestyle='--')
ax.plot(tD, p_wd_short, label='Solução de Tempos Curtos', color='mediumvioletred', linestyle='-', linewidth='3')
ax.plot(tD, p_wd_long, label='Solução de Tempos Longos', color='aqua', linestyle='-', linewidth='3')
plt.xlabel('pD')
plt.ylabel('tD')
plt.title(f"Solução Reservatório com Manutenção de Pressão e Poço Cilíndrico")
plt.legend(framealpha=1, loc='upper left', fontsize=7)
plt.yticks(np.arange(3, 9, step=0.25))
plt.show()

