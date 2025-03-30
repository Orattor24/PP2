import matplotlib.pyplot as plt
import networkx as nx

# Создаем граф для карты катакомб
G = nx.DiGraph()

# Добавляем комнаты и пути между ними
rooms = {
    "Вход в катакомбы": (0, 5),
    "Коридор иллюзий": (2, 4),
    "Часовня Глухих": (4, 3),
    "Кровавый лабиринт": (6, 2),
    "Зал Саркофага": (8, 1)
}

# Добавляем пути
edges = [
    ("Вход в катакомбы", "Коридор иллюзий"),
    ("Коридор иллюзий", "Часовня Глухих"),
    ("Часовня Глухих", "Кровавый лабиринт"),
    ("Кровавый лабиринт", "Зал Саркофага")
]

G.add_nodes_from(rooms.keys())
G.add_edges_from(edges)

# Создаем визуализацию
plt.figure(figsize=(8, 5))
pos = rooms
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgray", font_size=10, font_weight="bold", edge_color="black")
plt.title("Карта катакомб под храмом Закрытого Ока", fontsize=12, fontweight="bold")
plt.show()

