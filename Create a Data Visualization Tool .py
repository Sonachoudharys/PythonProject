'''
Task: Create a Data Visualization Tool
Build a tool that takes a dataset and
generates interactive visualizations using
libraries such as Matplotlib, Seaborn, or Plotly.
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("C:/Users/Anita/Desktop/PythonProject/tips.csv")

plt.style.use('ggplot')

# Smaller overall figure
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

# 1. Bar plot: Total bill by day
data.groupby('day')['total_bill'].sum().plot(kind='bar', color='skyblue', ax=axes[0, 0])
axes[0, 0].set_title('Bar Chart: Total Bill by Day', fontsize=9, pad=10)
axes[0, 0].set_xlabel('Day', fontsize=8)
axes[0, 0].set_ylabel('Total Bill', fontsize=8)

# 2. Scatter plot: Total bill vs Tip
axes[0, 1].scatter(data['total_bill'], data['tip'], color='green', alpha=0.6)
axes[0, 1].set_title('Scatter Plot: Total Bill vs Tip', fontsize=9, pad=10)
axes[0, 1].set_xlabel('Total Bill', fontsize=8)
axes[0, 1].set_ylabel('Tip', fontsize=8)

# 3. Box plot: Tips by day
data.boxplot(column='tip', by='day', grid=False, ax=axes[1, 0])
axes[1, 0].set_title('Box Plot: Tip by Day', fontsize=9, pad=10)
axes[1, 0].set_xlabel('Day', fontsize=8)
axes[1, 0].set_ylabel('Tip', fontsize=8)

# 4. Pie chart: Gender distribution
gender_counts = data['sex'].value_counts()
axes[1, 1].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 8})
axes[1, 1].set_title('Pie Chart: Gender Distribution', fontsize=9, pad=10)

# Remove automatic title from boxplot
fig.suptitle('')

# Adjust spacing between subplots
plt.tight_layout(pad=4.0)
plt.show()
