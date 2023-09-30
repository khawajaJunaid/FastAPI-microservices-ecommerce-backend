# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in Docker
WORKDIR /app

# Copy the content of the local src directory to the working directory
COPY ./ /app
# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt



# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]