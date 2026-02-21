import numpy as np

def f(x):
    f1=x[0]**2+x[1]
    f2=np.sin(x[0]*x[1])
    return np.array([f1, f2])

x_alvo=np.array([1.0,2.0])
h=1e-5 #valor infinitesinal

jacobiana = np.zeros((2,2))

for i in range(len(x_alvo)):
    x_perturbado= x_alvo.copy()
    x_perturbado[i] += h

    deriv_parcial= (f(x_perturbado)-f(x_alvo))/h

    jacobiana[:,i]=deriv_parcial


print(jacobiana)

