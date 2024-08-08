# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([1, 3, 6, 7])
# y = np.array([1, 3, 6, 1])
#
# fig, ax = plt.subplots()
# ax.plot(x, y, color="orange")
# ax.bar(x, y, color="black", edgecolor="black", s=10)  # Add circles with scatter
#
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

label = ['Anil', 'Vikas', 'Dharma',

'Mahen', 'Manish', 'Rajesh']

per = [94,85,45,25,50,54]
N
index = np.arange(len(label))
plt.bar(index, per)

plt.xlabel('Student Name', fontsize=5)
plt.ylabel('Percentage', fontsize=5)
plt.xticks(index, label, fontsize=5,
rotation=30)

plt.title('Percentage of Marks achieve by student Class X')

plt.show()