import pandas as pd

# read csv
# df_csv = pd.read_csv('실습/data.csv', encoding='UTF-8')
# print(df_csv)

# df_from_url = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv', delimiter='\t')
# print(df_from_url.head(3))

# read excel
df_xl = pd.read_excel('실습/data.xlsx')
# print(df_xl.head(3))
# print(df_xl.info())
print(df_xl[['반', '이름']])

print(df_xl.isna().sum())

# fill na 
df_editna = df_xl.dropna(subset=['응시여부'])
df_editna = df_editna.fillna(0)
# print(df_editna.describe())

# total score
df_editna['총점'] = df_editna['국어'] + df_editna['수학']

# sort data
df_sorted_bykor = df_editna.sort_values(by=['국어'], ascending=False)
print(df_sorted_bykor)

# score >= 80
df_over_80 = df_editna[(df_editna['국어'] >= 80) & (df_editna['수학'] >= 80)]
print(df_over_80)
