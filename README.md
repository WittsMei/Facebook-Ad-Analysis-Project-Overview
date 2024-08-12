# Facebook-campaign-analysis-with-recommendations.

## The goal of this project is to investigate the performance of Facebook marketing campaigns and surface recommendations for future budget allocation across all campaigns, with a focus on maximizing sales conversions through social media advertising.

## Data Cleaning & Exploratory Data Analysis

Identify any missing values and analyze the correlation between key metrics and selected dimensions. For more details, click [here](https://github.com/WittsMei/Facebook-campaign-analysis-with-recommendations./blob/main/Facebook%20Campaign%20Data%20Cleaning.ipynb).

<img width="926" alt="image" src="https://github.com/user-attachments/assets/ba84e0cf-9ac5-4b33-bcac-68bcdeba184c">





## Dashboard

The dashboard can be found in Tableau Public [here](https://public.tableau.com/app/profile/witts.jianming.mei/viz/FacebookCampaignPerformanceDsahboard/FacebookadsPerformanceDashboard?publish=yes). This dashboard enables users to filter by age group, campaign type, gender, and interest, and focuses on values in marketing metrics, purchase metrics, and claim metrics.


<img width="1071" alt="image" src="https://github.com/user-attachments/assets/8da11632-7dac-41ca-a9c4-2feaabf7df5c">





## North Star Metics and Dimensions
- **Conversion & Cost**: Avg purchase (Avg Approved Conversion), Avg spent, CPA (Cost per Acquisition)
- **Gender Targeting**: Male, Female
- **Age Targeting**: 30-34, 35-39, 40-44, 45-49
- **Interest Targeting**: a code specifying the category to which the person’s interest belongs (interests are as mentioned in the person’s Facebook public profile)



## Summary of Insights

### Age Targeting
- The 45-49 age group received the most impressions and the highest number of ad clicks. 
- Despite allocating the highest ad spend to the 45-49 age group, the 30-34 age segment delivered almost twice as many purchases (Approved Conversions).

### Gender Targeting
- The gender-based spent allocation reveals that spending on males is nearly half of that on females.
- While the female audience segment generated higher impressions, clicks, and inquiries (Total Conversion), the male segment achieved nearly equal Approved Conversions (purchases). This suggests that males may have a higher conversion rate from inquiry to purchase.


### Interest Targeting
- Under Campaign A, interest segments 7, 8, 19, 24, 25, 30, 63, and 65 resulted in zero purchases (Approved Conversions).
- Interest segment 20 under Campaign A, segments 22 and 27 under Campaign B, and segments 22 and 23 under Campaign C resulted in average purchases (0.3 - 0.4) in the lowest portion. However, the cost is nearly double or even triple compared to the segments with the highest average purchases (Avg Approved Conversions). This indicates that these segments are underperforming in terms of cost-efficiency and may not be providing a good return on investment.
- Across all campaigns, the interests with codes 101, 29, 16, 15, and 107 drove the highest Approved Conversions. Focusing more ad spend on these interest segments could yield a higher return on investment.


## Recommendations & Next Step
- Gradually shift a larger portion of the age-based ad budget from the 45-49 segment to the 30-34 segment, which has proven to be more cost-effective in driving purchases. 
- Optimize gender targeting by maintaining strong exposure to both male and female audiences, but prioritize males for conversion campaigns or retargeting efforts.
- Remove the budget for interest segments 7, 8, 19, 24, 25, 30, 63, and 65 under Campaign A, as they generated zero purchases (Approved Conversions). Additionally, consider reducing or reallocating ad spend from interest segment 20 in Campaign A, segments 22 and 27 in Campaign B, and segments 22 and 23 in Campaign C due to their low cost-efficiency. Redirect these funds to the top-performing segments (101, 29, 16, 15, and 107) to maximize ROI.
- Conduct further analysis on the customer journey and messaging resonance to understand why males exhibit higher purchase conversion rates and leverage those insights for campaign optimization.
- Implement ongoing campaign monitoring and optimization based on real-time performance data to continually refine audience targeting and messaging for maximum cost efficiency and return on ad spend.

