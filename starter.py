import matplotlib
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


input_data = np.array([
    [0,0],
    [.25,.25],
    [0.5,0.5],
    [1,1]
])

output_data = np.array([
    0,
    0,
    1,
    1
])

model = LogisticRegression()
model.fit(input_data,output_data)
print(model.coef_)
print(model.intercept_)
pred = model.predict(input_data)
print(pred)

plt.scatter(
    x=input_data[:,0],
    y=output_data,
    color =['blue' if x==1 else 'red' for x in output_data]
)
plt.title('SHOw')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()



plt.scatter(
    x=input_data[:,0],
    y=input_data[:,1],
    color =['blue' if x==1 else 'red' for x in pred]
)
plt.title('SHOw')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()