# Facebook-campaign-analysis-with-recommendations.

## The goal of this project is to investigate the performance of Facebook marketing campaigns and surface recommendations for future budget allocation across all campaigns, with a focus on maximizing sales conversions through social media advertising.

## Data Cleaning & Exploratory Data Analysis

Identify any missing values and analyze the correlation between key numeric metrics. For more details, click [here](https://github.com/WittsMei/Facebook-campaign-analysis-with-recommendations./blob/main/Facebook%20Campaign%20Data%20Cleaning.ipynb).

<img width="926" alt="image" src="https://github.com/user-attachments/assets/ba84e0cf-9ac5-4b33-bcac-68bcdeba184c">





## Dashboard

The dashboard can be found in Tableau Public [here](https://public.tableau.com/app/profile/witts.jianming.mei/viz/FacebookCampaignPerformanceDsahboard/FacebookadsPerformanceDashboard?publish=yes). This dashboard allows users to filter by age group, campaign type, gender, and interest, with a focus on marketing metrics, purchase metrics, and claim metrics.


<img width="1027" alt="image" src="https://github.com/user-attachments/assets/c013c698-cbc9-4d06-bd3f-c106b6fe1a13">







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
- While the female audience segment generated higher impressions, clicks, and inquiries (Total Conversion), the male segment achieved nearly equal purchases (Approved Conversions). This suggests that males may have a higher conversion rate from inquiry to purchase.


### Interest Targeting
- Under Campaign A, interest segments 7, 8, 19, 24, 25, 30, 63, and 65 resulted in 0 purchases (Approved Conversions). Interestingly, segments 63 and 65 account for the highest spent within the campaign.
- Interest segment 20 in Campaign A, along with segments 22 and 27 in Campaign B and segments 22 and 23 in Campaign C, have yielded the lowest average purchases, approximately 0.3 to 0.4, across each campaign. However, the costs for these segments are nearly double or even triple those associated with the segments that have the highest average purchases (Avg Approved Conversions). This indicates that these segments are underperforming in terms of cost-efficiency and may not be delivering a favorable ROI.
- Across all campaigns, the interests with codes 101, 29, 16, 15, and 107 drove the highest Approved Conversions. Focusing more ad spend on these interest segments could yield a higher return on investment.


## Recommendations & Next Step
- Gradually shift a larger portion of the age-based ad budget from the 45-49 segment to the 30-34 segment, which has proven to be more cost-effective in driving purchases. 
- Optimize gender targeting by maintaining strong exposure to both male and female audiences, but prioritize males for conversion campaigns or retargeting efforts.
- Remove the budget for interest segments (7, 8, 19, 24, 25, 30, 63, and 65) under Campaign A, as they have generated zero purchases (Approved Conversions). Additionally, consider reducing or reallocating ad spend from the lowest-performing segments—20 under Campaign A, 22 and 27 under Campaign B, and 22 and 23 under Campaign C. Redirect these funds to the top-performing segments (101, 29, 16, 15, and 107) to maximize ROI (return on investment).
- Conduct further analysis on the customer journey and messaging resonance to understand why males exhibit higher purchase conversion rates and leverage those insights for campaign optimization.
- Implement ongoing campaign monitoring and optimization based on real-time performance data to continually refine audience targeting and messaging for maximum cost efficiency and ROAS (return on ad spend).

