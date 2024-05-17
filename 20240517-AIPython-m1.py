import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family = 'Malgun Gothic')

df=pd.read_excel('data1.xlsx')

x = df['name']
y1 = df['kor']
y2 = df['math']

plt.plot(x, y1, marker='o', label='국어점수')
plt.plot(x, y2, marker='o',label='수학점수')
plt.title('성적 그래프')
plt.xlabel('이름')
plt.ylabel('점수')
plt.legend()
plt.show()
