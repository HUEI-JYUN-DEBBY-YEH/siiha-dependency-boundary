FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080 \
    PYTHONPATH=/app

# 基本系統依賴（Cloud Run 建議）
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 安裝 Python 套件
COPY backend/requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 複製後端
COPY backend/ .

# 複製前端靜態檔（直接服務）
COPY frontend/ ./static

# Debug（可留，確認用）
RUN echo "=== /app ===" && ls -alh /app
RUN echo "=== /app/static ===" && ls -alh /app/static

EXPOSE 8080

# Cloud Run 正確啟動方式
CMD ["gunicorn","-k","gthread","-w","2","--threads","8","--timeout","120","-b","0.0.0.0:8080","app:app"]
