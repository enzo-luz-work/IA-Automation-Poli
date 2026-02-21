import numpy as np

vector_a=np.random.rand(1000)

vector_b=np.random.rand(1000)

dif=vector_a-vector_b
dist=np.sqrt(np.dot(dif, dif))
print(dist)


