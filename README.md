## EDA
Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns, to spot anomalies, to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.

## #1 EOD Heatmap
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

## #2 ATH corrections
* Linechart - SPX corrections from all time highs in % from 1962 to 2020.

![ATH corr](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/010_ATH_1962-2020.png)

## #3 ON range
* Histogram - Distribution of ONp ranges during last 15 year for S&P 500 futures. 

![ATH corr](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/016_ONp%20histogram.png)

## #4 Rollover impact
* Futures rollover impact on open interest over the last 18 months (2020) in spooz shows rolling over all the volume to new contract took about 6-8 trading days on average. 

![Roll](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/009_OIChange%20detailed.png)

## #5 ES ON Gaps
* ES RTH only data shows (globex) gaps sizes and frequencies of occurence (1962-2020). 

![Gaps](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/014_gap_size%201962-2020.png)

## #6 OHLC plot
* Mplfinance library - great library for visualisation of OHLC (candlestick, bar) charts. 

![mpl](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/008_mplfinance_print.png)

## #7 Crashes
* Daily lines chart for visual comparation of stock market crashes confirms 3rd Quarter seasonall weakness even during outliers years.

![crash](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/007_crashes.png)

## #8 Day types OHLC
* Histogram - Day types - Type "C" is the most common from dataset, representing almost 28% of the data.

![hist](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/008_Y_Wiwo_week_types.png)

## #9 VIX/SPX
* lmplot - VIX change vs SPX change - daily closing prices, hue = UP/DOWN days.

![hist](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/018_SPXvsVIX.png)

## #10 ES corrections
* Heatmap - ES futures over 10 years period - number of trading days each month in 5% correction or lower.

![hist](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/019_below_5.png)

## #11 ES distribution
* Histogram & Boxplot - "About 68% of values drawn from a normal distribution are within one standard deviation σ away from the mean; about 95% of the values lie within two standard deviations; and about 99.7% are within three standard deviations." ES futures daily %change ETH, 2010-2019 - median -0.07, 1σ -0.76, 0.62, 2σ -1.82, 2.06.
```python
n, bins, patches = axes[1].hist(s, n_bins, density=True, stacked=True, alpha=.1, edgecolor='black')
pdf = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2))

median, q1, q3 = np.percentile(s, 50), np.percentile(s, 25), np.percentile(s, 75)
s1, s1b, s2, s2b = np.percentile(s, 15.9), np.percentile(s, 84.1), np.percentile(s, 2.3), np.percentile(s, 97.7)
```

![hist](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/020_ES_pdf.png)

## #12 ATH moves
* Visualization of large absolute moves (> 1%) based on distance from all time high (ATH).

![hist](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/015_ath%20lines%20plus%20big%20moves%20(1960).png)

## #13 ES HoDLoD types
* ES HoDLoD classification (4 types, 2 classes).

![hist](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/021_ES_fades.png)

## #14 ES seasonality (M)
* ES Monthly seasonality with one sigma confidence interval.

![conf](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/022_confidence_interval.png)

## #15 CL IB rng
* CL IB pRNG vs RTH_LC pRNG with period 10 simple moving average.

![IBv](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/023_CL_IBvLCRNG.png)

## #16 ES RTH
* ES RNG in RTH. Power BI - Chord (A graphical method of displaying the inter-relationships between data in a matrix).

![IBv](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/099_powerbi_chord_prng.PNG)

## #17 ES trend
* ES stacked Bar chart visualizing trend of cparts.

![IOUTv](https://github.com/vldmrmrv/ES-Exploratory-Data-Analysis-DataScience/blob/main/EDA_charts/024_cpart_es_outlier.png)

## #18 CL EOD HoMLoM
* CL HoMLoM (2013-2022).

![cl_00](https://github.com/vldmrmrv/ES-studies-sample-DataScience/blob/main/016_cl_hodlod_dom.png)
