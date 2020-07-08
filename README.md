# Eigen Portfolios
After finishing MIT 18.06 on Linear Algebra, I wanted to put my new found knowledge to good use. I knew about the traditional approach of Markovitz mean-variance optimization, but I was curious to explore other approaches. This led me to attempt eigen decomposition/PCA on the basket of stocks contained within popular indices like DJI to create an optimized portfolio. The timeframe I will be using will be from 2000 onwards.

### Basic Visualisations
![](Images/DJI-Returns.png)
![](Images/DJI-Returns-Distribution.png)
We can observe here that returns may appear to follow a normal distribution but tend to have fatter tails.

### Eigen Decomposition/PCA
![](Images/Explained-Variance.png)
We see the decay happening quickly with the first few principal components explaining majority of the variance.
![](Images/Eigen-Portfolios.png)
This gives us a quick overview on all the principal components relative to DJI's overall price movement, with each principal component explaining a particular factor of the market. I am curious if there is way to identify the value and momentum factor.

## Results 
#### Best Portfolio Performance
![](Images/Portfolio-Performance.png)
![](Images/Eigen-Weights.png)

## Resources required to replicate findings
A dataframe containing prices of tickers that interest you.

## Disclaimer
All views and findings presented in my code or repository are my own and do not represent the opinions of any entity whatsoever with which I have been, am now, or will be affiliated. All material provided are for general information purposes only and do not constitute accounting, legal, tax, or other professional advice. Visitors should not act upon the content or information found here without first seeking appropriate advice from an accountant, financial planner, lawyer or other professional. Usage of any material contained within this repository constitutes an explicit understanding and acceptance of the terms of this disclaimer. 
