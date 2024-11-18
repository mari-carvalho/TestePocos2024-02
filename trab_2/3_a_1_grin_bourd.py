import numpy as np
import matplotlib.pyplot as plt
from Gavsteh_func import calculate_gavsteh
from gringbourdet_deriv import *

# informações da formação:

q = 185 # BOPD
h = 114 #ft
phi = 0.28
ct = 4.1*10**-6 # psi^-1
mi_o = 2.2 #cp
Bo = 1.1 # RB/STB
rw = 0.50 # ft
pwf = 2820 # psia
tp = 540 #hrs
c2_americano = 141.2
c1_americano = 0.0002637

# Δt (hrs) - Coluna 1
delta_t = [
    0.0000, 0.0018, 0.0035, 0.0071, 0.0106, 0.0142, 0.0177, 0.0213, 0.0248, 0.0283,
    0.0319, 0.0390, 0.0425, 0.0496, 0.0567, 0.0638, 0.0708, 0.0815, 0.0921, 0.1027,
    0.1133, 0.1240, 0.1381, 0.1523, 0.1665, 0.1806, 0.1948, 0.2125, 0.2479, 0.2833,
    0.3188, 0.3542, 0.3896, 0.4250, 0.4604, 0.4958, 0.5313, 0.5667, 0.6021, 0.6375,
    0.6906, 0.7438, 0.7969, 0.8500, 0.9031, 0.9563, 1.0094, 1.0625, 1.1156, 1.1688,
    1.2219, 1.2750, 1.3813, 1.4875, 1.5938, 1.7000, 1.9125, 2.0188, 2.1250, 2.3375,
    2.5500, 2.7625, 2.9750, 3.1875, 3.4000, 3.6125, 3.8250, 4.0375, 4.2500, 4.4625,
    4.6750, 4.8875, 5.1000, 5.3125, 5.7375, 6.1625, 6.5875, 7.0125, 7.4375, 7.8625,
    8.2875, 8.7125, 9.1375, 9.5625, 9.9875, 10.4125, 10.8375, 11.2625, 11.6875,
    12.3250, 12.9625, 13.6000, 14.2375, 14.8750, 15.5125, 16.1500, 16.7875, 17.4250,
    18.0625, 18.9125, 19.7625, 20.6125, 21.4625, 22.3125, 23.1625, 24.2250, 25.5000,
    27.6250, 29.7500, 31.8750, 34.0000, 38.2500, 42.5000, 46.7500, 51.0000, 55.2500, 59.5000
]

# Pᵧₒₑₛ (psia) - Coluna 2
pws = [
    2820.00, 2822.15, 2823.18, 2825.61, 2827.67, 2830.28, 2832.71, 2835.33, 2837.76,
    2840.19, 2842.62, 2844.86, 2847.11, 2851.97, 2857.19, 2861.13, 2865.98, 2876.72,
    2883.26, 2889.05, 2895.59, 2900.93, 2909.72, 2917.76, 2926.17, 2934.03, 2942.06,
    2951.60, 2970.66, 2987.87, 3006.01, 3022.46, 3036.49, 3051.08, 3065.68, 3080.63,
    3091.29, 3104.95, 3116.73, 3125.52, 3144.23, 3158.26, 3170.42, 3184.07, 3194.93,
    3207.47, 3218.31, 3228.62, 3235.90, 3244.89, 3253.49, 3260.61, 3274.46, 3284.39,
    3294.70, 3297.68, 3317.54, 3323.15, 3327.83, 3336.24, 3344.09, 3350.80, 3355.10,
    3362.38, 3367.23, 3370.40, 3371.72, 3373.03, 3375.09, 3377.52, 3379.73, 3381.28,
    3383.15, 3384.46, 3384.80, 3387.00, 3387.51, 3388.64, 3389.96, 3390.89, 3391.64,
    3392.76, 3393.32, 3394.07, 3394.63, 3395.39, 3395.94, 3396.56, 3396.88, 3397.63,
    3398.19, 3398.75, 3399.31, 3399.86, 3400.25, 3400.80, 3401.10, 3401.55, 3401.83,
    3402.39, 3402.71, 3403.21, 3403.51, 3403.96, 3404.24, 3404.78, 3405.13, 3406.22,
    3406.62, 3407.52, 3407.90, 3409.71, 3410.10, 3411.42, 3411.83, 3412.83, 3413.25
]

list_delta_p = []
for i in range(len(pws)):
    delta_p = pws[i] - pwf
    list_delta_p.append(delta_p)

derivate_p = []
for i in range(len(delta_t)):
    if i == 0:
        p1 = abs(pws[i] - pwf)
        t1 = abs(np.log(delta_t[i]))
        p2 = abs(pws[i+1]-pws[i])
        t2 = abs(np.log(delta_t[i+1]) - np.log(delta_t[i]))
        derivate_p.append(((p1/t1)*t2 + (p2/t2)*t1)/(t1+t2))
    elif i == len(delta_t) - 1:
        p1 = abs(pws[i] - pws[i-1])
        t1 = abs(np.log(delta_t[i]) - np.log(delta_t[i-1]))
        p2 = abs(pws[i])
        t2 = abs(np.log(delta_t[i]))
        derivate_p.append(((p1/t1)*t2 + (p2/t2)*t1)/(t1+t2))
    else:
        p1 = abs(pws[i] - pws[i-1])
        t1 = abs(np.log(delta_t[i]) - np.log(delta_t[i-1]))
        p2 = abs(pws[i+1] - pws[i])
        t2 = abs(np.log(delta_t[i+1]) - np.log(delta_t[i]))
        derivate_p.append(((p1/t1)*t2 + (p2/t2)*t1)/(t1+t2))

print('derivative_p', derivate_p)
print('log delta p', list_delta_p)

list_log_delta_p = []
list_log_delta_t = []
list_log_derivative_p = []
for i in range(len(list_delta_p)):
    if i == 0:
        delta_p_log = None
        delta_t_log = None
    else:
        delta_p_log = np.log10(list_delta_p[i])
        delta_t_log = np.log10(delta_t[i])
    list_log_delta_t.append(delta_t_log)
    list_log_delta_p.append(delta_p_log)
for i in range(len(derivate_p)):
    if i == 0 or i == 1:
        derivate_p_log = None
    else:
        derivate_p_log = np.log10(derivate_p[i])
    list_log_derivative_p.append(derivate_p_log)
print('list_log_derivative_p', list_log_derivative_p)

plt.plot(list_log_delta_t, list_log_delta_p, marker='o', markersize=2, linestyle='', color='#D5006D', label=r'$\log(\Delta p)$ vs. $\log(\Delta t)$')
plt.plot(list_log_delta_t, list_log_derivative_p, marker='o', markersize=2, linestyle='', color='#00FF00', label=r'$\log(pws^{prime})$')
plt.xlabel(r'$\log(\Delta t)$')
plt.ylabel(r'$\log(\Delta p) \, $ e $\log(pws^{\prime})$')
plt.title(r'Gráfico $\log(\Delta p)$ e $\log(pws^{\prime})$ vs. $\log(\Delta t)$')
plt.legend()
plt.show()

l = 10 # número de coeficientes para a aproximação
 # número de pontos do intervalo do tempo
tD = np.linspace(1e-1, 1e4, 10000)
CDe2s = [1e4, 1e6, 1e8, 1e10, 1e15]
pD_cd_list = []  # Lista para armazenar os resultados da pressão para este reD
rD = 1
ceuler = 0.5772

pD_Cd_list = []
#  Solução
for j in CDe2s:
    pD_Cd = []
    for i in tD:
        # Função de pressão func(u) que será avaliada para cada tempo adimensional:
        func = lambda u: (1/(u*(1/(0.5*np.log(4*j/(np.exp(ceuler**2)*u)))+u))) # equação do slide 27
        # Chama a função gavsteh_param para calcular a pressão adimensional:
        pD_Cd.append(calculate_gavsteh.gavsteh_param(l, func, i))
    pD_Cd_list.append(pD_Cd)
print('pD_Cd_list', pD_Cd_list)

derivative_GringBourdet = deriv_bourdet(pD_Cd_list, CDe2s, tD)

# Plotagem dos gráficos:
plt.figure()
cores = ['#1abc9c', '#e67e22', '#f1c40f', '#e84393', '#3498db'] # Cores para cada valor de S
lines = []

for t in range(len(CDe2s)):
    plt.plot(tD, pD_Cd_list[t], color=cores[t], linewidth=1, label=f'CDe2s = {CDe2s[t]}')
    plt.plot(tD[:-1], derivative_GringBourdet[t], color=cores[t], linestyle='--')
    plt.legend()
plt.xlabel(r'$t_D$/$C_D$')
plt.ylabel(r'$p_D$ and $p_D^{\prime},(t_D/C_D)$')
plt.title('Solução Reservatório Infinito com Efeitos de Película e Estocagem')
#plt.xlim(9*10**1, 10**7)
#plt.ylim(0.2, 100)
plt.grid(color="gray", linestyle='--')

# translação:
list_delta_t_ajus = []
list_delta_p_ajus = []
list_derivative_p_ajus = []
for i in delta_t:
    delta_t_ajust = i*16.8
    list_delta_t_ajus.append(delta_t_ajust)
for i in list_delta_p:
    delta_p_ajus = i*0.024
    list_delta_p_ajus.append(delta_p_ajus)
for i in derivate_p:
    derivate_p_ajus = i* 0.024
    list_derivative_p_ajus.append(derivate_p_ajus)

plt.plot(list_delta_t_ajus, list_delta_p_ajus, marker='o', markersize=2, linestyle='', color='#D5006D')
plt.plot(list_delta_t_ajus, list_derivative_p_ajus, marker='o', markersize=2, linestyle='', color='#89CFF0')
plt.xscale('log',)
plt.yscale('log')
plt.show()

delta_t_match = delta_t[20]
tD_Cd_match = delta_t_match*16.8
delta_p_match = list_delta_p[20]
pD_match = delta_p_match*0.024

k = ((c2_americano*Bo*mi_o*q)/h) * (pD_match/delta_p_match)
print('k', k)

Cd = (c1_americano*k)/(phi*mi_o*ct*(rw**2)) * (delta_t_match/tD_Cd_match)
print('Cd', Cd)

s = 0.5 * np.log(1e10/Cd)
print('s', s)

# cálculo do raio efetivo:

rwa = rw*(np.exp(-s))
print('rwa', rwa)