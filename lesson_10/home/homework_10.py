"""
Шаблони класів об'єктів природи та побуту (ЗАГОТОВКИ)
Template classes for nature and household objects (TEMPLATES)

ІНСТРУКЦІЯ / INSTRUCTION:
Реалізуйте всі методи та властивості згідно з вимогами в коментарях
Implement all methods and properties according to requirements in comments
"""

import math


class Tree:
    """
    Клас природного об'єкта "Дерево"
    Class for natural object "Tree"
    
    Атрибути / Attributes:
    - height: висота дерева (0 < height < 150 метрів)
    - trunk_diameter: діаметр стовбура (0 < diameter < 1000 см)
    - leaf_count: кількість листя (обчислюється автоматично)
    """
    
    def __init__(self, height, trunk_diameter):
        """
        Ініціалізація дерева / Initialize tree
        
        Args:
            height (float): Висота дерева в метрах / Tree height in meters
            trunk_diameter (float): Діаметр стовбура в см / Trunk diameter in cm
        
        TODO: 
        - Встановити атрибути через властивості для валідації
        - Обчислити початкову кількість листя
        """
        pass
    
    @property
    def height(self):
        """
        Властивість: висота дерева / Property: tree height
        
        TODO: Повернути значення приватного атрибута _height
        """
        pass
    
    @height.setter
    def height(self, value):
        """
        Сетер для висоти дерева / Setter for tree height
        
        TODO: 
        - Перевірити що 0 < value < 150
        - Встановити _height = value
        - Перерахувати кількість листя
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def trunk_diameter(self):
        """
        Властивість: діаметр стовбура / Property: trunk diameter
        
        TODO: Повернути значення приватного атрибута _trunk_diameter
        """
        pass
    
    @trunk_diameter.setter
    def trunk_diameter(self, value):
        """
        Сетер для діаметра стовбура / Setter for trunk diameter
        
        TODO:
        - Перевірити що 0 < value < 1000
        - Встановити _trunk_diameter = value
        - Перерахувати кількість листя
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def leaf_count(self):
        """
        Властивість: кількість листя (тільки читання) / Property: leaf count (read-only)
        
        TODO: Повернути значення _leaf_count
        """
        pass
    
    def _calculate_leaf_count(self):
        """
        Приватний метод: обчислення кількості листя / Private method: calculate leaf count
        
        Формула: height * trunk_diameter * 100
        
        TODO: 
        - Обчислити кількість листя за формулою
        - Повернути результат
        """
        pass
    
    def grow(self):
        """
        Метод: ріст дерева / Method: tree growth
        
        TODO:
        - Збільшити висоту на 0.5 м (але не більше 149.9)
        - Збільшити діаметр стовбура на 2 см (але не більше 999.9)
        - Використовувати властивості для автоматичного перерахунку листя
        - Вивести повідомлення про ріст
        """
        pass
    
    def leaf_fall(self):
        """
        Метод: опадання листя / Method: leaf fall
        
        TODO:
        - Зменшити кількість листя на 30% (помножити на 0.7)
        - Вивести повідомлення про опадання
        """
        pass
    
    def get_info(self):
        """
        Метод: отримати інформацію про дерево / Method: get tree information
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити висоту, діаметр стовбура, кількість листя
        """
        pass


class Kettle:
    """
    Клас побутового об'єкта "Чайник"
    Class for household object "Kettle"
    
    Атрибути / Attributes:
    - volume: максимальний об'єм (0.5 <= volume <= 5 літрів)
    - current_volume: поточний об'єм води (0 <= current <= volume)
    - water_temperature: температура води (за замовчуванням 20°C)
    - is_on: чи включений чайник (за замовчуванням False)
    """
    
    def __init__(self, volume):
        """
        Ініціалізація чайника / Initialize kettle
        
        Args:
            volume (float): Максимальний об'єм в літрах / Maximum volume in liters
        
        TODO:
        - Встановити volume через властивість
        - Ініціалізувати current_volume = 0
        - Ініціалізувати water_temperature = 20
        - Ініціалізувати is_on = False
        """
        pass
    
    @property
    def volume(self):
        """
        Властивість: максимальний об'єм / Property: maximum volume
        
        TODO: Повернути _volume
        """
        pass
    
    @volume.setter
    def volume(self, value):
        """
        Сетер для максимального об'єму / Setter for maximum volume
        
        TODO:
        - Перевірити що 0.5 <= value <= 5
        - Встановити _volume = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def current_volume(self):
        """
        Властивість: поточний об'єм води / Property: current water volume
        
        TODO: Повернути _current_volume
        """
        pass
    
    @property
    def water_temperature(self):
        """
        Властивість: температура води / Property: water temperature
        
        TODO: Повернути _water_temperature
        """
        pass
    
    @property
    def is_on(self):
        """
        Властивість: стан чайника / Property: kettle state
        
        TODO: Повернути _is_on
        """
        pass
    
    def pour_water(self, amount):
        """
        Метод: налити воду / Method: pour water
        
        Args:
            amount (float): Кількість води для додавання / Amount of water to add
        
        TODO:
        - Перевірити що amount >= 0
        - Обчислити скільки води можна додати (не більше ніж volume)
        - Додати воду до current_volume
        - Вивести повідомлення про додавання
        - Повідомити якщо чайник переповнений
        """
        pass
    
    def drain_water(self, amount):
        """
        Метод: злити воду / Method: drain water
        
        Args:
            amount (float): Кількість води для зливання / Amount of water to drain
        
        TODO:
        - Перевірити що amount >= 0
        - Зменшити current_volume (але не менше 0)
        - Вивести повідомлення про зливання
        """
        pass
    
    def turn_on(self):
        """
        Метод: включити чайник / Method: turn on kettle
        
        TODO:
        - Перевірити що в чайнику є вода (current_volume > 0)
        - Встановити is_on = True
        - Встановити water_temperature = 100
        - Вивести повідомлення про включення
        - Якщо води немає - вивести попередження
        """
        pass
    
    def turn_off(self):
        """
        Метод: вимкнути чайник / Method: turn off kettle
        
        TODO:
        - Встановити is_on = False
        - Вивести повідомлення про вимкнення
        """
        pass
    
    def get_status(self):
        """
        Метод: отримати статус чайника / Method: get kettle status
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити об'єм, температуру, стан включення
        """
        pass


class Cloud:
    """
    Клас природного об'єкта "Хмара"
    Class for natural object "Cloud"
    
    Атрибути / Attributes:
    - area: площа хмари (1 <= area <= 10000 км²)
    - altitude: висота над землею (0.5 <= altitude <= 15 км)
    - humidity_density: щільність вологи (0 <= humidity <= 30 г/м³)
    - rain_probability: ймовірність дощу (обчислюється автоматично)
    """
    
    def __init__(self, area, altitude, humidity_density):
        """
        Ініціалізація хмари / Initialize cloud
        
        Args:
            area (float): Площа хмари в км² / Cloud area in km²
            altitude (float): Висота над землею в км / Altitude above ground in km
            humidity_density (float): Щільність вологи в г/м³ / Humidity density in g/m³
        
        TODO:
        - Встановити всі атрибути через властивості
        - Обчислити початкову ймовірність дощу
        """
        pass
    
    @property
    def area(self):
        """
        Властивість: площа хмари / Property: cloud area
        
        TODO: Повернути _area
        """
        pass
    
    @area.setter
    def area(self, value):
        """
        Сетер для площі хмари / Setter for cloud area
        
        TODO:
        - Перевірити що 1 <= value <= 10000
        - Встановити _area = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def altitude(self):
        """
        Властивість: висота / Property: altitude
        
        TODO: Повернути _altitude
        """
        pass
    
    @altitude.setter
    def altitude(self, value):
        """
        Сетер для висоти / Setter for altitude
        
        TODO:
        - Перевірити що 0.5 <= value <= 15
        - Встановити _altitude = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def humidity_density(self):
        """
        Властивість: щільність вологи / Property: humidity density
        
        TODO: Повернути _humidity_density
        """
        pass
    
    @humidity_density.setter
    def humidity_density(self, value):
        """
        Сетер для щільності вологи / Setter for humidity density
        
        TODO:
        - Перевірити що 0 <= value <= 30
        - Встановити _humidity_density = value
        - Перерахувати ймовірність дощу
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def rain_probability(self):
        """
        Властивість: ймовірність дощу (тільки читання) / Property: rain probability (read-only)
        
        TODO: Повернути _rain_probability
        """
        pass
    
    def _calculate_rain_probability(self):
        """
        Приватний метод: обчислення ймовірності дощу / Private method: calculate rain probability
        
        Формула: min(humidity_density * 3, 100)
        
        TODO:
        - Обчислити ймовірність за формулою
        - Повернути результат
        """
        pass
    
    def accumulate_moisture(self, amount):
        """
        Метод: накопичити вологу / Method: accumulate moisture
        
        Args:
            amount (float): Кількість вологи для додавання / Amount of moisture to add
        
        TODO:
        - Перевірити що amount >= 0
        - Збільшити humidity_density на amount (але не більше 30)
        - Використати властивість для автоматичного перерахунку ймовірності
        - Вивести повідомлення про накопичення
        """
        pass
    
    def rain(self):
        """
        Метод: дощ / Method: rain
        
        TODO:
        - Перевірити чи rain_probability > 70
        - Якщо так: зменшити humidity_density на 50% і вивести повідомлення про дощ
        - Якщо ні: вивести повідомлення що дощу немає з поточною ймовірністю
        - Повернути True якщо йде дощ, False якщо ні
        """
        pass
    
    def move(self, new_altitude):
        """
        Метод: рух хмари / Method: cloud movement
        
        Args:
            new_altitude (float): Нова висота / New altitude
        
        TODO:
        - Встановити нову висоту через властивість
        - Вивести повідомлення про переміщення
        """
        pass
    
    def get_forecast(self):
        """
        Метод: отримати прогноз / Method: get forecast
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити площу, висоту, щільність вологи, ймовірність дощу
        """
        pass


class Aquarium:
    """
    Клас побутового об'єкта "Акваріум"
    Class for household object "Aquarium"
    
    Атрибути / Attributes:
    - length, width, height: розміри (10 < розмір < 200 см)
    - water_level: рівень води (0 <= water_level <= height)
    - fish_count: кількість риб (максимум 1 риба на 5 літрів води)
    - temperature: температура води (18 <= temperature <= 30 °C)
    - water_volume: об'єм води (обчислюється автоматично)
    """
    
    def __init__(self, length, width, height, water_level=0, fish_count=0, temperature=24):
        """
        Ініціалізація акваріума / Initialize aquarium
        
        Args:
            length (float): Довжина в см / Length in cm
            width (float): Ширина в см / Width in cm
            height (float): Висота в см / Height in cm
            water_level (float): Рівень води в см / Water level in cm
            fish_count (int): Кількість риб / Fish count
            temperature (float): Температура води в °C / Water temperature in °C
        
        TODO:
        - Встановити всі атрибути через властивості для валідації
        - Порядок важливий: спочатку розміри, потім water_level, потім fish_count
        """
        pass
    
    @property
    def length(self):
        """
        Властивість: довжина / Property: length
        
        TODO: Повернути _length
        """
        pass
    
    @length.setter
    def length(self, value):
        """
        Сетер для довжини / Setter for length
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _length = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def width(self):
        """
        Властивість: ширина / Property: width
        
        TODO: Повернути _width
        """
        pass
    
    @width.setter
    def width(self, value):
        """
        Сетер для ширини / Setter for width
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _width = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def height(self):
        """
        Властивість: висота / Property: height
        
        TODO: Повернути _height
        """
        pass
    
    @height.setter
    def height(self, value):
        """
        Сетер для висоти / Setter for height
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _height = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def water_level(self):
        """
        Властивість: рівень води / Property: water level
        
        TODO: Повернути _water_level
        """
        pass
    
    @water_level.setter
    def water_level(self, value):
        """
        Сетер для рівня води / Setter for water level
        
        TODO:
        - Перевірити що 0 <= value <= height
        - Встановити _water_level = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def fish_count(self):
        """
        Властивість: кількість риб / Property: fish count
        
        TODO: Повернути _fish_count
        """
        pass
    
    @fish_count.setter
    def fish_count(self, value):
        """
        Сетер для кількості риб / Setter for fish count
        
        TODO:
        - Перевірити що value >= 0
        - Обчислити максимальну кількість риб (water_volume / 5)
        - Перевірити що value не перевищує максимум
        - Встановити _fish_count = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def temperature(self):
        """
        Властивість: температура води / Property: water temperature
        
        TODO: Повернути _temperature
        """
        pass
    
    @temperature.setter
    def temperature(self, value):
        """
        Сетер для температури / Setter for temperature
        
        TODO:
        - Перевірити що 18 <= value <= 30
        - Встановити _temperature = value
        - Викинути ValueError при неправильному значенні
        """
        pass
    
    @property
    def water_volume(self):
        """
        Властивість: об'єм води в літрах (тільки читання) / Property: water volume in liters (read-only)
        
        Формула: (length * width * water_level) / 1000
        
        TODO: Обчислити та повернути об'єм води
        """
        pass
    
    def add_water(self, level_increase):
        """
        Метод: додати воду / Method: add water
        
        Args:
            level_increase (float): Збільшення рівня в см / Level increase in cm
        
        TODO:
        - Перевірити що level_increase >= 0
        - Обчислити новий рівень (не більше height)
        - Встановити новий рівень через властивість
        - Перевірити чи кількість риб все ще допустима
        - Вивести повідомлення про додавання води
        """
        pass
    
    def add_fish(self):
        """
        Метод: додати рибу / Method: add fish
        
        TODO:
        - Обчислити максимальну кількість риб для поточного об'єму
        - Перевірити чи можна додати ще одну рибу
        - Якщо можна: збільшити fish_count на 1
        - Вивести повідомлення про результат операції
        - Повернути True якщо риба додана, False якщо ні
        """
        pass
    
    def remove_fish(self):
        """
        Метод: забрати рибу / Method: remove fish
        
        TODO:
        - Перевірити чи є риби в акваріумі
        - Якщо є: зменшити fish_count на 1
        - Вивести повідомлення про результат операції
        - Повернути True якщо риба забрана, False якщо риб немає
        """
        pass
    
    def heat(self, new_temperature):
        """
        Метод: нагріти воду / Method: heat water
        
        Args:
            new_temperature (float): Нова температура / New temperature
        
        TODO:
        - Встановити нову температуру через властивість
        - Вивести повідомлення про зміну температури
        """
        pass
    
    def inspect(self):
        """
        Метод: огляд акваріума / Method: aquarium inspection
        
        TODO:
        - Обчислити максимальну кількість риб для поточного об'єму
        - Повернути форматований рядок з усією інформацією
        - Включити розміри, рівень води, об'єм, кількість риб, температуру
        """
        pass


# Область для тестування / Testing area
if __name__ == "__main__":
    print("=== ТЕСТУВАННЯ ШАБЛОНІВ КЛАСІВ / TESTING CLASS TEMPLATES ===\n")
    
    # TODO: Розкоментуйте код нижче після реалізації класів
    # Uncomment code below after implementing classes
    
    """
    # Тестування дерева / Testing tree
    print("1. ТЕСТУВАННЯ ДЕРЕВА / TESTING TREE")
    try:
        tree = Tree(10, 50)
        print(tree.get_info())
        tree.grow()
        tree.leaf_fall()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування чайника / Testing kettle
    print("2. ТЕСТУВАННЯ ЧАЙНИКА / TESTING KETTLE")
    try:
        kettle = Kettle(2.0)
        kettle.pour_water(1.5)
        print(kettle.get_status())
        kettle.turn_on()
        kettle.turn_off()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування хмари / Testing cloud
    print("3. ТЕСТУВАННЯ ХМАРИ / TESTING CLOUD")
    try:
        cloud = Cloud(100, 2.5, 15)
        print(cloud.get_forecast())
        cloud.accumulate_moisture(10)
        cloud.rain()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування акваріума / Testing aquarium
    print("4. ТЕСТУВАННЯ АКВАРІУМА / TESTING AQUARIUM")
    try:
        aquarium = Aquarium(50, 30, 40)
        aquarium.add_water(35)
        print(aquarium.inspect())
        aquarium.add_fish()
        aquarium.add_fish()
        aquarium.heat(26)
        print(aquarium.inspect())
    except Exception as e:
        print(f"Помилка: {e}")
    """
    
    print("Реалізуйте методи класів та розкоментуйте код для тестування!")
    print("Implement class methods and uncomment code for testing!")