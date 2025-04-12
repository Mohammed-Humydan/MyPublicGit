import pandas as pd
dic = {'math':[50,47,75,47],'prog':[]'electric':[]}
std =['ahmad','ali','sara','maha']
df = pd.data frame(dic,index=std)
print(df)
df['max']=df.max(axis=1)
df['min']=df.min(axis=1)
df['avg']=df.mean(axis=1)
print(df)