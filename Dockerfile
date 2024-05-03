# Используем официальный образ Python
FROM python:3.8

# Копирование исходных файлов приложения в контейнер
COPY . /app

# Установка рабочей директории
WORKDIR /app

# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt

# Определение команды для запуска приложения
CMD ["python", "app.py"]
