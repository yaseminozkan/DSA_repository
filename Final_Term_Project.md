# Does Caffeine Productivity – DSA210 Term Project ☕️
###### the layout of this project file was heavily inspired by Ada Dila Akbulut's final submission (which you have sent us as a sample).
### The aim of this project is to analyze the relationship between caffeine consumption and productivity based on manually collected data such as caffeine intake, sleep, work hours,etc. Is the relation just a placebo? Or does it really have positive effects? 

- **Null Hypothesis:** "Caffeine intake has no impact on productivity"
- **Alternative Hypothesis:** Caffeine intake positively (or negatively) affects productivity.

# Motivation & Project Goal
Coffee and it's derivatives are a big part of our daily lives. Many use it for it's scientifically proven effect; block melatonin(sleep hormone) from binding to certain receptors and prevent sleepiness. 
But over time people have started to think that it also increases their productivity. So far no study canprove the corelation. This project attempts to analyze this relation using self-tracked data.

# Data Sources & Pre-proccessing
All off the data was collected manually and put into an excel file. The data which i collected were:
- Caffeine Intake (mg)
- Time of Intake
- Total Hours Worked
- Break Amount
- Sleep Duration(hours)
- Drink Type

Then some of these data were used to create new data such as:
- Break Frequency(Break Amount / Total hours worked)
- Quality of Work Score = ((Hours Worked - Break Amount) / Total Work Time ) * 10
  
