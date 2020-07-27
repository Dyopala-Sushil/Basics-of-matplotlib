from matplotlib import pyplot as plt

slices=[7,5,3,10]
activities=['sleeping','eating','playing','working']
cols=['m','k','r','b']

plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0.1,0,0,0),autopct='%1.1f%%')

plt.title('Pie Chart')
plt.show()