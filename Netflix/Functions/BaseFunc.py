import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from datetime import datetime as dt

# Importing the Netfllix dataset
df = pd.read_csv("https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/000/940/original/netflix.csv")
df.info()

movies_data=df.loc[df["type"]=="Movie"].reset_index()
movies_data_plot=movies_data.groupby(["release_year"])["type"].count()

# Creating a sample line plot
plt.figure(figsize=(20,5))
movies_data_plot.plot(kind="line")