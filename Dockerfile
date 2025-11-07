# Use official Python 3.12 image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Set environment variables
ENV PYTHONPATH=/app

# Ensure allure-results directory exists
RUN mkdir -p allure-results

# Default command: run pytest and output to allure-results
CMD ["pytest", "-v", "--alluredir=allure-results"]