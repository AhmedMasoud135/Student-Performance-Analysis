import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max.columns',25)

data = pd.read_csv(r"D:\My Course\Machine Learning\Module 1 Python\5.Projects\2.Data Visualization\StudentPerformanceFactors.csv")
print(data)


# Look at the Data
print(data.shape)
print(data.info())
print(data.describe())


# Convert data to numeric
data["Parental_Involvement"] = data["Parental_Involvement"].replace({"Low" : 1,"Medium" : 2,"High" : 3})
data["Access_to_Resources"] = data["Access_to_Resources"].replace({"Low" : 1,"Medium" : 2,"High" : 3})
data["Extracurricular_Activities"] = data["Extracurricular_Activities"].replace({"Yes" : 2,"No" : 1})
data["Motivation_Level"] = data["Motivation_Level"].replace({"Low" : 1,"Medium" : 2,"High" : 3})
data["Internet_Access"] = data["Internet_Access"].replace({"Yes" : 2,"No" : 1})
data["Family_Income"] = data["Family_Income"].replace({"Low" : 1,"Medium" : 2,"High" : 3})
data["Teacher_Quality"] = data["Teacher_Quality"].replace({"Low" : 1,"Medium" : 2,"High" : 3})
data["School_Type"] = data["School_Type"].replace({"Public" : 1,"Private" : 2})
data["Peer_Influence"] = data["Peer_Influence"].replace({"Positive" : 3,"Neutral" : 2,"Negative" : 1})
data["Learning_Disabilities"] = data["Learning_Disabilities"].replace({"Yes" : 2,"No" : 1})
data["Parental_Education_Level"] = data["Parental_Education_Level"].replace({"High School" : 1,"College" : 2,"Postgraduate" : 3})
data["Distance_from_Home"] = data["Distance_from_Home"].replace({"Near" : 1,"Moderate" : 2,"Far" : 3})
data["Physical_Activity"] = data["Physical_Activity"].replace({0:0.5})        # there is 46 value has 0
############################################################################### 


# We have null values at Parental_Education_Level & Distance_from_Home & Teacher_Quality
print(data["Parental_Education_Level"].mean())      # approx. (1.7) ==> College  ==> 2
data["Parental_Education_Level"].fillna(2,inplace=True)


print(data["Distance_from_Home"].mean())      # approx. (1.5) ==> Moderate  ==> 2
data["Distance_from_Home"].fillna(2,inplace=True)


print(data["Teacher_Quality"].mean())      # approx. (2.2) ==> Medium  ==> 2
data["Teacher_Quality"].fillna(2,inplace=True)


# Check for null values:
print(data.columns[data.isnull().any()])
###############################################################################


print(data.columns)
# Group Columns:
# Family Columns: Parental_Involvement - Motivation_Level - Family_Income - Parental_Education_Level
# School Columns: Distance_from_Home - Physical_Activity - School_Type - Teacher_Quality - Internet_Access - Access_to_Resources
# Student Columns: Hours_Studied - Attendance - Extracurricular_Activities - Sleep_Hours - Previous_Scores

data["Family"] = data["Parental_Involvement"]*data["Motivation_Level"]*data["Family_Income"]*data["Parental_Education_Level"]
data["School"] = data["Distance_from_Home"]*data["Physical_Activity"]*data["School_Type"]*data["Teacher_Quality"]*data["Internet_Access"]*data["Access_to_Resources"]
data["Student"] = data["Hours_Studied"]*data["Attendance"]*data["Extracurricular_Activities"]*data["Sleep_Hours"]*data["Previous_Scores"]
###############################################################################



# problem found
## print((data.loc[data["Family"] == 0]))
## print(data["Tutoring_Sessions"].value_counts())
## print(data["School"].value_counts())
## print((data.loc[data["Student"] == 0]))
## print((data.loc[data["Family"] == 0]))
###############################################################################



# Visualization

# Relation Between Numeric Columns and Exam Score
for col in data.select_dtypes(include = "number").columns.drop(['Exam_Score']):
  plt.figure(figsize=(9, 6))
  sns.scatterplot(x= data[col] ,y=data['Exam_Score'] ,data=data ,hue="Gender")
  plt.title(f'Scatter plot of {col} vs Exam_Score')
  plt.xlabel(col)
  plt.ylabel('Exam_Score')
  plt.grid(True)
  plt.savefig(f'{col}.png', dpi=300)
  plt.show()


# Attendance vs Distance
sns.lineplot(data=data, x="Distance_from_Home", y="Attendance")
plt.savefig('Attendance vs Distance.png', dpi=300)
plt.show()


# Look at Correlation
print(data["Sleep_Hours"].corr(data["Attendance"]))    # ===>  -0.016 
print(data["Sleep_Hours"].corr(data["Hours_Studied"]))    # ===>  0.01 
print(data["Teacher_Quality"].corr(data["School_Type"]))    # ===>  0.008

plt.figure(figsize=(15,15), dpi=300)
sns.heatmap(data.select_dtypes(["number"]).corr(), annot=True, cmap="coolwarm")
plt.savefig('Corr.png', dpi=300)







###############################################################################

# Save the data
data.to_csv("NEWData.csv",index=True)





















