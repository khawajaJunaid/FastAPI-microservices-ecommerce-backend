# E-Commerce Manager Backend

A back-end API that can power a web
admin dashboard for e-commerce managers. This API provides detailed insights into
sales, revenue, and inventory status, as well as allow new product registration.

## Installation

This is a FastAPI project that provides documentation for its API using Swagger UI. You can easily run the project using Docker with the following steps:

## Prerequisites

For running the project on your system, there is no package installation required, only requirement to run the porject locally is:

- Docker: Ensure that Docker is installed on your system.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-fastapi-project.git
   cd your-fastapi-project
   ```

2. The project has docker-compose files that starts up the container for the database, and the two microservices so that the system can work.

In the root directory of the project, run this command:

```bash
  ./docker-manager.sh start
```

The above command will start up the containers for the database and setup local mounts for persistence in your local system.

## Documentation

There backend system consists of two major backend services:

- **products-microservice** :
  The product microservice handles all operations that are concerned with products:
  - create product category
  - create new product
  - update product attributes
  - fetch product details
  - fetch inventory transactions for the product
- **sales-microservice**:
  - create sales transactions i.e register a product was sold
  - retrieve,filter and group by sales transaction across product,category,time.

The choice of architecture for this a less strict microservices architecture, on a typical microservices each microservice would have their own database however for the use case of this project a single **MySQL** databse has been used to which all the microservices connect.

For communication with the databse, SQLALchemy has been used as the orm to fetch,create and update data.

### Database Documentation

For details on each model and their attributes, please navigate to to the `common/db/models`.

The databse models from SQLALchemy have been used in a one to one mapping with pydantic models provided by FastAPI, this way we have the flexibility to alter request response classes and cater for any internal field that should not be exposed to the API params.

A brief map of how the database works:

- _Categories_:
  We should have differnet categories in the database for a product to exist, a constraint with a foreign key relation has been added. So category gets created and using which a product can be registered.

  There are specific categories designated for the products which are specified by an enum of the values, for the `name` column. The purpose of separating out categories includes curated categories, and attributes for future purpose that are very much hanlded on categorical level instead of aggregations on product.

- _Products_:
  The products table holds all product attributes, including invenotry and relations with categories,inventory,and sales table. A unique product is identified with a unique id.

- _Inventory_:
  This table holds all inventory transactions happening across the board on the application. Whenever a product is created the first transaction would be its current invenotry and any updated quantity would be registered as a transaction in the database.

  This would allow us to have time series data for all products for the entirety of its life, it can also save a null value in the inventory possibly indicating a state where the product has been blocked,deleted or any other state that nullified the inventory.

- _Sales_:
  This table holds all the sales transaction corresponding to at the product level i.e a single transaction would be related to a single product but there can be multiple sales transactions for a product.

  This table allows aggregations, comparisons and filtering for revenue and units sold. A valuable resource to monitor for insights and dashboards.

For more details, refer to the docstrings on the models.

## Access the API documentation:

The project consists of two major microservices:

To explore the API using Swagger UI, FastAPI offers in built documentation.

- **products-microservices**:

```
http://localhost:8000/docs
```

- **sales-microservices**:

```
http://localhost:8001/docs
```
