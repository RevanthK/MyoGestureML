import matplotlib.pyplot as plt
import datetime
import numpy as np

x = np.array([datetime.datetime(2013, 9, 28, i, 0) for i in range(24)])
y = np.random.randint(100, size=x.shape)



plt.xticks(rotation=90)

ax = plt.subplot(111)
pos1 = ax.get_position() # get the original position 
pos2 = [pos1.x0 + 0.3, pos1.y0 + 0.3,  pos1.width / 2.0, pos1.height / 2.0] 
ax.set_position(pos2) # set a new position

#plt.colorbar(image)  # make colorbar
#plt.xlim(amin, amax)
#plt.ylim(bmin, bmax)


plt.xlabel(r'$Time (secs)$', fontsize=18)
plt.ylabel(r'$Myo\ Units$', fontsize=18)
plt.plot(x,y)
plt.show()