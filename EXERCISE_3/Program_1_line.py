"""
1. Draw a line in a diagram from position (1, 3) to (2, 10) then to (6, 12) and finally to position
(18, 20). (Mark each point with a beautiful green colour and set line colour to red and line style
dotted)
"""
import matplotlib.pyplot as plt
import numpy as np
xpoint=np.array([1,2,6,18])
ypoint=np.array([3,10,12,20])
plt.plot(xpoint,ypoint,marker='o',ms=10,mfc="g",mec="g",linestyle="dotted",color="red")
plt.show()

