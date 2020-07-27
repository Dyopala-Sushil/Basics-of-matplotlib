from matplotlib import pyplot as plt
import numpy as np


t1=np.arange(0,10,0.1)


plt.subplot(211)  #plt.subplot(2,1,1)
plt.plot(t1,np.sin(t1),'r',label='sine wave')
plt.legend()
plt.xlabel('sin(t)')
plt.ylabel('time')

plt.subplot(212)  #plt.subplot(2,1,2)
plt.plot(t1,np.cos(t1),'b',label='cosine wave')
plt.xlabel('cos(t)')
plt.ylabel('time')
plt.legend()
plt.show()
