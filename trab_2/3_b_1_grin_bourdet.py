import numpy as np
import matplotlib.pyplot as plt
import math as mt
import pandas as pd
import scipy.special as sp
from Gavsteh_func import calculate_gavsteh
from gringbourdet_deriv import *

# informações da formação:

c1_americano = 0.0002637
tinj = 240 #hrs
qw = 807 # STB/D
pwf = 3582 #psia
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

list_delta_p = []
for i in range(len(pws)):
    delta_p = pwf - pws[i]
    list_delta_p.append(delta_p)
print('delta_p', list_delta_p)

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
print('derivada', derivate_p)

list_log_delta_p = []
list_log_delta_t = []
list_log_derivative_p = []
for i in range(len(list_delta_p)):
    delta_p_log = np.log10(list_delta_p[i])
    delta_t_log = np.log10(delta_t[i])
    list_log_delta_t.append(delta_t_log)
    list_log_delta_p.append(delta_p_log)
for i in range(len(derivate_p)):
    derivate_p_log = np.log10(derivate_p[i])
    list_log_derivative_p.append(derivate_p_log)
print('list_log_derivative_p', list_log_derivative_p)
print('list_log_delta_p', list_log_delta_p)

plt.plot(list_log_delta_t, list_log_delta_p, marker='o', markersize=2, linestyle='', color='#D5006D', label=r'$\log(\Delta p)$ vs. $\log(\Delta t)$')
plt.plot(list_log_delta_t, list_log_derivative_p, marker='o', markersize=2, linestyle='', color='#00FF00', label=r'$\log(\Delta p)$')
plt.xlabel(r'$\log(\Delta t)$')
plt.ylabel(r'$\log(\Delta p)$')
plt.title(r'Gráfico $\log(\Delta p)$ vs. $\log(\Delta t)$')
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
plt.ylabel(r'$p_D$ and $p_D(t_D/C_D)$')
plt.title('Solução Reservatório Infinito com Efeitos de Película e Estocagem')
#plt.xlim(9*10**1, 10**7)
#plt.ylim(0.2, 100)
plt.grid(color="gray", linestyle='--')

# translação:
list_delta_t_ajus = []
list_delta_p_ajus = []
list_derivative_p_ajus = []
for i in delta_t:
    delta_t_ajust = i*155
    list_delta_t_ajus.append(delta_t_ajust)
for i in list_delta_p:
    delta_p_ajus = i*0.017
    list_delta_p_ajus.append(delta_p_ajus)
for i in derivate_p:
    derivate_p_ajus = i* 0.017
    list_derivative_p_ajus.append(derivate_p_ajus)

plt.plot(list_delta_t_ajus, list_delta_p_ajus, marker='o', markersize=2, linestyle='', color='#D5006D')
plt.plot(list_delta_t_ajus, list_derivative_p_ajus, marker='o', markersize=2, linestyle='', color='#89CFF0')
plt.xscale('log',)
plt.yscale('log')
plt.show()

delta_t_match = delta_t[10]
tD_Cd_match = delta_t_match*155
delta_p_match = list_delta_p[10]
pD_match = delta_p_match*0.017

k = -((c2_americano*B_w*mi_w*-qw)/h) * (pD_match/delta_p_match)
print('k', k)

Cd = (c1_americano*k)/(phi*mi_w*ct*(rw**2)) * (delta_t_match/tD_Cd_match)
print('Cd', Cd)

s = 0.5 * np.log(1e4/Cd)
print('s', s)