from matplotlib import pyplot as plt 

days=[1,2,3,4,5]

sleeping=[7,8,6,5,4]
eating=[2,3,1,4,3]
working=[8,9,12,10,15]
playing=[4,6,5,7,3]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

plt.title('Stack Plot')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()