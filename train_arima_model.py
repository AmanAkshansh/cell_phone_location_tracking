import pandas as pd
import matplotlib.pyplot as plt
## Loading the data
loc_data = pd.read_excel('C:/Users/aa0117/Desktop/Aman Job Change/Cellphone_tracking.xlsx') ## Curated data having historic data of past 100 time periods
latitude = loc_data['Latitude']
longitude = loc_data['Longitude']
timeperiod = loc_data['TimePeriod']

## Visualizing the cell phone movement in the historic data
plt.scatter(latitude,longitude)
plt.title("Historic Cell phone movement")
plt.show()

## Visualizing the location change w.r.t Time
def ts_viz(y,title):
    plt.plot(timeperiod,y)
    plt.title(title)
    plt.show()

ts_viz(y=latitude,title="Latitude Time Series") 
ts_viz(y=longitude, title="Longitude Time Series")

from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
import numpy as np

class cell_phone_movement_forecasting():
    
    def __init__(self, axis):
        self.axis = axis
        
    def stationarity_check(self):
        result = adfuller(self.axis)
        print('ADF Statistic: %f' % result[0])
        print('p-value: %f' % result[1])
        
    def plot_acf_pacf(self,plot_type):
        fig, axes = plt.subplots(1,2, sharex=True)
        axes[0].plot(self.axis); axes[0].set_title('Original Series')
        if plot_type == 'acf':
            plot_acf(self.axis, ax=axes[1])
        elif plot_type=='pacf':
            plot_pacf(self.axis, ax=axes[1])
        else:
            print("enter correct plot type argument")
        plt.show()
    
    def arima_fit(self, p,d,q):
        model= ARIMA(self.axis, order=(p,d,q))
        global model_fit
        model_fit = model.fit(disp=0)
        
        ## Generating the model summary
        print(model_fit.summary())
        
        ## Plotting the residuals density to see how well the model has performed
        residuals = pd.DataFrame(model_fit.resid)
        fig, ax = plt.subplots(1,2)
        residuals.plot(title="Residuals", ax=ax[0])
        residuals.plot(kind='kde', title='Density', ax=ax[1])
        plt.show()
        
        ## Plotting the Actual vs Predicted
        model_fit.plot_predict(dynamic=False)
        plt.show()
        
    
    def n_forecasting(self, start, end):
        return np.array(model_fit.predict(start=start, end=end))
      

## Instantiating the class with Latitude time series
x = cell_phone_movement_forecasting(axis=latitude)
x.stationarity_check()
x.plot_acf_pacf(plot_type='acf')
x.plot_acf_pacf(plot_type='pacf')
x.arima_fit(p=0,d=0,q=1) ## Chose the values of p,d,q using the acf, pacf plots and the result of Dickey fuller test
pred_latitude = x.n_forecasting(start=100,end=149) # Predicting future 50 latitude values

## Instantiating the class with LOngitude time series
y = cell_phone_movement_forecasting(axis=longitude)
y.stationarity_check()
y.plot_acf_pacf(plot_type='acf')
y.plot_acf_pacf(plot_type='pacf')
y.arima_fit(p=0,d=0,q=1)
pred_longitude = y.n_forecasting(start=100,end=149) # Predicting future 50 longitude values

## Creating a Dataframe with the predicted latitudes and longitudes
forecasted_locations = pd.DataFrame({'TimePeriod': range(100,150),
                   'predicted_latitude': pred_latitude,
                   'predicted_longitude': pred_longitude})
## This dataframe will be used for visualizing the future cell phone movements
