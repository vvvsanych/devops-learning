FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# 1) Встановлюємо залежності як root (скрипти підуть у /usr/local/bin)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Копіюємо код
COPY main.py .

# 3) Створюємо безпечного користувача і передаємо права
RUN adduser --disabled-password --gecos '' appuser \
 && chown -R appuser /app
USER appuser

EXPOSE 8000

# Healthcheck без curl/wget
HEALTHCHECK --interval=10s --timeout=2s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0) if urllib.request.urlopen('http://127.0.0.1:8000/healthz').status==200 else sys.exit(1)"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
