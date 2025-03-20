import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from scipy.stats import linregress, pearsonr


tillage_file = "/Users/yangyangxiayule/Documents/GitHub/Geospatial-Technologies/Tillage.xlsx"
waste_file = "/Users/yangyangxiayule/Documents/GitHub/Geospatial-Technologies/Waste.xlsx"

tillage_data = pd.ExcelFile(tillage_file)
waste_data = pd.ExcelFile(waste_file)

# Task 1: Model of Soil C Stocks under Reduced Tillage
# Load fitting data
tillage_fitting = tillage_data.parse("fitting")
print(tillage_fitting.columns)

tillage_fitting.rename(columns={'Soil C stocks under conventional tillage (t C ha-1 to 30cm) ': 'Conventional Tillage','Soil C stocks under reduced tillage           (t C ha-1 to 30cm)': 'Reduced Tillage' }, inplace= True)
print(tillage_fitting.columns)

tillage_fitting["Change_in_Soil_C"] = tillage_fitting["Reduced Tillage"] - tillage_fitting["Conventional Tillage"]
tillage_fitting["Annual_Change_in_Soil_C"] = tillage_fitting["Change_in_Soil_C"] / tillage_fitting["Duration (y)"]
#display(tillage_fitting)

# Calculate mean annual change
mRT = tillage_fitting["Annual_Change_in_Soil_C"].mean()
print(mRT)

# Model testing
tillage_testing = tillage_data.parse("testing")
#print(tillage_testing.columns)
tillage_testing.rename(columns={'Soil C stock under conventional tillage (t C ha-1 to 30cm) ': 'Conventional Tillage', 'Measured soil C stock after 10 years reduced tillage                               (t C ha-1 to 30cm) ': 'Reduced Tillage'}, inplace=True)
tillage_testing["Predicted_CRT"] = tillage_testing["Conventional Tillage"] + mRT * 10
#display(tillage_testing)

r, p_value = pearsonr(tillage_testing["Reduced Tillage"], tillage_testing["Predicted_CRT"])
print(f"Pearson's r: {r}, P-value: {p_value}")

# Scatter plot
plt.figure(figsize=(6, 6))
sns.scatterplot(x=tillage_testing["Reduced Tillage"], y=tillage_testing["Predicted_CRT"])
plt.plot([tillage_testing["Reduced Tillage"].min(), tillage_testing["Reduced Tillage"].max()],
         [tillage_testing["Reduced Tillage"].min(), tillage_testing["Reduced Tillage"].max()],
         linestyle="--", color="red")
plt.xlabel("Measured CRT")
plt.ylabel("Modelled CRT")
plt.title("Measured vs Modelled CRT under Reduced Tillage")
plt.show()

# Model predictions
tillage_predicting = tillage_data.parse("predicting")
print(tillage_predicting.columns)
tillage_predicting.rename(columns={'Unnamed: 0': 'Sector Name', 'Present Soil Carbon Stock (tonnes C )': 'Carbon Stock','Arable Area (ha)': 'Arable Area'}, inplace= True)


for t in [10, 20, 30, 40, 50]:
    tillage_predicting[f"CRT_{t}_years"] = tillage_predicting["Carbon Stock"] + mRT * t



# Task 2: Model of Soil C Stocks under Organic Waste Application
waste_fitting = waste_data.parse("fitting")
print(waste_fitting.columns)

waste_fitting["Change_in_Soil_C"] = waste_fitting["With Waste"] - waste_fitting["Without Waste"]
waste_fitting["Annual_Change_in_Soil_C"] = waste_fitting["Change_in_Soil_C"] / waste_fitting["Years"]

# Regression analysis
slope, intercept, r_value, p_value, std_err = linregress(waste_fitting["Waste Application Rate"], waste_fitting["Annual_Change_in_Soil_C"])

# Model testing
waste_testing = waste_data.parse("testing")
waste_testing["Predicted_CW"] = waste_testing["Without Waste"] + (slope * 20 + intercept) * 50

# Predictions
waste_predicting = waste_data.parse("predicting")
for t in range(10, 110, 10):
    waste_predicting[f"CW_{t}_years"] = waste_predicting["Initial Soil C"] + (slope * waste_predicting["Waste Application Rate"] + intercept) * t

# Plot soil C stock trends
plt.figure(figsize=(10, 6))
for sector in waste_predicting["Sector"].unique():
    sector_data = waste_predicting[waste_predicting["Sector"] == sector]
    plt.plot(range(10, 110, 10), sector_data.iloc[0, 2:].values, label=f"Sector {sector}")
plt.xlabel("Years")
plt.ylabel("Soil C Stock (t C ha-1)")
plt.title("Soil C Stock Predictions under Organic Waste Application")
plt.legend()
plt.show()
