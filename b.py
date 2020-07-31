import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# data = pd.read_csv('Advertising.csv')
# X = data.values[:,2]
# y = data.values[:,4]
# plt.scatter(X,y,marker="o")
# plt.show()

# print("nguyen duc quyet")

data = pd.read_csv('cost_revenue_clean.csv')
# print(data.describe())
X = DataFrame(data, columns = ['production_budget_usd'])
y = DataFrame(data, columns = ['worldwide_gross_usd'])

# graph
plt.figure(figsize=(10,6))
plt.scatter(X, y, alpha=0.3)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('Production Budget (USD)')
plt.ylabel('Worldwide Gross (USD)')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
# plt.show()

regression = LinearRegression()
regression.fit(X, y)
x1= int(regression.coef_)
x0= int(regression.intercept_ )

n = 50000000
def predict(cost_input):
    print(cost_input)
    return cost_input*x1 + x0


print(predict(n)) 



