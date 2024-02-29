# Start from a Python base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Install psycopg2 package
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy the current directory contents into the container at /app
COPY . /app/

# Collect static files
RUN python3 manage.py collectstatic --no-input

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
