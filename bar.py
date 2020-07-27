from matplotlib import pyplot as plt

plt.bar([1,3,5,7,9],[3,4,5,6,7],label='first bar')
plt.bar([2,4,6,8,10],[5,6,7,8,9],color='g',label='second bar')
plt.legend()
plt.title('Bar Graph')
plt.xlabel('bar number')
plt.ylabel('bar height')

plt.show()