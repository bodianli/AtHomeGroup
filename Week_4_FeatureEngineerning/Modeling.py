import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import math
import sklearn.metrics as sklm
import sklearn.model_selection as GridSearchCV
from sklearn.linear_model import Ridge
import sklearn.model_selection as ms

sale_2017 = pd.read_csv("../Week_4_FeatureEngineerning/2017_Sale.csv")

sale_2017[['Pickup_InStore', 'Pickup_Curbside', 'Local_Delivery']] = sale_2017[
    ['Pickup_InStore', 'Pickup_Curbside', 'Local_Delivery']].fillna(0)

sale_2017.dropna(subset=['2017_sale'], inplace=True)
# print (sale_2017.shape)

cols_input = [
    "Pickup_InStore",
    "Pickup_Curbside",
    "Local_Delivery",
    "POPESTIMATE2017",
    "NPOPCHG_2017",
    "BIRTHS2017",
    "DEATHS2017",
    "NATURALINC2017",
    "INTERNATIONALMIG2017",
    "DOMESTICMIG2017",
    "NETMIG2017",
    "RESIDUAL2017",
    "RBIRTH2017",
    "RDEATH2017",
    "RNATURALINC2017",
    "RINTERNATIONALMIG2017",
    "RDOMESTICMIG2017",
    "RNETMIG2017",
    "2017_sale"
]

print (sale_2017[cols_input].isnull().sum())


x_train, x_test, y_train, y_test = train_test_split(sale_2017[cols_input],
                                                    sale_2017['2017_sale'],
                                                    test_size=.3,
                                                    random_state=42)
X_train_all = sale_2017[cols_input]
print (x_train.shape)
print (x_test.shape)

print (X_train_all.shape)
# Scalar the dataset

scaler  = StandardScaler()
scaler.fit(X_train_all)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)





#
# # Using RMSE as evaluation
# def score(y_pred):
#     return str(math.sqrt(sklm.mean_squared_error(y_test, y_pred)))
#
#
# # Ridge Regresssion
# ridge = Ridge()
# parameters = {'alpha': [x for x in range(1, 101)]}
#
# ridge_reg = ms.GridSearchCV(ridge, param_grid=parameters, scoring='neg_mean_squared_error', cv=15)
# ridge_reg.fit(x_train, y_train)
# print("The best value of Alpha is: {}".format(ridge_reg.best_params_))
# print("The best score achieved with Alpha=11 is: {}".format(math.sqrt(-ridge_reg.best_score_)))
# ridge_pred = math.sqrt(-ridge_reg.best_score_)
#
#
#
# ridge_mod=Ridge(alpha=18)
# ridge_mod.fit(x_train,y_train)
# y_pred_train=ridge_mod.predict(x_train)
# y_pred_test=ridge_mod.predict(x_test)
#
# print('Root Mean Square Error train =  {}'.format(str(math.sqrt(sklm.mean_squared_error(y_train, y_pred_train)))))
# print('Root Mean Square Error test =  {}'.format(score(y_pred_test)))
