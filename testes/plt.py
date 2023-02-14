import matplotlib.pyplot as plt

c1 = plt.Circle((0.58,0.6),0.2, color="b")
c2 = plt.Circle((0.43,0.6),0.2, color="r")
c3 = plt.Circle((0.5,0.5),0.2, color="g")

f, ax = plt.subplots()
ax.add_patch(c1)
ax.add_patch(c2)
ax.add_patch(c3)

ax.set_aspect('equal')

plt.show()