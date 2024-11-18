import numpy as np
import matplotlib.pyplot as plt


tinj = 240 #hrs
qw = 807 # STB/D
pwf = 2788 #psia
mi_w = 1 # cp
B_w = 1 # RB/STB
ct = 1.18*10**-5 # psia^-1
phi = 0.25
h = 28 # ft
rw = 0.4 # ft
depth = 4819 # ft
A = 871200 # ft²
c2_americano = 141.2

delta_t = [0.01, 0.015, 0.02, 0.03, 0.04, 0.06,
     0.08, 0.10, 0.1501,
     0.2002, 0.3004, 0.4007,
     0.6015, 0.8027, 1.0042, 2.0168,
     4.0678, 6.1538, 8.2759, 10.435]

pws = [3500, 3470, 3442, 3397,3362, 3317, 3282,
       3257, 3216, 3187, 3155, 3137, 3112, 3091,
       3075, 3042, 3007, 2982, 2972, 2962]

plt.plot(delta_t, pws, marker='o', linestyle='', color='#D5006D', label=r'$p_{ws}$ vs. $\Delta t$')
plt.xlabel(r'$\Delta t$')
plt.ylabel(r'$p_{ws}$')
plt.title(r'$P_{ws}$ vs. $\Delta t$')
plt.legend()
plt.show()

list_eixo_x = []
for i in range(len(delta_t)):
    eixo_x = (tinj+delta_t[i])/delta_t[i]
    list_eixo_x.append(eixo_x)

print('x', list_eixo_x)
list_log_eixo_x = []
for j in range(len(list_eixo_x)):
    log_eixo_x = np.log10(list_eixo_x[j])
    list_log_eixo_x.append(log_eixo_x)
print('log', list_log_eixo_x)

plt.semilogx(list_log_eixo_x, pws, marker='o', linestyle='', color='#D8A7FF', label=r'$p_{ws}$ vs. $\log\left(\frac{t_{inj} + \Delta t}{\Delta t}\right)$')
plt.xlabel(r'$\log\left(\frac{t_{inj} + \Delta t}{\Delta t}\right)$')
plt.ylabel(r'$p_{ws}$')
plt.title(r'Gráfico de $p_{ws}$ vs. $\log\left(\frac{t_{inj} + \Delta t}{\Delta t}\right)$')
plt.legend()
plt.show()

list_selecao = [ 2.079182681634575, 1.778150894503594, 1.6020631671185683,  1.4771193305583894, 1.3802025709957204]
print(len(list_selecao))
pws_selecao = [3042, 3007, 2982, 2972, 2962]
print(len(pws_selecao))

# ajustando uma linha de tendência no gráfico semilog:
grau = 1
coeffs = np.polyfit(list_selecao, pws_selecao, grau)
coef_angular = coeffs[0]
print('Coeficiente Angular:', coef_angular)
tendencia = np.poly1d(coeffs)
x_tendencia = np.linspace(min(list_selecao)*0.9, max(list_selecao)*1.8, 100)
plt.plot(x_tendencia, tendencia(x_tendencia), color='green', linestyle='dashed', label='Linha de Tendência Linear')
plt.semilogx(list_log_eixo_x, pws, marker='o', linestyle='', color='#D8A7FF', label=r'$p_{ws}$ vs. $\log\left(\frac{t_{inj} + \Delta t}{\Delta t}\right)$')
plt.title('Linearização com Linha de Tendência')
plt.legend()
plt.xlabel(r'$\log\left(\frac{t_{inj} + \Delta t}{\Delta t}\right)$')
plt.ylabel(r'$p_{ws}$]')
plt.show()

# cálculo da permeabilidade:

k = -1.151 * (c2_americano*-qw*B_w*mi_w)/(abs(coef_angular)*h)
print('permeabilidade', k)

# cálculo do fator de película:

for i in range(len(delta_t)):
    j = delta_t[i]
    if j == 1.0042:
        p1 = pws[i]
    else:
        pass

s = 1.151*(((pwf-p1)/coef_angular) - (np.log10((k)/(phi*mi_w*ct*(rw**2)))) + 3.23)
print('s', s)

# cálculo do delta_ps:

delta_ps = 0.8686*coef_angular*s
print('delta_ps', delta_ps)

# cálculo do raio efetivo:

rwa = rw*(np.exp(-s))
print('rwa', rwa)




