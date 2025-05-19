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


  
