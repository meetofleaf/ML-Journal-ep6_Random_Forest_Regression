# Random Forest Regression

#### Import Default Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#### Data Preparation
dataset = pd.read_csv("petrol_consumption.csv")

X = dataset.iloc[:,1:2].values     # Average income
y = dataset.iloc[:,-1].values      # Petrol consumption
#plt.scatter(X,y)


#### Train the model
from sklearn.ensemble import RandomForestRegressor

# We train our model with RandomForestRegressor class and fit method
regressor = RandomForestRegressor(n_estimators=10, random_state=0)  # random_state adds a dash of randomness to how the trees of the forest are built, but it doesn't significantly affect the final predictions (variable value and randomness are inversely proportional)
                                                                    # For more parameters explore: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
regressor.fit(X,y)


#### Predicting Results
# We define a simple function to predict the dependent variable for code reusability
def predict(model, inputs):
    return model.predict(inputs)

predict(regressor, [[15]])    # average_income


#### Visualization

X_grid = np.arange(min(X), max(X), 0.1)
y_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X,y, color='red')
plt.plot(X_grid, regressor.predict(X_grid.reshape(-1, 1)), color='blue')
plt.xlabel('Average Income')
plt.ylabel('Petrol Consumption')
plt.show()
