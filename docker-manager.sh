#!/bin/bash

# Define the paths to the Docker Compose files
DB_COMPOSE_FILE="docker-compose-db.yml"
APP_COMPOSE_FILE="docker-compose-product-service.yml"
SALES_COMPOSE_FILE="docker-compose-sales-service.yml"

# Function to stop all containers
stop_containers() {
  docker-compose -f "$APP_COMPOSE_FILE" down
  docker-compose -f "$DB_COMPOSE_FILE" down
  docker-compose -f "$SALES_COMPOSE_FILE" down
}

# Function to start all containers with environment variables
start_containers() {
  # Load environment variables from .env files (if present)
  if [ -f .env.db ]; then
    export $(cat .env.db | xargs)
  fi

  if [ -f .env.app ]; then
    export $(cat .env.app | xargs)
  fi

  if [ -f .env.sales ]; then
    export $(cat .env.sales | xargs)
  fi

  # Start the containers
  docker-compose -f "$DB_COMPOSE_FILE" up -d 
  docker-compose -f "$APP_COMPOSE_FILE" up -d 
  docker-compose -f "$SALES_COMPOSE_FILE" up -d 
}

# Main script logic
case "$1" in
  "start")
    stop_containers
    start_containers
    ;;
  *)
    echo "Usage: $0 start"
    exit 1
    ;;
esac

exit 0