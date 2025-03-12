from print import *
from character import *

print_slow("Приветствую в игру")

# Создание персонажей
player_type = Character.choose_character_type()
player_name = input("Выбери имя для своего персонажа: ")
player = Character(player_name, 500, 50, 200, player_type)

enemy = Character.get_random_enemy()
print(f"Твой противник: {enemy.tag} ({enemy.type})")

ACTIONS = {
    "1": "защита",
    "2": "атака",
    "3": "зелье"
}

while player.hp > 0 and enemy.hp > 0:
    print("\nТвой ход! 1 - Защита, 2 - Атака, 3 - Зелье:")
    player_action = input()

    if player_action not in ACTIONS:
        print("Некорректный ввод, пропуск хода!")
        continue

    enemy_action = random.choice(["1", "2", "3"] if enemy.healing_potions > 0 else ["1", "2"])

    print(f"Ты выбрал {ACTIONS[player_action]}!")
    print(f"{enemy.tag} выбрал {ACTIONS[enemy_action]}!")

    # Лечение выполняется ДО проверки урона, но атака все равно проходит
    if player_action == "3":
        player.heal()
    if enemy_action == "3":
        enemy.heal()

    # Логика боя (урон теперь наносится в любом случае)
    if player_action == "2":
        enemy.take_damage(player.damage, player.type)
    if enemy_action == "2":
        player.take_damage(enemy.damage, enemy.type)

    # Защита (атаку нельзя блокировать, если цель лечится)
    if player_action == "1" and enemy_action == "2":
        print(f"Атака {enemy.tag} заблокирована!")
        player.hp += enemy.damage  # Отмена урона
    if enemy_action == "1" and player_action == "2":
        print(f"Атака {player.tag} заблокирована!")
        enemy.hp += player.damage  # Отмена урона

    # Вывод информации
    player.show_info()
    enemy.show_info()


# Итог
print("Ты проиграл!" if player.hp <= 0 else "Ты победил!")

