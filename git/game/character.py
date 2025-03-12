import random

# Возможные типы персонажей
TYPES = ["Нежить", "Элементаль", "Конструкт", "Гуманоид", "Зверь", "Демон"]

# Таблица урона по типам
DAMAGE_MULTIPLIER = {
    ("Гуманоид", "Зверь"): 2,
    ("Зверь", "Элементаль"): 2,
    ("Элементаль", "Нежить"): 2,
    ("Нежить", "Гуманоид"): 2,
    ("Конструкт", "Демон"): 1.5,
    ("Демон", "Конструкт"): 1.5,
}

# Таблица резистов (уменьшение урона)
RESISTANCE_MULTIPLIER = {
    ("Зверь", "Гуманоид"): 0.5,  # Зверь бьёт гуманоида в 2 раза слабее
}

# Имена врагов и их характеристики
ENEMY_STATS = {
    "Нежить": {"Скелет": (300, 30), "Призрак": (250, 40), "Зомби": (350, 20)},
    "Элементаль": {"Огненный дух": (280, 35), "Каменный голем": (400, 25), "Водный призрак": (260, 30)},
    "Конструкт": {"Железный голем": (450, 20), "Паровой робот": (420, 25), "Механический страж": (400, 30)},
    "Гуманоид": {"Бандит": (320, 35), "Рыцарь": (350, 40), "Маг": (280, 50)},
    "Зверь": {"Волк": (300, 30), "Гиена": (270, 35), "Медведь": (400, 20)},
    "Демон": {"Ифрит": (350, 45), "Проклятый": (320, 50), "Темный лорд": (400, 40)},
}

class Character:
    def __init__(self, tag: str, price: int, damage: int, hp: int, char_type: str):
        self.tag = tag
        self.price = price
        self.damage = damage
        self.hp = hp
        self.type = char_type
        self.healing_potions = 3  # У каждого персонажа 3 зелья лечения

    def take_damage(self, amount: int, attacker_type: str):
        multiplier = DAMAGE_MULTIPLIER.get((attacker_type, self.type), 1)
        resistance = RESISTANCE_MULTIPLIER.get((attacker_type, self.type), 1)
        final_damage = amount * multiplier * resistance
        self.hp -= int(final_damage)
        if self.hp < 0:
            self.hp = 0

    def heal(self):
        if self.healing_potions > 0:
            self.hp += 30  # Зелье восстанавливает 30 HP
            self.healing_potions -= 1

        else:
            print(f"{self.tag} попытался выпить зелье, но у него их больше нет!")

    def show_info(self):
        print(f"{self.tag} — Здоровье: {self.hp}, Урон: {self.damage}, Тип: {self.type}, Зелья: {self.healing_potions}")

    @staticmethod
    def choose_character_type():
        print("Выбери свой тип героя:")
        for i, t in enumerate(TYPES, 1):
            print(f"{i}. {t}")

        while True:
            choice = input("Введи номер типа: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(TYPES):
                    return TYPES[choice - 1]
            print("Некорректный ввод. Попробуй снова.")

    @staticmethod
    def get_random_enemy():
        enemy_type = random.choice(TYPES)
        enemy_name, (hp, damage) = random.choice(list(ENEMY_STATS[enemy_type].items()))
        return Character(enemy_name, 0, damage, hp, enemy_type)
