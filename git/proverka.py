# Повторное построение графика для вывода изображения
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Векторы r, v и a")

# Рисуем окружность x^2 + y^2 = 16
ax.plot(circle_x, circle_y, 'gray', linestyle='dashed', alpha=0.5)

# Отрисовка векторов
for t in t_values:
    r_vec = r(t)
    v_vec = v(t)
    a_vec = a(t)

    # Радиус-вектор r
    ax.quiver(0, 0, r_vec[0], r_vec[1], angles='xy', scale_units='xy', scale=1, color='b',
              label="r" if t == np.pi else "")

    # Вектор скорости v
    ax.quiver(r_vec[0], r_vec[1], v_vec[0], v_vec[1], angles='xy', scale_units='xy', scale=1, color='g',
              label="v" if t == np.pi else "")

    # Вектор ускорения a
    ax.quiver(r_vec[0], r_vec[1], a_vec[0], a_vec[1], angles='xy', scale_units='xy', scale=1, color='r',
              label="a" if t == np.pi else "")

# Легенда
ax.legend()
ax.grid()

# Сохранение изображения
plot_path = "/mnt/data/vector_plot.png"
plt.savefig(plot_path)
plt.show()

# Вывод пути к изображению
plot_path
