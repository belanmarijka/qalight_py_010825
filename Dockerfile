# Використовуємо офіційний образ Python версії 3.9
FROM python:3.10

# Створюємо робочу директорію
WORKDIR /app

# Спочатку копіюємо тільки requirements.txt (для кешування)
COPY requirements.txt .

# Оновлюємо pip і встановлюємо залежності
RUN pip install --upgrade pip && pip install -r requirements.txt

# Потім копіюємо решту файлів проєкту
COPY . .

# Виконуємо команду для запуску тестів під час створення контейнера
CMD ["pytest", "lesson_18"]