import matplotlib.pyplot as plt

n=100

squares = [0] * n

for i in range (n):
    squares[i] = i*i

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()