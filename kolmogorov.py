import scipy.stats as stats
import numpy as np
y = np.array([389, 387., 388.1, 388.6, 387.9, 388.3, 387.2, 388.5, 387.7, 388, 389.8, 387.4, 387.5, 397.1, 387.6, 387.5, 387.9, 388.6, 387.5, 389.3, 387.6, 386.8])

media= np.mean(y)
print(media)
std = np.std(y, ddof=1)
print(std)

ks_stat, ks_p_valor = stats.kstest(y, cdf='norm', args=(media, std), N = len(y))
print(ks_stat)
print(ks_p_valor)

