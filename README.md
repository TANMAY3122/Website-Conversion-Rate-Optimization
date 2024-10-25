# A/B Testing for Website Conversion Rate Optimization

## Project Overview

This project aims to evaluate the effectiveness of changes made to a website's design (e.g., layout and call-to-action buttons) on its conversion rates. By performing an A/B test, we can determine if the treatment variation leads to a statistically significant improvement in conversions compared to the control group.

## Tools Used

- **Python**: Programming language for data analysis.
- **Pandas**: Library for data manipulation and analysis.
- **Matplotlib**: Library for data visualization.
- **Statsmodels**: Library for conducting statistical tests.

## Dataset

The dataset used in this analysis contains information on users who interacted with two variations of a website (control and treatment). It includes the following columns:

- `user_id`: Unique identifier for each user.
- `variation`: Indicates whether the user was in the control or treatment group.
- `converted`: Indicates whether the user converted (1 for yes, 0 for no).

## Steps Performed

1. **Data Loading**: Load the A/B testing data from a CSV file.
2. **Exploratory Data Analysis**: Check for missing values, duplicates, and generate summary statistics.
3. **Conversion Rate Calculation**: Calculate the conversion rates for both control and treatment groups.
4. **Hypothesis Formulation**: Formulate null and alternative hypotheses.
5. **Statistical Testing**: Conduct a two-proportion z-test to compare conversion rates.
6. **Result Interpretation**: Interpret the statistical results.
7. **Visualization**: Create visualizations to represent the conversion rates.

## Statistical Report

### Objective:
Determine if changes to the website (treatment variation) led to a higher conversion rate compared to the control group.

### Key Findings:
- **Control Group Conversion Rate**: 10.00%
- **Treatment Group Conversion Rate**: 12.50%
- **Z-Statistic**: 2.50
- **P-Value**: 0.012

### Conclusion:
- Since the p-value (0.012) is below the 0.05 significance level, we reject the null hypothesis. This suggests that the treatment group’s website variation resulted in a statistically significant increase in conversions.
- The increase in conversion rate from 10.00% to 12.50% represents a **25% improvement** in conversions.

### Recommendation:
Based on these findings, it is recommended to further test or roll out the website changes to monitor the impact on conversions at a larger scale.
