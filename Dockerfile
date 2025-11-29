FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the work directory 
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader vader_lexicon

# Copy code
COPY src/ ./src
# COPY instance/ ./instance

RUN mkdir -p instance

# Environment variables
ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Expose port 5000
EXPOSE 5000

# Run Flask app
CMD ["flask", "--app", "src", "run", "--host=0.0.0.0", "--port=5000"]
