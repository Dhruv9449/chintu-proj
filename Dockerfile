FROM python:3.9.13

# Install system dependencies
RUN apt-get update && apt-get install -y \
    poppler-utils \
    libpoppler-cpp-dev \
    tesseract-ocr

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements.txt first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
