import matplotlib.pyplot as plt

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

plotVulns = {'detected': detectedVuln.count(1), 'not-detected': detectedVuln.count(0)}
labels = list(plotVulns.keys())
values = list(plotVulns.values())

plt.subplot(2, 1, 1)
fig = plt.bar(labels, values)
for bar in fig:
    plt.annotate(bar.get_height(), xy=(bar.get_x()+0.33, bar.get_height()-10), fontsize=10, color="white")
plt.title("No differential privacy if a company detected a specific vulnerability.")
plt.text(detectedVuln.count(1), 0, str(detectedVuln.count(1)))

# now append a new element (company)
detectedVuln.append(1)

plotVulns = {'detected': detectedVuln.count(1), 'not-detected': detectedVuln.count(0)}
labels = list(plotVulns.keys())
values = list(plotVulns.values())

plt.subplot(2, 1, 2)
fig2 = plt.bar(labels, values)
for bar in fig2:
  plt.annotate(bar.get_height(), xy=(bar.get_x()+0.33, bar.get_height()-10), fontsize=10, color="white")
plt.title("No differnential privacy: Adding a company to the data.")
plt.text(detectedVuln.count(1), 0, str(detectedVuln.count(1)))

plt.show()
