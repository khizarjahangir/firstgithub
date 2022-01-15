#import libraries 
import seaborn as sns
import matplotlib.pyplot as plt

#set a theme
sns.set_theme(style="ticks",color_codes="True")

#import data set or u can import ur own data
titanic = sns.load_dataset("titanic")

#plot basic graph
# p1=sns.countplot(x="sex",data=titanic)
# print(titanic)
# p1.set_title("plot for counting")
# plt.show()

# graph with two variables
p1=sns.countplot(x="sex",data=titanic, hue="class")
p1.set_title("graph")
plt.show()