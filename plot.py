import matplotlib.pyplot as plt
import numpy as np
 
x = np.arange(0, 255, 1)
 
y = (x/255.0)*(x/255.0)*(x/255.0)*255.0
 
plt.title("gamma")
plt.plot(x, y)
 
plt.show()
