# Task 1

class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones
        self.green_index = self.calculate_green_index()

    def calculate_green_index(self):
        green_index = sum(self.green_zones) / self.territory_area * 100
        return round(green_index , 2)

territory_name = "Пушкин"
territory_area = 28676
green_zones = [302, 487, 420, 325, 471, 363, 404]

green_zone_index = GreenZoneIndex(territory_name, territory_area, green_zones)
print(f"Индекс озеленения территории {territory_name} равен {green_zone_index.green_index}%")

"""
Task 2
Дан список словарей территорий.
Сделать новый список с объектами ранее реализованного типа GreenZoneIndex.
"""

list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]

green_zone_indexes_list = []
for territory in list_territories:
    green_zone_indexes_list.append(GreenZoneIndex(territory.get("territory_name"), territory.get("territory_area"), territory.get("green_zones")))

"""
Task 3
Написать функцию get_mean_green_index,
которая в качестве аргумента принимает список объектов типа GreenZoneIndex 
и считает от них средний индекс озеленения.
"""

def get_mean_green_index(green_zone_indexes):
    return round(sum(map(lambda item: item.green_index, green_zone_indexes)) / 3, 2)

"""
Task 4
Написать функцию filter_min_green_index,
которая в качестве аргументов принимает список объектов типа GreenZoneIndex
и минимальный порог озеленения, значение по умолчанию 0.1.

Результатом функции должно быть число территорий,
индекс озеленения которых ниже заданного минимального порога.
"""

def filter_min_green_index(green_zone_indexes, threshold=0.1):
    counter = 0
    indexes = map(lambda item: item.green_index, green_zone_indexes)
    for index in indexes:
        if index > threshold * 100:
            print(index)
            counter += 1
    return counter

"""
Task 5
Задача. Сделать название городов с заглавной буквы.
"""

list_cities = ["москва", "иЖЕВСк", "Владивосток", "новосибирсК", "мУРМАНСК"]

list_cities = [city.capitalize() for city in list_cities]
print(list_cities)

"""
Task 6
Задача. Отфильтровать города с населением больше 1 млн. человек.
"""

list_cities = [
    {
        "name": "Москва",
        "population": 12 * 10 ** 6,
    },
    {
        "name": "Санкт-Петербург",
        "population": 5 * 10 ** 6,
    },
    {
        "name": "Ижевск",
        "population": 0.6 * 10 ** 6,
    },
]

filter_population = 10 ** 6
filtered_cities = [city for city in list_cities if city.get("population") > filter_population]