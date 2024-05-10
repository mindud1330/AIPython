import pandas as pd

df = pd.DataFrame({ '학생': ['John', 'Alice', 'Bob', 'Emily'], 
                    '수학': [90, 87, 78, 92], 
                    '영어': [85, 91, 80, 80], 
                    '과학': [88, 89, 85, 82] })

print(df.describe())

print("\n수학 최고점 학생:")
max_math = df['수학'].max()
print(df[df['수학'] == max_math])

print("\n수학 90점 이상 학생")
df_mathover90 = df[df['수학'] >= 90]
print(df_mathover90)