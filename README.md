
# DaneShop Project

This project is a simple e-commerce for  shop built using Django framework. It includes basic functionalities such as product listing, adding to cart, and pay.

## Features
- Product listing with details
- Add to cart functionality
- Dockerized setup for easy deployment

## Requirements
- Docker
- Docker Compose

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/sinabakhshandeh/daneshop.git
    ```
2. Navigate to the project directory:

    ```
    cd daneshop
    ```

3. Build the Docker image and start the containers:

    ```
    docker-compose up --build
    ```

Access the application at http://localhost:8000

## Faker
You can use two command to popuate database with fake data, run this scripts:

```
# for generate post data
docker exec -it daneshweb python3 manage.py  fake_post_generator

# for generate product data
docker exec -it daneshweb python3 manage.py fake_product_generator
```
