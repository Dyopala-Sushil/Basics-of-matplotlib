from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x=[1,2,3]
y=[4,5,1]

x1=[6,9,11]
y1=[5,2,0]

plt.plot(x,y,'c',label='line one',linewidth=5)
plt.plot(x1,y1,'g',label='line two',linewidth=5)
plt.title('Info')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True,color='k')

plt.show()