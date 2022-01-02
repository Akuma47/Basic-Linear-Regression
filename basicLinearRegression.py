
from typing import Tuple


# database
x = [2,4,6,8,10,12,14]
y = [4,8,12,16,20,24,28] # Dobro do numero 

epochs = 10
m = 0.1
b = 0.1
lr = 0.01

for i in range(epochs):

    print('Epoch: ', i)
    for j in range(len(x)):
        xi = x[j]
        yi = y[j]


        y_hat = m*xi+b


        error = y_hat - yi
        print(error)

        m = m - (lr * error * xi)
        b = b - (lr * error)



run = True
while run:
    n = int(input('> '))
    print(round(m*n+b))
    print('')













