from matplotlib import pyplot as plt

x=[1,2,3,4,5,6,7,8,9]
y=[4,6,8,2,4,9,7,5,1]

plt.scatter(x,y,label='skitscat',color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')

plt.legend()

plt.show()
