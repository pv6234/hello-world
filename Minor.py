import pandas as pd
df = pd.read_csv("diabetes.csv")
df
import seaborn as sns
import matplotlib.pyplot as plt
df.describe()
import matplotlib.pyplot as plt
sns.catplot(x = "Outcome", hue= "Outcome", kind= "count", data=df)
plt.xlabel("Non-Diabetic                                                        Diabetic")
plt.ylabel("People") 
plt.title(" Statistics for Diabetes")
plt.show()
