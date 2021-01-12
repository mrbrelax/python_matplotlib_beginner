import matplotlib.pyplot as plt
# alpha :
# plt.plot([1,2,3],[4,5,6], alpha=0.25,linewidth=20)
# plt.plot([10,20,30,40], linewidth=20, alpha=0.25)

# zorder :
# plt.plot([10,20,80,90], linewidth=30, zorder=2)
# plt.plot([10,20,30,40], linewidth=30, zorder=1)
plt.plot([0,0],[-1,1], linewidth=15, zorder=2)
plt.plot([-1,1],[-1,1], linewidth=15, zorder=3)
plt.plot([-1,1],[1,-1], linewidth=15, zorder=1)

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Alpha and Zorder")
plt.show()