# ===== Stage 1: builder =====
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Створюємо venv в /opt/venv (стандартне місце для переносимого середовища)
RUN python -m venv /opt/venv

# Активувати venv у Dockerfile зручно через повний шлях на pip
ENV PATH="/opt/venv/bin:${PATH}"

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# ===== Stage 2: runtime =====
FROM python:3.12-slim AS runtime

# Мінімальна телеметрія Python, буферизація вимкнена
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Копіюємо готовий venv з builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

WORKDIR /app
COPY main.py .

# Безпека: запускаємося не з root
RUN adduser --disabled-password --gecos '' appuser \
 && chown -R appuser /app
USER appuser

EXPOSE 8000

# Healthcheck без curl/wget: питаємо /healthz
HEALTHCHECK --interval=10s --timeout=2s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0) if urllib.request.urlopen('http://127.0.0.1:8000/healthz').status==200 else sys.exit(1)"

# Uvicorn коректно обробляє SIGTERM → graceful shutdown
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
