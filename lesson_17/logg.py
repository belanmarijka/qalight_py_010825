import logging

# Створення логера
logger = logging.getLogger(__name__)

# Налаштування рівня логування
logger.setLevel(logging.DEBUG)

# Створення обробника для виводу в stdout (консоль)
console_handler = logging.StreamHandler()

# Створення обробника для запису в файл
file_handler = logging.FileHandler('example.log', encoding="utf-8")

# Налаштування рівня логування для обробників
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# Створення форматера для обробників
formatter = logging.Formatter('%(asctime)s : %(levelname)s - %(message)s - %(funcName)s - %(lineno)d')

# Налаштування форматера для обробників
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Додавання обробників до логера
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# logging.shutdown()