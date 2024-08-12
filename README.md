# Facebook-campaign-analysis-with-recommendations.

## The goal of this project is to investigate the performance of Facebook marketing campaigns and surface recommendations for future budget allocation across all campaigns, with a focus on maximizing sales conversions through social media advertising.

## Data Cleaning & Exploratory Data Analysis

Identify any missing values and analyze the correlation between key metrics and selected dimensions. For more details, click [here](https://github.com/WittsMei/Facebook-campaign-analysis-with-recommendations./blob/main/Facebook%20Campaign%20Data%20Cleaning.ipynb).

<img width="926" alt="image" src="https://github.com/user-attachments/assets/cfa54645-d6a4-46bb-828b-2df8eea5fabb">




## North Star Metics and Dimensions
- **Conversion & Cost**: Avg purchase (Avg Approved Conversion), Avg spent, CPA (Cost per Acquisition)
- **Gender Targeting**: Male, Female
- **Age Targeting**: 30-34, 35-39, 40-44, 45-49
- **Interest Targeting**: a code specifying the category to which the person’s interest belongs (interests are as mentioned in the person’s Facebook public profile)



## Summary of Insights

### Gender Targeting
- While the female audience segment generated higher impressions, clicks, and inquiries (Total Conversion), the male segment achieved nearly equal Approved Conversions (purchases). This suggests that males may have a higher conversion rate from inquiry to purchase.


### Interest Targeting
- Across all campaigns, the interests with codes 101, 29, 16, 15, and 107 drove the highest Approved Conversions. Focusing more ad spend on these interest segments could yield a higher return on investment.

### Age Targeting
- The 45-49 age group had the highest number of ad clicks. 
- Despite allocating the highest ad spend to the 45-49 age group, the 30-34 age segment delivered almost twice as many Approved Conversions. Reallocating a larger portion of the budget towards the 30-34 age group could be more cost-effective.
  
### Gender Conversion Rates
- The data indicates that male audiences from the campaign_c campaign tend to convert to actual purchases at a higher rate compared to females.

## Recommendations & Next Step
- Optimize gender targeting by maintaining strong exposure to both male and female audiences, but prioritize males for conversion campaigns or retargeting efforts.
- Consider reallocating ad spend by removing it from interest segments 7, 8, 19, 24, 25, 30, 63, and 65 under Campaign A, which have near-zero purchases. Additionally, reduce ad spend in interest segment 20 under Campaign A, segments 22 and 27 under Campaign B, and segments 22 and 23 under Campaign C due to their relatively low cost-efficiency. Redirect these funds to the top-performing interest segments (101, 29, 16, 15, and 107) to enhance cost-efficient conversions.
- Gradually shift a larger portion of the age-based ad budget from the 45-49 segment to the 30-34 segment, which has proven to be more effective in driving purchases.
- Conduct further analysis on the customer journey and messaging resonance to understand why males exhibit higher purchase conversion rates and leverage those insights for campaign optimization.
- Implement ongoing campaign monitoring and optimization based on real-time performance data to continually refine audience targeting and messaging for maximum cost efficiency and return on ad spend.


## Dashboard

The dashboard can be found in Tableau Public [here](https://public.tableau.com/app/profile/witts.jianming.mei/viz/FacebookCampaignPerformanceDsahboard/FacebookadsPerformanceDashboard?publish=yes).
