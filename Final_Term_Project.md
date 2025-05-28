# Does Caffeine Productivity – DSA210 Term Project ☕️
###### the layout of this project file was heavily inspired by Ada Dila Akbulut's final submission (which you have sent us as a sample).
### The aim of this project is to analyze the relationship between caffeine consumption and productivity based on manually collected data such as caffeine intake, sleep, work hours,etc. Is the relation just a placebo? Or does it really have positive effects? 

- **Null Hypothesis:** "Caffeine intake has no impact on productivity"
- **Alternative Hypothesis:** Caffeine intake positively (or negatively) affects productivity.

# Motivation & Project Goal
Coffee and it's derivatives are a big part of our daily lives. Many use it for it's scientifically proven effect; block melatonin(sleep hormone) from binding to certain receptors and prevent sleepiness. 
But over time people have started to think that it also increases their productivity. So far no study canprove the corelation. This project attempts to analyze this relation using self-tracked data.

# Data Collection & Pre-proccessing
#### All off the data was collected manually and put into an excel file. The data which i collected were:
- Caffeine Intake (mg)
- Time of Intake
- Total Hours Worked
- Break Amount
- Sleep Duration(hours)
- Drink Type

#### Then some of these data were used to create new data such as:
- Break Frequency(Break Amount / Total hours worked)
- Quality of Work Score = ((Hours Worked - Break Amount) / Total Work Time ) * 10


## Data analysis (EDA,etc.) of the data  & Findings

#### - The data which was collected was checked using Box Plots and Z-score to see if it was appropriate to use.
##### -> First Box-Plots were made then the ones conatining outliers were checked for Z-score.
You can check the  [`box_plots`](box_plots) folder to see the graphs for each data.

#### Further graphs used to check for corelation. You can acccess the graphs codes on  [Graph Codes & Hypothesis Testing Notebook](Graph_codes&Hypothesis_testing.ipynb)
##### -> The line graph below shows my daily caffeine intake for each day. There are some 0 values where no caffeine was consumed but work was still done.
![image](https://github.com/yaseminozkan/DSA_repository/blob/e60b102af573bf6ea0f3cd9d49323e61b619643b/GRAPHS/Daily%20Caffeine%20Intake.png)

##### -> The scatterplot below shows the relation between Caffeine intake and Total hours worked. If there was a coraletion we would expect o see a linear positive increase (As caf. consumption increases total hours increase). Even though total hours worked increases between 150-175 mg this can be atrributed to the fact that the days before the exam more studying was done and more caffeine was consumed to stay awake wather than caffeine having an effect.
![image](https://github.com/yaseminozkan/DSA_repository/blob/e60b102af573bf6ea0f3cd9d49323e61b619643b/GRAPHS/%20Caffeine%20Intake%20vs%20Total%20Hours%20Worked.png)

##### -> The scatterplot below shows the relation between Total hours work and break amount. It would be expected that as work hours increase break amount has a increase as well(positive relation). The graph is as expected
![image]( https://github.com/yaseminozkan/DSA_repository/blob/e60b102af573bf6ea0f3cd9d49323e61b619643b/GRAPHS/Break%20Amount%20vs%20Total%20Hours%20Worked.png)

##### -> The bar chart bellow show the Quality of Work Score per day. It was made just for a visual representation.
![image](https://github.com/yaseminozkan/DSA_repository/blob/eaa2bf635c7057c7d6e6851ea108f8c51c6c0fdd/GRAPHS/Quality%20of%20Work%20Score.png)

##### -> The scatterplot below shows the relationship between Caffeine Intake and Quality of Work Score. If caffeine had a direct positive effect on work quality, we would expect to see a rising linear trend due to higher caffeine leading to higher quality scores. However there is no such thing and the data points are widely scattered. This shows no meaningful linear correlation between the two variables. 
![image](https://github.com/yaseminozkan/DSA_repository/blob/899b0c78f4fce8ed4df26b51cf30df1846f8894f/GRAPHS/quality_vs_caffeine_trendline.png)
###### chatgpt was used when generating this graph
# Hypothesis Testing

- **Null Hypothesis:** "Caffeine intake has no impact on productivity"
- **Alternative Hypothesis:** Caffeine intake positively (or negatively) affects productivity.

  I think i should again clarify that since "productivity" has no measurement i used "Quality of Work Score" as producivity. The formula of which was already stated. ->[`general notes`](general_notes.md)

  To evaluate the hypothesis, a Pearson correlation test was applied between daily caffeine intake (in mg) and the computed quality of work score.
### Results

```python
from scipy.stats import pearsonr

#Calculate Quality of Work Score
cleaned_data['Quality of Work Score'] = ((refined_data['Total Hours Worked'] - refined_data['Break Amount']) / refined_data['Total Hours Worked']) * 10

#Pearson correlation between Caffeine Intake and Quality of Work Score
caffeine_intake = cleaned_data['Caffeine Intake (mg)']
quality_of_work_score = cleaned_data['Quality of Work Score']

#Perform Pearson's correlation test
correlation, p_value = pearsonr(caffeine_intake, quality_of_work_score)

#Display
print(f"Pearson Correlation: {correlation}")
print(f"P-value: {p_value}")

#Interpret the result
if p_value < 0.05:
    print("Reject the null hypothesis (H₀): There is a significant relationship between caffeine intake and the Quality of Work Score.")
else:
    print("Fail to reject the null hypothesis (H₀): There is no significant relationship between caffeine intake and the Quality of Work Score.")
 ``` 
#### - Pearson Correlation Coefficient: 0.190
#### - p-value: 0.384

#### !!! The correlation coefficient of 0.19 suggests a very weak positive relationship between caffeine intake and quality of work. However, the p-value of 0.384 is significantly above the commonly accepted threshold of for statistical significance. Therefore, we fail to reject the null hypothesis. *This indicates that there is no statistically significant relationship between caffeine intake and quality of work score in this dataset.*


# Machine Learning Techniques

The goal was to see whether **daily caffeine intake** alone can predict the **Quality of Work Score (QoWS)**

The Machine Learning Model aims to predict Quality of Work Score only by taking caffeine intake(mg) as input. The dataset was split into training and test sets (%80 - %20). Random Forest Generator was used since it's a flexible model that works well even when the relationship between variables isn’t simple or straight. It is overalll a good choice for real-life data that might be a bit messy or unclear.

***The following code was used for the Model***
```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Use only caffeine intake as feature
X = final_data[['Caffeine_Intake_mg']]
y = final_data['Quality_of_Work_Score']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
```

 Results
	**- RMSE: 5.59**
	**-	MAE: 3.98**

These values indicate a *high prediction error*, suggesting that caffeine intake alone does not sufficiently explain the variance in Quality of Work Score. Same as the Hypothesis Testing results. 
The following graph visualizes this; the points are scattered away from the diagonal line. 
![image](https://github.com/yaseminozkan/DSA_repository/blob/1f480362b31890598050da8de8dd6f33d65fabf8/GRAPHS/Actual%20vs.%20Predicted%20QoWS%20(Caffeine%20Only%20Model).png)
###### chatgpt was used when generating this graph

# Conclusion

!!! Even though caffeine is often assumed to improve work performance, the model’s weak predictive power reinforces that other behavioral factors (such as sleep, breaks, or time of day) might play a more important role. The high RMSE and MAE values support the earlier finding that *no significant linear relationship exists between caffeine and productivity.* 


