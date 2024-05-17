import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')

x = ['서울', '부산', '인천', '대구']
y = [9904312, 3448737, 2890451, 2466052]

plt.bar(x, y)
plt.xlabel('도시')
plt.ylabel('인구 수')
plt.show()
