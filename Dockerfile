FROM python:3.14-slim

# Improve Python behavior in containers and reduce noisy bytecode/cache files.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first to maximize layer caching.
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the application source.
COPY . .

EXPOSE 8000

# Run the FastAPI app with uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
