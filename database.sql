-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: 127.0.0.1    Database: domainDirectory
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `receiver_id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_members_idx` (`receiver_id`),
  KEY `fk_messages_members1_idx` (`sender_id`),
  CONSTRAINT `fk_messages_members` FOREIGN KEY (`receiver_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_messages_members1` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (7,'',NULL,NULL,64,63),(8,'',NULL,NULL,64,63),(9,'How are you TEST',NULL,NULL,64,63),(12,'testing',NULL,NULL,66,63),(26,'Hello',NULL,NULL,66,63),(28,'Hello',NULL,NULL,64,63),(35,'Raul here','2018-10-18 10:56:01','2018-10-18 10:56:01',67,68),(36,'How are you TEST','2018-10-18 11:53:49','2018-10-18 11:53:49',64,65),(37,'Hello','2018-10-18 11:54:00','2018-10-18 11:54:00',67,65),(41,'Hello','2018-10-18 18:44:27','2018-10-18 18:44:27',67,65),(42,'Hello','2018-10-20 20:20:44','2018-10-20 20:20:44',64,63),(43,'Hello','2018-10-20 20:20:49','2018-10-20 20:20:49',67,63);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (63,'Marco','Basurco','marcobasurco@gmail.com','$2b$12$n4KjsYFoornwCDvGwzV8gujuS.bLOUaZuMrhfE/Nt/1hM2GxiTt5C','2018-10-17 12:13:29','2018-10-17 12:13:29'),(64,'Marco','Basurco','marcobasurco@gmail.com','$2b$12$Kdb4LkylT4fKamiCexVpYeekp0NUeFNMPlG.5pZTEf654Wj5iM3/q',NULL,NULL),(65,'Sarita','Basurco','sara@gmail.com','$2b$12$o/kas5umJ.kMQOxlHq1kqObTiIDin3qyKiF05TOeutbSuKmTcNn8G',NULL,NULL),(66,'Mnmj','mbmnb','marcobasurco@gmail.com','$2b$12$rK8My0jeSxZW4Ol4v.CEVOTPozxe797JBIMbUsjFxTqxWScW5FyY6',NULL,NULL),(67,'Raul','Basurco','raul@gmail.com','$2b$12$v7XBtStn0wrQBmHM1nWlK.gdHxd1x8ZwhEfbPpGUt8fLgcIlO/y8y','2018-10-17 20:47:42','2018-10-17 20:47:42'),(68,'Fernando','Basurco','fernando@gmail.com','$2b$12$D7OEsYojwYYBkqUg2MidL.5ij4LCEAai5xdj43kF85j/GeUyHCTky','2018-10-17 20:48:03','2018-10-17 20:48:03');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'domainDirectory'
--

--
-- Dumping routines for database 'domainDirectory'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-20 20:26:39
