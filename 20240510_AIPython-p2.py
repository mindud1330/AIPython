import pandas as pd

# read excel
df = pd.read_excel('BoxOffice.xlsx')
print(df.info())

grouped_movie_count = df.groupby('대표국적')['영화명'].count()
print(grouped_movie_count)

df_england = df[df['대표국적'] == '영국']
print(df_england)

grouped_prior = df.groupby('대표국적')['순위'].min()
print(grouped_prior)
