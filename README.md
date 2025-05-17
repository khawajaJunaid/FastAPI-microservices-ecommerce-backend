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

3. Once the containers have started, demo data can be loaded into the mysql database by executing a restoration command into the database from dump.

```bash
  docker exec -i fastapi-microservices-ecommerce-backend-db-1 sh -c 'exec mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE' < ./common/db/dump/dump.sql
```

**Note** : Incase the above command runs into an issue, the volume mount can instead be downloaded from [demo data volume mount](https://drive.google.com/drive/folders/1eb_5FaXY5tzV_EfCKPYFTbNNjvbM-Bg5?usp=sharing) and placed in the
`common/db` and execute the above command as it is.

### Demo data (insights extracted)

The data has been limited to two electronics products nad one fashion product populated with their invenotry changes and sales data over a period of 2 years to enable some comparison and insights, as a proof of concept that the same can be done across more than two categories if need be.

In the comparison over the years, the year 2022 had more sales collectively with more revenue in flow as compared to 2023. In `category` the best seller compared among the two had been electronics by out numbering `fashion`.

Similar extractions can be made from running the apis and comparing the data, with specific group by. The API offers support group by for `category` and `product` and `time` (year,month,day) as well as with dual group bys like category-day, category-mont, category-year, product_id-day, product_id-month, product_id-year.

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

# Additional Concerns 🌐⏰

In cases where the timezone of the data and the user's timezone may differ, it's crucial to handle datetime appropriately to ensure consistency and accuracy. Here are some considerations and a code example to illustrate how to handle datetime using Python and a database.

## Handling Different Timezones ⏰

To manage datetime differences, it's recommended to use UTC timestamps consistently throughout your application. UTC (Coordinated Universal Time) provides a standardized reference point and avoids ambiguity that can arise from timezones.

Here's an example of how to handle datetime conversion between UTC and a user's timezone using Python:

```python
sale_time_utc = retrieve_sale_time_from_database()
sale_time_local = sale_time_utc.astimezone(user_timezone)

```

By following this approach, you ensure that datetime data remains consistent and can be easily adapted to the user's preferred timezone, providing a seamless experience across different time zones.

## Examples of use from demo data

The folder examples in the root shows sample apis request bodies, to navigate and check the data. The major use case pushed for in this project was to get flexibility exploring database and comparison that could be enable by providing an interface or a mini ORM specific to our data and verify the responses. The responses from these can then be used to plot graphs acorss products,categories and timelines.

For exploring the apis apart from the demo data, please refer to the collection thunderclient collections imported in ``/examples`` for both microservices,(thunderclient is a vscode extension like postman for validating apis).

Happy exploring and managing your e-commerce backend! 🚀🛍️💹
