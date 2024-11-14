import numpy as np
import matplotlib.pyplot as plt
import math as mt
import pandas as pd

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

plt.plot(delta_t, pws, marker='o', linestyle='', color='#D5006D', label='pws vs delta_t')
plt.xlabel('delta_t [hrs]')
plt.ylabel('pws [ psia]')
plt.title('Gráfico de Pws vs. Delta t')
plt.legend()
plt.show()

list_eixo_x = []
for i in range(len(delta_t)):
    if i == 0:
        eixo_x = None
    else:
        eixo_x = (tp*delta_t[i])/(tp+delta_t[i])
    list_eixo_x.append(eixo_x)

print('x', list_eixo_x)
list_log_eixo_x = []
for j in range(len(list_eixo_x)):
    if j == 0:
        log_eixo_x = None
    else:
        log_eixo_x = np.log10(list_eixo_x[j])
    list_log_eixo_x.append(log_eixo_x)
print('log', list_log_eixo_x)

plt.plot(list_log_eixo_x, pws, marker='o', linestyle='', color='#D8A7FF', label='pws vs log(tp*delta t)/(tp+delta t)')
plt.xscale('symlog', linthresh=1)
plt.xlabel('log(tp*delta t)/(tp+delta t)')
plt.ylabel('pws [ psia]')
plt.title('Gráfico de Pws vs. log(tp*delta t)/(tp+delta t)')
plt.legend()
plt.show()

list_selecao = [-0.6059228008197698, -0.5479812094868574, -0.4967380062159451, -0.4510362147717714, -0.4096942742411091,
                -0.3719527413555314, -0.3372348035427853, -0.30509204130021766, -0.27508727153665274, -0.24710231630541443,
                -0.22081534137780026, -0.19603221725475442, -0.16132848551984585, -0.12914161480848155, -0.09923660679432256,
                -0.0712641485064013, -0.04498986835795052, -0.020174267371679922, 0.0032522492126534795, 0.02547526368395288,
                0.04661221088514291, 0.06680121247777454, 0.08605406305795169, 0.10448597590346909]
print(len(list_selecao))
pws_selecao = [2970.66, 2987.87, 3006.01, 3022.46, 3036.49, 3051.08, 3065.68, 3080.63,
    3091.29, 3104.95, 3116.73, 3125.52, 3144.23, 3158.26, 3170.42, 3184.07, 3194.93,
    3207.47, 3218.31, 3228.62, 3235.90, 3244.89, 3253.49, 3260.61]
print(len(pws_selecao))

# ajustando uma linha de tendência no gráfico semilog:
grau = 1
coeffs = np.polyfit(list_selecao, pws_selecao, grau)
coef_angular = coeffs[0]
print('Coeficiente Angular:', coef_angular)
tendencia = np.poly1d(coeffs)
x_tendencia = np.linspace(min(list_selecao), max(list_selecao), 100)
plt.plot(x_tendencia, tendencia(x_tendencia), color='green', linestyle='dashed', label='Linha de Tendência Linear')
plt.plot(list_selecao, pws_selecao, marker='o', linestyle='', color='#D8A7FF', label='pws vs log(tp*delta t)/(tp+delta t)')
plt.xscale('symlog', linthresh=1)
plt.title('Linearização com Linha de Tendência')
plt.legend()
plt.xlabel('log(tp*delta t)/(tp+delta t)')
plt.ylabel('pws [ psia]')
plt.show()

# cálculo da permeabilidade:

k = 1.151 * (c2_americano*q*Bo*mi_o)/(abs(coef_angular)*h)
print('permeabilidade', k)

# cálculo do fator de película:

for i in range(len(delta_t)):
    j = delta_t[i]
    if j == 1.0094:
        p1 = pws[i]
    else:
        pass

s = 1.151*(((p1-pwf)/coef_angular) - (np.log10((k)/(phi*mi_o*ct*(rw**2)))) + 3.23)
print('s', s)

# cálculo do delta_ps:

delta_ps = 0.8686*coef_angular*s
print('delta_ps', delta_ps)

# cálculo do raio efetivo:

rwa = rw*np.exp(-s)
print('rwa', rwa)

