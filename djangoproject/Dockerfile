FROM python:3.10-slim

# Set working directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Command to run your application
CMD ["gunicorn","--workers", "2" ,"--timeout", "120", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]