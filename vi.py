
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from IPython.display import HTML, display

# ==========================================
# 1. ПАРАБОЛОИД
# ==========================================

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

ax.set_title('1. Параболоид', fontsize=16)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()


# ==========================================
# 2. ТОРОИДАЛЬНАЯ ПОВЕРХНОСТЬ
# ==========================================

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)

U, V = np.meshgrid(u, v)

R = 3  # Большой радиус
r = 1  # Малый радиус

X = (R + r * np.cos(V)) * np.cos(U)
Y = (R + r * np.cos(V)) * np.sin(U)
Z = r * np.sin(V)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')

ax.set_title('2. Тороидальная поверхность', fontsize=16)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_box_aspect([1, 1, 0.5])

plt.show()


# ==========================================
# 3. ДВУМЕРНАЯ СИНУСОИДА В ПРОСТРАНСТВЕ
# АНИМАЦИЯ
# ==========================================

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')


def update(frame):

    ax.clear()

    t = frame * 0.15

    # Волнообразная поверхность
    Z = np.sin(X - t) * np.cos(Y - t)

    ax.plot_surface(
        X, Y, Z,
        cmap='coolwarm',
        vmin=-1,
        vmax=1,
        edgecolor='none'
    )

    ax.set_title('3. Анимация двумерной синусоиды', fontsize=15)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_zlim(-1.5, 1.5)


animation = FuncAnimation(
    fig,
    update,
    frames=40,
    interval=80,
    repeat=True
)

# Отображение анимации прямо в Google Colab
html = HTML(animation.to_jshtml())

plt.close(fig)
display(html)
