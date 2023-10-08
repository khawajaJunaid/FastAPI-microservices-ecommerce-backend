-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: mydatabase
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `name` enum('ELECTRONICS','FASHION','PERSONAL_CARE','TOYS','HOME') DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`category_id`),
  KEY `ix_categories_category_id` (`category_id`),
  KEY `ix_categories_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'ELECTRONICS','appliances and all other stuff'),(2,'FASHION','Clothing line up'),(3,'HOME','Home decor and furniture'),(4,'TOYS','toys for children'),(5,'PERSONAL_CARE','All cosmetic equipment and skin care');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory_transactions`
--

DROP TABLE IF EXISTS `inventory_transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory_transactions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int DEFAULT NULL,
  `category_name` enum('ELECTRONICS','FASHION','PERSONAL_CARE','TOYS','HOME') DEFAULT NULL,
  `inventory_quantity` int DEFAULT NULL,
  `inserted_at` datetime DEFAULT NULL,
  `low_stock_alert_threshold` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `category_name` (`category_name`),
  KEY `ix_inventory_transactions_id` (`id`),
  CONSTRAINT `inventory_transactions_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `inventory_transactions_ibfk_2` FOREIGN KEY (`category_name`) REFERENCES `categories` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory_transactions`
--

LOCK TABLES `inventory_transactions` WRITE;
/*!40000 ALTER TABLE `inventory_transactions` DISABLE KEYS */;
INSERT INTO `inventory_transactions` VALUES (1,1,'ELECTRONICS',15,'2021-10-08 12:48:25',10),(2,2,'ELECTRONICS',15,'2021-10-08 12:48:27',10),(3,3,'FASHION',15,'2021-10-08 12:49:20',10),(4,4,'FASHION',10,'2023-10-08 12:49:27',10),(5,5,'TOYS',10,'2023-10-08 12:49:35',10),(6,6,'TOYS',10,'2023-10-08 12:49:41',10),(7,7,'HOME',10,'2023-10-08 12:49:46',10),(8,8,'HOME',10,'2023-10-08 12:49:51',10),(9,1,'ELECTRONICS',14,'2022-10-08 12:51:20',10),(10,1,'ELECTRONICS',12,'2022-10-08 12:51:22',10),(11,1,'ELECTRONICS',9,'2022-11-08 12:51:26',10),(12,1,'ELECTRONICS',8,'2023-10-08 12:51:29',10),(13,1,'ELECTRONICS',7,'2023-10-08 12:51:30',10),(14,1,'ELECTRONICS',3,'2023-10-08 12:51:35',10),(15,1,'ELECTRONICS',1,'2023-10-08 12:51:39',10),(16,2,'ELECTRONICS',13,'2021-10-08 13:20:07',10),(17,2,'ELECTRONICS',11,'2022-10-08 13:20:08',10),(18,2,'ELECTRONICS',9,'2022-10-08 13:20:09',10),(19,2,'ELECTRONICS',8,'2022-12-08 13:20:13',10),(20,2,'ELECTRONICS',7,'2023-10-08 13:20:15',10),(21,2,'ELECTRONICS',6,'2023-10-08 13:20:21',10),(22,3,'FASHION',11,'2022-10-08 13:26:54',10),(23,3,'FASHION',8,'2022-11-08 13:26:57',10),(24,3,'FASHION',6,'2023-10-08 13:27:01',10),(25,3,'FASHION',5,'2023-10-08 13:27:05',10),(26,3,'FASHION',4,'2023-10-08 13:30:51',10);
/*!40000 ALTER TABLE `inventory_transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category_name` enum('ELECTRONICS','FASHION','PERSONAL_CARE','TOYS','HOME') DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `status` enum('ACTIVE','INACTIVE') DEFAULT NULL,
  `current_inventory` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_name` (`category_name`),
  KEY `ix_products_name` (`name`),
  KEY `ix_products_id` (`id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_name`) REFERENCES `categories` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'ELECTRONICS','Ophone 15 pro max','This is an example product for electronics category.',2000,'https://images.unsplash.com/photo-1546054454-aa26e2b734c7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=880&q=80','2023-10-08 12:48:25','2023-10-08 12:45:15','ACTIVE',1),(2,'ELECTRONICS','Ophone 14','This is an example product for electronics category.',1000,'https://images.unsplash.com/photo-1546054454-aa26e2b734c7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=880&q=80','2023-10-08 12:48:27','2023-10-08 12:45:15','ACTIVE',6),(3,'FASHION','sweater','This is an example product for fashion category.',1500,'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1005&q=80','2023-10-08 12:49:20','2023-10-08 12:45:15','ACTIVE',4),(4,'FASHION','cardigan','This is an example product for fashion category.',1000,'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1005&q=80','2023-10-08 12:49:27','2023-10-08 12:49:27','ACTIVE',10),(5,'TOYS','lego bricks','This is an example product for toys category.',400,'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1005&q=80','2023-10-08 12:49:35','2023-10-08 12:49:35','ACTIVE',10),(6,'TOYS','ironman action bot','This is an example product for fashion category.',500,'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1005&q=80','2023-10-08 12:49:41','2023-10-08 12:49:41','ACTIVE',10),(7,'HOME','decoration plants','This is an example product for home category.',500,'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1005&q=80','2023-10-08 12:49:46','2023-10-08 12:49:46','ACTIVE',10),(8,'HOME','comfortable chair','This is an example product for home category.',1200,'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1005&q=80','2023-10-08 12:49:51','2023-10-08 12:49:51','ACTIVE',10);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int DEFAULT NULL,
  `category_name` enum('ELECTRONICS','FASHION','PERSONAL_CARE','TOYS','HOME') DEFAULT NULL,
  `units_sold` int NOT NULL,
  `sold_at` datetime DEFAULT NULL,
  `total_price` float NOT NULL,
  `revenue` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `category_name` (`category_name`),
  KEY `ix_sales_id` (`id`),
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`category_name`) REFERENCES `categories` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (1,1,'ELECTRONICS',1,'2022-10-08 12:51:20',2000,2000),(2,1,'ELECTRONICS',2,'2022-10-08 12:51:22',4000,4000),(3,1,'ELECTRONICS',3,'2022-11-08 12:51:26',6000,6000),(4,1,'ELECTRONICS',1,'2023-10-08 12:51:29',2000,2000),(5,1,'ELECTRONICS',1,'2023-10-08 12:51:30',2000,2000),(6,1,'ELECTRONICS',4,'2023-10-08 12:51:35',8000,8000),(7,1,'ELECTRONICS',2,'2023-10-08 12:51:39',4000,4000),(8,2,'ELECTRONICS',2,'2022-10-08 13:20:07',2000,2000),(9,2,'ELECTRONICS',2,'2022-10-08 13:20:08',2000,2000),(10,2,'ELECTRONICS',2,'2022-12-08 13:20:09',2000,2000),(11,2,'ELECTRONICS',1,'2023-10-08 13:20:13',1000,1000),(12,2,'ELECTRONICS',1,'2023-10-08 13:20:15',1000,1000),(13,2,'ELECTRONICS',1,'2023-10-08 13:20:21',1000,1000),(14,3,'FASHION',4,'2022-10-08 13:26:54',6000,6000),(15,3,'FASHION',3,'2022-11-08 13:26:57',4500,4500),(16,3,'FASHION',2,'2023-10-08 13:27:01',3000,3000),(17,3,'FASHION',1,'2023-10-08 13:27:05',1500,1500),(18,3,'FASHION',1,'2023-10-08 13:30:51',1500,1500);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'mydatabase'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-08 18:58:03
