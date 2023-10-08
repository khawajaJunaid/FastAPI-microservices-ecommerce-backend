
# 🛒 E-Commerce Manager Backend 📈

Welcome to the back-end API that powers a web admin dashboard for e-commerce managers. This API provides detailed insights into sales, revenue, and inventory status, as well as allows new product registration.

## Installation 🚀

This is a FastAPI project that provides documentation for its API using Swagger UI. You can easily run the project using Docker with the following steps:

### Prerequisites ✅

Before running the project on your system, make sure you have the following:

- **Docker:** Ensure that Docker is installed on your system.

## Getting Started 🏁

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/ecommerce.git
   cd ecommerce
   ```

2. The project includes Docker Compose files that start up containers for the database and the two microservices to make the system work.

   In the root directory of the project, run this command:

   ```bash
   ./docker-manager.sh start
   ```

   This command will start up the containers for the database and set up local mounts for persistence on your system.

## Documentation 📚

The backend system consists of two major backend services:

- **products-microservice** 📦 :
  The product microservice handles all operations related to products, including:

  - Create product category 🏷️
  - Register new product 🆕
  - Update product attributes 🔄
  - Fetch product details 📋
  - Retrieve inventory transactions for the product 📊

- **sales-microservice** 💰:
  - Create sales transactions (register a product as sold) 💲
  - Retrieve, filter, and group sales transactions by product, category, and time 📊

The architecture for this project is a less strict microservices architecture, with a single **MySQL** database to which all the microservices connect.

For communication with the database, SQLAlchemy has been used as the ORM to fetch, create, and update data.

### Database Documentation 📦📊

For details on each model and their attributes, please navigate to the `common/db/models` directory.

The database models in SQLAlchemy are one-to-one mappings with Pydantic models provided by FastAPI, allowing flexibility in altering request/response classes and handling internal fields not exposed in API parameters.

A brief overview of how the database works:

- **Categories** 🏷️:
  Different product categories are stored in the database, with constraints and foreign key relations. Products are registered under specific categories, which are specified by an enum of values in the `name` column. This separation allows for curated categories and future attributes to be handled at the categorical level.

- **Products** 📦:
  The products table holds all product attributes, including inventory and relations with categories, inventory, and sales tables. Each unique product is identified by a unique ID.

- **Inventory** 📊:
  This table records all inventory transactions, including initial inventory when a product is created and subsequent quantity updates. It provides a time series of data for all products throughout their lifecycles.

- **Sales** 💲:
  The sales table contains all sales transactions for products. Each transaction is related to a single product, but there can be multiple sales transactions for a product. This table supports aggregations, comparisons, and filtering for revenue and units sold.

For more details, refer to the docstrings on the models.

## Access the API documentation 📖:

The project consists of two major microservices:

To explore the API using Swagger UI, FastAPI offers built-in documentation.

- **products-microservices** 📦:
  [Explore Product Microservice API](http://localhost:8000/docs)

- **sales-microservices** 💰:
  [Explore Sales Microservice API](http://localhost:8001/docs)

Happy exploring and managing your e-commerce backend! 🚀🛍️💹
