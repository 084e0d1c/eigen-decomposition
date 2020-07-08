# Eigen Portfolios
After finishing MIT 18.06 on Linear Algebra, I wanted to put my new found knowledge to good use. I knew about the traditional approach of Markovitz mean-variance optimization, but I was curious to explore other approaches. This led me to attempt Eigenvalue decomposition on the basket of stocks contained within popular indices like DJI and S&P500 to create an optimized portfolio. 

## Results 
#### Cumulative Performance
![](Images/cumulative_performance.png)

#### Non-cumulative Performance
![](Images/non_cumulative_performance.png)

#### Observations
1. The top 10% and bottom 10% of stocks appear to be inversely related between 2018-06 to 2019-01.
2. When we factor in transaction costs (spreads & fx), even if we only go long, the returns will be significant less than SPY. 
3. The strategy is missing key growth stocks (due to unavailable data) that have contributed to SPY's performance and thus when we include them, the results could change drastically. (Refer to Appendix A)

Does the strategy work? Yes, but one would be far better off passively holding SPY. :sweat_smile:

## Resources required to replicate findings
A dataframe containing prices of tickers that interest you.

## Disclaimer
All views and findings presented in my code or repository are my own and do not represent the opinions of any entity whatsoever with which I have been, am now, or will be affiliated. All material provided are for general information purposes only and do not constitute accounting, legal, tax, or other professional advice. Visitors should not act upon the content or information found here without first seeking appropriate advice from an accountant, financial planner, lawyer or other professional. Usage of any material contained within this repository constitutes an explicit understanding and acceptance of the terms of this disclaimer. 
