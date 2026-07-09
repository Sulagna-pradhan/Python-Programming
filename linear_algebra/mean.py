import numpy as np
import matplotlib.pyplot as plt

heights = np.array([150, 155, 160, 162, 158, 165, 170, 168, 172, 166])

mean = np.mean(heights)
print("Mean is : ", mean)

median = np.median(heights)
print("Median is : ", median)

variance = np.var(heights)
print("Variance is : ", variance)

standard_daviation = np.std(heights)
print(standard_daviation)


plt.hist(heights)
plt.title("Histogram of Student Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()