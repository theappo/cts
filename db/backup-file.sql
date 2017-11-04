-- MySQL dump 10.16  Distrib 10.2.9-MariaDB, for osx10.10 (x86_64)
--
-- Host: localhost    Database: cts
-- ------------------------------------------------------
-- Server version	10.2.9-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `applications`
--

DROP TABLE IF EXISTS `applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `applications` (
  `user_id` varchar(64) NOT NULL,
  `password` varchar(64) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `deposit` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applications`
--

LOCK TABLES `applications` WRITE;
/*!40000 ALTER TABLE `applications` DISABLE KEYS */;
INSERT INTO `applications` VALUES ('testuser1','password1',0,999999.90);
/*!40000 ALTER TABLE `applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blacklist`
--

DROP TABLE IF EXISTS `blacklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blacklist` (
  `user_id` varchar(64) NOT NULL,
  `banned` date DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blacklist`
--

LOCK TABLES `blacklist` WRITE;
/*!40000 ALTER TABLE `blacklist` DISABLE KEYS */;
/*!40000 ALTER TABLE `blacklist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `currentprojects`
--

DROP TABLE IF EXISTS `currentprojects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `currentprojects` (
  `proj_id` int(11) NOT NULL,
  `title` varchar(64) DEFAULT NULL,
  `description` varchar(512) DEFAULT NULL,
  `client_id` varchar(64) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `bidding_deadline` date DEFAULT NULL,
  `project_deadline` date DEFAULT NULL,
  `developer_id` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`proj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `currentprojects`
--

LOCK TABLES `currentprojects` WRITE;
/*!40000 ALTER TABLE `currentprojects` DISABLE KEYS */;
/*!40000 ALTER TABLE `currentprojects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logins`
--

DROP TABLE IF EXISTS `logins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `logins` (
  `user_id` varchar(64) NOT NULL,
  `monthlylogins` int(11) DEFAULT NULL,
  `total_logins` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logins`
--

LOCK TABLES `logins` WRITE;
/*!40000 ALTER TABLE `logins` DISABLE KEYS */;
/*!40000 ALTER TABLE `logins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `message_id` int(11) NOT NULL,
  `user_id` varchar(64) DEFAULT NULL,
  `reciever_id` varchar(64) DEFAULT NULL,
  `datesent` date DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectbids`
--

DROP TABLE IF EXISTS `projectbids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projectbids` (
  `proj_id` int(11) DEFAULT NULL,
  `developer_id` varchar(64) DEFAULT NULL,
  `bid` decimal(8,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectbids`
--

LOCK TABLES `projectbids` WRITE;
/*!40000 ALTER TABLE `projectbids` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectbids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projecthistory`
--

DROP TABLE IF EXISTS `projecthistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projecthistory` (
  `proj_id` int(11) NOT NULL,
  `title` varchar(64) DEFAULT NULL,
  `description` varchar(512) DEFAULT NULL,
  `client_id` varchar(64) DEFAULT NULL,
  `developer_id` varchar(64) DEFAULT NULL,
  `client_rating` int(11) DEFAULT NULL,
  `developer_rating` int(11) DEFAULT NULL,
  `language` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`proj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projecthistory`
--

LOCK TABLES `projecthistory` WRITE;
/*!40000 ALTER TABLE `projecthistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `projecthistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projectreviews`
--

DROP TABLE IF EXISTS `projectreviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projectreviews` (
  `proj_id` int(11) DEFAULT NULL,
  `user_id` varchar(64) DEFAULT NULL,
  `review` varchar(512) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projectreviews`
--

LOCK TABLES `projectreviews` WRITE;
/*!40000 ALTER TABLE `projectreviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `projectreviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` varchar(64) NOT NULL,
  `password` varchar(64) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `money` decimal(8,2) DEFAULT NULL,
  `avgrating` decimal(4,3) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `address` varchar(256) DEFAULT NULL,
  `resume` varchar(32) DEFAULT NULL,
  `picture` varchar(32) DEFAULT NULL,
  `samplework` varchar(32) DEFAULT NULL,
  `businesscredentials` varchar(32) DEFAULT NULL,
  `loginstatus` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('testuser2','password2',0,999999.99,3.567,'testuser2@gmail.com','123 Street',NULL,NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-03 15:45:52
