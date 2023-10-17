FROM python:3.11-bullseye

WORKDIR /app

# Copy files from project to container
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Initialize the API when the container is running
CMD ["uvicorn", "ModelAPI:app", "--host", "0.0.0.0", "--port", "8000"]
