## EDA
Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns, to spot anomalies, to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.

## #1 Example
* Heatmap - averages of absolute percentage change of price by trading day of the month for last 20 years. Clearly visible the most volatile month of the year is October and very little price change occures during second half of the December.
```python
df = df.pivot("DoM", "M", "Pabs")
sns.heatmap(df, annot=True, cmap="YlGnBu", fmt='.3g')
# sns.heatmap(df, mask=df > 0.8, cbar=False)
plt.show()
```
![SPX heatmap](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/000_Heatmap_DoM_v_M_Pabs.png)

* Volume Heatmap - supports the first observation and shows clearly that December is very light in terms of volume traded.

![SPX2 heatmap](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/012_heatmap_volume.png)

## #2 Example
* Linechart - SPX corrections from ATHs in % from 1962 to 2020. 

![ATH corr](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/010_ATH_1962-2020.png)

## #3 Example
* Histogram - Distribution of ONp ranges during last 15 year for S&P 500 futures. 

![ATH corr](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/016_ONp%20histogram.png)

## #4 Example
* Linechart - Markers showing +1% days related to percentage distance from ATHs. 

![ATH corr](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/017_ath%20lines%20plus%20big%20moves%20(2020).png)

## #5 Example
* Rollover impact on open interest over the last 18 months (2020). 

![Roll](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/009_OIChange%20detailed.png)

## #6 Example
* Globex gaps sizes and frequency of occurence (1962-2020). 

![Gaps](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/014_gap_size%201962-2020.png)

## #7 Example
* Mplfinance library - great library for visualisation of OHLC (candlestick, bar) charts. 

![mpl](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/008_mplfinance_print.png)

## #8 Example
* Daily lines chart for visual comparation of stock market crashes confirms 3rd Quarter seasonall weakness even during outlier years.

![crash](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/007_crashes.png)

## #9 Example
* Histogram - Category "C" is the most common from dataset, representing almost 28% of the data.

![hist](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/008_Y_Wiwo_week_types.png)

## #10 Example
* lmplot - VIX change vs SPX change - daily closing prices, hue = UP/DOWN days.

![hist](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/018_SPXvsVIX.png)

