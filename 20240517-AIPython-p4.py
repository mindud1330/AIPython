import numpy as np
import matplotlib.pyplot as plt
import math

# dataset 1
x = np.random.rand(100) * 10
x.sort()

y1 = []
for d in x:
    y1.append(math.sin(d))

# dataset 2
y2 = []
for d in x:
    y2.append(math.cos(d))

fig, asx = plt.subplots(1, 2)

asx[0].scatter(x, y1)
asx[0].title.set_text('Sine Graph')

asx[1].scatter(x, y2)
asx[1].title.set_text('Cosine Graph')

plt.show()