import matplotlib.pyplot as plt
import random

# inspiration from
# https://towardsdatascience.com/a-differential-privacy-example-for-beginners-ef3c23f69401

detectedVuln = [
        0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, \
        1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, \
        0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, \
        1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, \
        0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, \
        1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, \
        0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, \
        1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, \
        0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, \
        1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, \
        0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, \
        1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1
        ]

def dpAlgo(data):
    dpData = []
    for each in data:
      flip = random.randint(0,1)
      if flip == 0:
        dpData.append(each)
      else:
        dpData.append(random.randint(0,1))

    dpPlotData = {'detected': dpData.count(1), 'not-detected': dpData.count(0)}

    labels = list(dpPlotData.keys())
    values = list(dpPlotData.values())

    graph = plt.bar(labels, values)
    for bar in graph:
      plt.annotate(bar.get_height(), xy=(bar.get_x()+0.33, bar.get_height()-10), fontsize=10, color="white")
    plt.title("With differential privacy: Number of companies who detected a vulnerability.")

# run it first
plt.subplot(2, 1, 1)
dpAlgo(detectedVuln)

plt.subplot(2, 1, 2)
detectedVuln.append(1)
dpAlgo(detectedVuln)


plt.show()
