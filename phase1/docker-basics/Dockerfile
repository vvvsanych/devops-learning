# Використовуємо офіційний Python образ
FROM python:3.12-slim

# Встановлюємо мітадані
LABEL maintainer="Volodymyr <solochenko1@bigmir.net>"
LABEL description="My first Docker container for DevOps learning"

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо наш додаток в контейнер
COPY app.py .

# Встановлюємо права на виконання
RUN chmod +x app.py

# Вказуємо користувача (безпека)
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Експонуємо порт (поки не використовуємо, але для прикладу)
EXPOSE 8000

# Команда запуску за замовчуванням
CMD ["python", "app.py"]