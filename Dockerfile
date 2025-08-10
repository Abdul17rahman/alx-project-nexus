FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project
COPY . /app

# Create a non-root user to run the app
RUN addgroup --system web && adduser --system --ingroup web web

# Make entrypoint executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose port
EXPOSE 8000

USER web

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "jobboard.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
