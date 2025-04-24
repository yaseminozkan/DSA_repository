# GRAPH CODES

import pandas as pd
import matplotlib.pyplot as plt

refined_data = pd.read_excel("Refined_Data.xlsx")

# daily caffeine intake graph
plt.figure(figure_size=(10, 6))
plt.plot(refined_data['Date'], refined_data['Caffeine Intake (mg)'], marker='o', color='b', linestyle='-', linewidth=2)
plt.title('Daily Caffeine Intake')
plt.xlabel('Date')
plt.ylabel('Caffeine Intake (mg)')
plt.xticks(rotation=45) 
plt.grid(True)
plt.tight_layout()
plt.show()

# caffeine intake vs break frequency
# (expected negative relation)
plt.figure(figure_size=(8, 6))
plt.scatter(refined_data['Caffeine Intake (mg)'], refined_data['Break Frequency(E/D)'], color='r', alpha=0.6)
plt.title('Caffeine Intake vs Break Frequency')
plt.xlabel('Caffeine Intake (mg)')
plt.ylabel('Break Frequency (E/D)')
plt.grid(True)
plt.tight_layout()
plt.show()

# caffeine intake vs total hours worked
plt.figure(figure_size=(8, 6))
plt.scatter(refined_data['Caffeine Intake (mg)'], refined_data['Total Hours Worked'], color='purple', alpha=0.6)
plt.title('Caffeine Intake vs Total Hours Worked')
plt.xlabel('Caffeine Intake (mg)')
plt.ylabel('Total Hours Worked')
plt.grid(True)
plt.tight_layout()
plt.show()

# break amount vs total hours worked
plt.figure(figure_size=(8, 6))
plt.scatter(refined_data['Break Amount'], refined_data['Total Hours Worked'], color='green', alpha=0.6)
plt.title('Break Amount vs Total Hours Worked')
plt.xlabel('Break Amount (hrs)')
plt.ylabel('Total Hours Worked')
plt.grid(True)
plt.tight_layout()
plt.show()

# quality of workscore calculation ( 0 - 10 )
refined_data['Quality of Work Score'] = ((refined_data['Total Hours Worked'] - refined_data['Break Amount']) / refined_data['Total Hours Worked']) * 10

# box plot for quality of workscore
plt.figure(figure_size=(8, 6))
plt.boxplot(refined_data['Quality of Work Score'])
plt.title('Box Plot of Quality of Work Score')
plt.ylabel('Quality of Work Score')
plt.grid(True)
plt.tight_layout()
plt.show()
