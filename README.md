## EDA
Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.

## #1 Example
* Heatmap - averages of absolute percentage change of price in trading day of the month in last 20 years. Clearly visible the most volatile month of the year is October and very little price change during second half of the December.
```python
df = df.pivot("DoM", "M", "Pabs")
sns.heatmap(df, annot=True, cmap="YlGnBu", fmt='.3g')
# sns.heatmap(df, mask=df > 0.8, cbar=False)
plt.show()
```
![SPX heatmap](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/000_Heatmap_DoM_v_M_Pabs.png)

## #2 Example
* Linechart - SPX corrections from All time highs in % from 1962 to 2020. 
![ATH corr](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/010_ATH_1962-2020.png)

## #3 Example
* Histogram - Distribution of ONp ranges during last 15 year for S&P 500 futures. 
![ATH corr](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/016_ONp%20histogram.png)
