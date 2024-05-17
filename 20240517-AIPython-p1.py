import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')

df = pd.DataFrame({
    '요일': ['월', '화', '수', '목', '금', '토', '일'],
    '공부시간(시간)': [2, 3, 1, 5, 4, 2, 1], 
    '성적': [70, 75, 65, 85, 80, 70, 60]
})

x = df['요일']
y1 = df['공부시간(시간)']
y2 = df['성적']

plt.plot(x, y1, label = '공부시간(시간)')
plt.plot(x, y2, label = '성적')
plt.xlabel('요일')
plt.legend()
plt.show()
