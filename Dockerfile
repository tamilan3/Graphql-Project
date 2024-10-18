FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Command to run your application
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]

