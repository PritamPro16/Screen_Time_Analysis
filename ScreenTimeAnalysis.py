# Screen Time Analysis is the task of analysis and creating a report on which applications and websites are used by the user for how much time. Apple devices have one of the best ways of creating a screen time report.
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screentime-App-Details.csv")
#print(data.head())
#print(data.isnull().sum())
#print(data.describe())

'''# Usage
figure = px.bar(data_frame=data, x="Date", y="Usage", color="App", title = "Usage Graph by Pritam Das")
figure.show()

# Notification
figure1 = px.bar(data_frame=data, x="Date", y="Notifications", color="App", title = "Notifications Graph by Pritam Das")
figure1.show()

# Time opened
figure1 = px.bar(data_frame=data, x="Date", y="Time opened", color="App", title = "Time opened Graph by Pritam Das")
figure1.show()'''

figure = px.scatter(data_frame=data, x="Notifications", y="Usage", size="Notifications", trendline="ols", color="App", title = "Relationship Between Number of notification and amount of usage")
figure.show()