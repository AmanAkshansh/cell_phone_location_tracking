# Cell Phone location tracking

## Objective: - 

The objective of this project is to create a process that can predict the movement of an Individual using his/her historic cell phone location data.

## End Results: -

(i) Generation of location predictions for future 'n' time periods.

(ii) Creation of an animated graph that shows the movement of the individual concerned over the next 'n' time periods.

## Data Used: -

For this project, manually curated data has been used. The data contains historic cell phone locations tracked over the past 100 time periods.
The dataset contains following three columns:

a) TimePeriod - The time period at which the location data had been tracked

b) Latitude - Latitude of the locations

c) Longitude - Longitude of the locations

## Methods used/Steps performed: -

i) Created a scatter plot to visualize the cell phone locations in the historic data.

ii) Generated line plots to visualize both Latitude and Longitude w.r.t Time periods to check if there is any pattern/trend in the movement.

iii) Performed Dicky fuller test for both longitudes and latitudes series to check their stationarity.

iv) Then, plotted Auto Correlation plots (ACF) and Partial Auto Correlation plots (PACF) for both Latitudes and Longitudes in order to determine the orders of Auto regression (p) and Moving averages (q).

v) After determining the values of p,d and q for latitudes and longitudes time series, trained ARIMA model on both the series.

vi) ARIMA model has been used because there is no seasonality in the data.

vii) The trained ARIMA model has been then used to predict the cell phone location's latitudes and longitudes for future n time periods.

viii) Finally the forecasted locations have been plotted and visualized through an animated graph.

## Resources Used: -

Multiple resources have been referred to for the end-to-end completion of this project. The most notable ones are mentioned below: -

### 1. https://www.nytimes.com/interactive/2019/12/19/opinion/location-tracking-cell-phone.html

I have read this article to understand the actual problem statement. Reading the article also helped me in deciding the final solution methodology.

### 2. https://www.kaggle.com/c/recruit-restaurant-visitor-forecasting/data?select=air_store_info.csv.zip

I have gone through this kaggle dataset to see how a location dataset looks like. I have also used this data as a reference to create my own data for this project.

### 3. https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/
### 4. https://towardsdatascience.com/arima-forecasting-in-python-90d36c2246d3
### 5. https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/

The resources 3,4 and 5 have been used to learn about Time series analysis and Arima Forecasting. I hadn't performed time series analysis on real data/problem since 2 years and because of that I felt like a complete beginner when I started working on this project.
After going through the above resources, I learned about the application of time series and the various algorithms/techniques needed to perform its analysis.
I have also taken some code blocks from these resources for both training the models and visualizing the results.

### 6. https://holypython.com/python-visualization-tutorial/guide-to-python-animations-animating-line-charts/
### 7. https://github.com/kirthitej/Animation/blob/master/Sinewave-matplotlib

I have used resources 6 and 7 to learn the Python animations in detail. The resource 7 is a public github repository and it contains the code for the generation of an animated graph that traces a sinusoidal wave through a red dot. I have used this code file as a reference when I created my animated locations graph.

# Note: - Please do open the 'train_arima_model.py' file first before opening the animated graph code file.

