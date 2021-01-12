import matplotlib.pyplot as plt
# dashes :
# plt.plot([10,20,30,40], dashes=[10,20])

# linestyle :
# plt.plot([10,20,30,40], linestyle="-.")

# marker :
# plt.plot([10,20,30,40], marker="+", color="green")
# plt.plot([10,20,30,40], marker="+", markeredgecolor="green", markeredgewidth=20)
# plt.plot([10,20,30,40], marker="+", markeredgecolor="green", markersize=20)
# plt.plot([10,20,30,40], marker=".", markersize=20, markerfacecolor="red")
plt.plot([10,20,30,40,50,60,70,80], marker=".", markevery=3, markersize=10)

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("First Arguments")
plt.show()