import pandas as pd

csv = pd.read_csv('grade.csv')
print(csv)
units = csv['Units'].sum()
mean = (csv['Units']*csv['Grades']).sum() / units
upper_12 = csv.loc[csv['Grades']>12].__len__()
print(f"""Gpa: {mean}
Courses with grade upper then 12: {upper_12} of {csv.__len__()}""")