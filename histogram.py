from matplotlib import pyplot as plt

population_ages=[10,15,20,30,35,45,50]
bins=[10,20,30,40,50,60,70]

plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')

plt.show()