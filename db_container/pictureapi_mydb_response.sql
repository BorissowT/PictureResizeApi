CREATE DATABASE IF NOT EXISTS pictureapi_mydb;

USE pictureapi_mydb;

DROP TABLE IF EXISTS `response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `response` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Identifier` varchar(1000) DEFAULT NULL,
  `BaseCode` mediumtext,
  `Width` int DEFAULT NULL,
  `Height` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

