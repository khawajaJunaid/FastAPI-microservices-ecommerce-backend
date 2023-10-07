# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory in Docker
WORKDIR /app


# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt


# Specify the command to run on container start
CMD ["uvicorn", "code/main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]