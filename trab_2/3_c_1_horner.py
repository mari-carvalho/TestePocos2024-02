import numpy as np
import matplotlib.pyplot as plt
import math as mt
import pandas as pd

pwf = 3535 #psia
mi_o = 0.75 # cp
B_o = 1.25 # RB/STB
ct = 2.4*10**-5 # psia^-1
phi = 0.20
h = 50 # ft
rw = 0.50 # ft
c2_americano = 141.2

q = [450, 600, 500]
t_q = [7, 4, 10]

delta_t = [0.25, 0.50, 1.0, 1.50, 2, 3, 4, 7, 10, 15,24]

pws = [3605, 3632, 3795, 3960, 4230, 4320, 4370, 4390, 4395, 4410, 4422]

delta_te = [2026.60, 1013.80, 507.40, 338.60, 254.20, 169.80, 127.60, 73.34, 51.64, 34.76, 22.10]

plt.plot(delta_t, pws, marker='o', linestyle='', color='#D5006D', label=r'$p_{ws}$ vs. $\Delta t$')
plt.xlabel(r'$\Delta t$ [h]')
plt.ylabel(r'$p_{ws}$ [psia]')
plt.title(r'$P_{ws}$ vs. $\Delta t$')
plt.legend()
plt.show()

for i in range(len(q)):
    tpH = (24*((450*7) + (600*4) + (500*10)))/(500)
print('tpH', tpH)

list_log_eixo_x = np.log10(delta_te)
print('log', list_log_eixo_x)

plt.semilogx(list_log_eixo_x, pws, marker='o', linestyle='', color='#D8A7FF', label=r'$p_{ws}$ vs. $\log\left(\frac{t_{pH} + \Delta t}{\Delta t}\right)$')
plt.xlabel(r'$\log\left(\frac{t_{pH} + \Delta t}{\Delta t}\right)$')
plt.ylabel(r'$p_{ws}$ [psia]')
plt.title(r'Gráfico de $p_{ws}$ vs. $\log\left(\frac{t_{pH} + \Delta t}{\Delta t}\right)$')
plt.legend()
plt.show()

list_selecao = [2.40517555, 2.22993769, 2.10585067]
print(len(list_selecao))
pws_selecao = [4230, 4320, 4370]
print(len(pws_selecao))

# ajustando uma linha de tendência no gráfico semilog:
grau = 1
coeffs = np.polyfit(list_selecao, pws_selecao, grau)
coef_angular = coeffs[0]
print('Coeficiente Angular:', coef_angular)
tendencia = np.poly1d(coeffs)
x_tendencia = np.linspace(min(list_selecao), max(list_selecao), 100)
plt.plot(x_tendencia, tendencia(x_tendencia), color='green', linestyle='dashed', label='Linha de Tendência Linear')
plt.semilogx(list_selecao, pws_selecao, marker='o', linestyle='', color='#D8A7FF', label=r'$p_{ws}$ vs. $\log\left(\frac{t_{pH} + \Delta t}{\Delta t}\right)$')
plt.title('Linearização com Linha de Tendência')
plt.legend()
plt.xlabel(r'$\log\left(\frac{t_{pH} + \Delta t}{\Delta t}\right)$')
plt.ylabel(r'$p_{ws}$ [psia]')
plt.show()

# cálculo da permeabilidade:

k = -1.151 * (c2_americano*500*B_o*mi_o)/(abs(coef_angular)*h)
print('permeabilidade', k)

# cálculo do fator de película:

for i in range(len(delta_t)):
    j = delta_t[i]
    if j == 1.0:
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