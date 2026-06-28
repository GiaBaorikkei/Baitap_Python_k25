from abc import ABC, abstractmethod


# Lớp cha: Hero (Abstract Base Class)
class Hero(ABC):

    @abstractmethod
    def use_ultimate(self):
        pass


# Lớp Mage
class Mage(Hero):

    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")


# Lớp Assassin
class Assassin(Hero):

    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


# ------------------------
# Loading trận đấu
# ------------------------

print("--- LOADING TRẬN ĐẤU ---")

team_heroes = [
    Mage(),
    Assassin()
]

print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")

# Polymorphism
for hero in team_heroes:
    hero.use_ultimate()