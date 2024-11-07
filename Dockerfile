FROM python:3.11

# Set the working directory in the container
WORKDIR /flipbookproject

# Copy the requirements file to the container
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y imagemagick libmagickwand-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages from requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]