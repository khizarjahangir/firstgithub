#import libraries 
import seaborn as sns
import matplotlib.pyplot as plt

#set a theme
sns.set_theme(style="ticks",color_codes="True")

#import data set or u can import ur own data
Students = sns.load_dataset("data_viz.csv")

#plot basic graph
p1=sns.countplot(x="sex",data= Students)
print(Students)
# p1.set_title("plot")
# plt.show()