# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8111

# Run server
CMD ["gunicorn", "-b", "0.0.0.0:8111", "your_project.wsgi:application"]
