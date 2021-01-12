 # line color : "r = red" | " g = green" | "r+ = + red plus | with: color='red'"
 # line size: markersize= | linewidth= | note: not with "r+,dkk"
import matplotlib.pyplot as plt
plt.plot([10,20,30,40,],"g",[5,10,20,30],"ro")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Fist Plot")
plt.show()