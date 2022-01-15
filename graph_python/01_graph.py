# import library
import pandas as pd

# import data
df = pd.read_csv("data_viz.csv")
print(df)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes="True")


p =sns.countplot(x="Gender",data=df, hue="Age")
p.set_title("plot for chilla data")
plt.show()
