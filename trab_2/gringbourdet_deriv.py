import numpy as np

def deriv_bourdet(pD_Cd_list, CDe2s, tD):
    p = pD_Cd_list
    derivative_bourdet = []
    for i in range(len(CDe2s)):
        deriv_tD = []
        for k in range((len(tD) - 1)):
            deriv_tD.append(tD[k] * (p[i][k+1] - p[i][k])/((max(tD) - min(tD)) / len(tD)))
        derivative_bourdet.append(deriv_tD)
    return derivative_bourdet
