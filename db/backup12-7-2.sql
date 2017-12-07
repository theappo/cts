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
-- Table structure for table `Blacklist`
--

DROP TABLE IF EXISTS `Blacklist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Blacklist` (
  `user_id` varchar(64) NOT NULL,
  `ban_date` date DEFAULT NULL,
  `reason` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_blacklist` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Blacklist`
--

LOCK TABLES `Blacklist` WRITE;
/*!40000 ALTER TABLE `Blacklist` DISABLE KEYS */;
/*!40000 ALTER TABLE `Blacklist` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger removeapp after insert on Blacklist for each row
delete from application where user_id = NEW.user_id */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Clients`
--

DROP TABLE IF EXISTS `Clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Clients` (
  `user_id` varchar(64) NOT NULL,
  `avgrating` decimal(4,3) DEFAULT 0.000,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_clientuser` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clients`
--

LOCK TABLES `Clients` WRITE;
/*!40000 ALTER TABLE `Clients` DISABLE KEYS */;
INSERT INTO `Clients` VALUES ('testuser2',NULL),('testuser3',NULL),('testuser5',4.000),('testuser7',NULL),('testuser8',NULL),('testuser9',NULL);
/*!40000 ALTER TABLE `Clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Current_Individual_Project`
--

DROP TABLE IF EXISTS `Current_Individual_Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Current_Individual_Project` (
  `project_id` varchar(64) NOT NULL,
  `developer_id` varchar(64) NOT NULL,
  `bid` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`developer_id`),
  KEY `fk_CurrentIndivProjDev` (`developer_id`),
  CONSTRAINT `fk_CurrentIndivProjDev` FOREIGN KEY (`developer_id`) REFERENCES `Developers` (`user_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_CurrentIndivProjId` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Current_Individual_Project`
--

LOCK TABLES `Current_Individual_Project` WRITE;
/*!40000 ALTER TABLE `Current_Individual_Project` DISABLE KEYS */;
INSERT INTO `Current_Individual_Project` VALUES ('testcurrentproject','testuser4',500.00);
/*!40000 ALTER TABLE `Current_Individual_Project` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger choosedev after insert on Current_Individual_Project for each row begin
delete from Team_Bid_Project where project_id = NEW.project_id;
delete from Individual_Bid_Project where project_id = NEW.project_id;
delete from PendingProjects where project_id = NEW.project_id;
update Projects set project_type = "Individual" where project_id = NEW.project_id;
update Projects set project_status = "Current" where project_id = NEW.project_id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Current_Team_Project`
--

DROP TABLE IF EXISTS `Current_Team_Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Current_Team_Project` (
  `project_id` varchar(64) NOT NULL,
  `team_id` varchar(64) NOT NULL,
  `bid` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`team_id`),
  KEY `fk_CurrentTeamProjectTeam` (`team_id`),
  CONSTRAINT `fk_CurrentTeamProjectID` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_CurrentTeamProjectTeam` FOREIGN KEY (`team_id`) REFERENCES `Teams` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Current_Team_Project`
--

LOCK TABLES `Current_Team_Project` WRITE;
/*!40000 ALTER TABLE `Current_Team_Project` DISABLE KEYS */;
INSERT INTO `Current_Team_Project` VALUES ('currentteam1project','testteam1',1000.00);
/*!40000 ALTER TABLE `Current_Team_Project` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger chooseteam after insert on Current_Team_Project for each row begin
delete from Team_Bid_Project where project_id = NEW.project_id;
delete from Individual_Bid_Project where project_id = NEW.project_id;
delete from PendingProjects where project_id = NEW.project_id;
update Projects set project_type = "Team" where project_id = NEW.project_id;
update Projects set project_status = "Current" where project_id = NEW.project_id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Developers`
--

DROP TABLE IF EXISTS `Developers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Developers` (
  `user_id` varchar(64) NOT NULL,
  `avgrating` decimal(4,3) DEFAULT 0.000,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_devuser` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Developers`
--

LOCK TABLES `Developers` WRITE;
/*!40000 ALTER TABLE `Developers` DISABLE KEYS */;
INSERT INTO `Developers` VALUES ('testuser10',NULL),('testuser11',1.000),('testuser12',NULL),('testuser4',3.000),('testuser6',3.600);
/*!40000 ALTER TABLE `Developers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Individual_Bid_Project`
--

DROP TABLE IF EXISTS `Individual_Bid_Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Individual_Bid_Project` (
  `project_id` varchar(64) NOT NULL,
  `user_id` varchar(64) NOT NULL,
  `bid` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`user_id`),
  KEY `fk_IndivBidDev` (`user_id`),
  CONSTRAINT `fk_IndivBidDev` FOREIGN KEY (`user_id`) REFERENCES `Developers` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_IndivBidProj` FOREIGN KEY (`project_id`) REFERENCES `PendingProjects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Individual_Bid_Project`
--

LOCK TABLES `Individual_Bid_Project` WRITE;
/*!40000 ALTER TABLE `Individual_Bid_Project` DISABLE KEYS */;
INSERT INTO `Individual_Bid_Project` VALUES ('0','testuser11',100.00),('0','testuser6',150.00);
/*!40000 ALTER TABLE `Individual_Bid_Project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PendingProjects`
--

DROP TABLE IF EXISTS `PendingProjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PendingProjects` (
  `project_id` varchar(64) NOT NULL,
  `max_bid` decimal(8,2) DEFAULT NULL,
  `bid_deadline` date DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  CONSTRAINT `fk_PendingProjects` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PendingProjects`
--

LOCK TABLES `PendingProjects` WRITE;
/*!40000 ALTER TABLE `PendingProjects` DISABLE KEYS */;
INSERT INTO `PendingProjects` VALUES ('0',200.00,'2017-12-30'),('1',500.00,'2017-12-30'),('2',500.00,'2017-12-30'),('3',1000.00,'2017-12-30'),('4',2000.00,'2017-12-30');
/*!40000 ALTER TABLE `PendingProjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProjectReviews`
--

DROP TABLE IF EXISTS `ProjectReviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ProjectReviews` (
  `project_id` varchar(64) NOT NULL,
  `sender_id` varchar(64) NOT NULL,
  `receiver_id` varchar(64) NOT NULL,
  `review` varchar(256) DEFAULT NULL,
  `rating` int(1) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`sender_id`,`receiver_id`),
  KEY `fk_ReviewsSender` (`sender_id`),
  KEY `fk_ReviewsReceiver` (`receiver_id`),
  CONSTRAINT `fk_ReviewsProjectId` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_ReviewsReceiver` FOREIGN KEY (`receiver_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_ReviewsSender` FOREIGN KEY (`sender_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProjectReviews`
--

LOCK TABLES `ProjectReviews` WRITE;
/*!40000 ALTER TABLE `ProjectReviews` DISABLE KEYS */;
INSERT INTO `ProjectReviews` VALUES ('proj5','testuser4','testuser6','review',3),('proj5','testuser6','testuser4','review',1),('testproject','testuser2','testuser4','Good Project',5),('testproject','testuser2','testuser6','Good Project',5),('testproject','testuser4','testuser6','gz',5),('testproject','testuser6','testuser4','gz',5),('testproject2','testuser4','testuser5','good project',4),('testproject2','testuser4','testuser6','',2),('testproject2','testuser5','testuser11','Bad Review',3),('testproject2','testuser5','testuser4','Bad Review',3),('testproject2','testuser5','testuser6','Bad Review',3);
/*!40000 ALTER TABLE `ProjectReviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger warnuser after insert on projectreviews for each row 
begin
  call updateUserRating(NEW.sender_id, NEW.receiver_id);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `SuperUsers`
--

DROP TABLE IF EXISTS `SuperUsers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SuperUsers` (
  `user_id` varchar(64) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_superuser` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SuperUsers`
--

LOCK TABLES `SuperUsers` WRITE;
/*!40000 ALTER TABLE `SuperUsers` DISABLE KEYS */;
INSERT INTO `SuperUsers` VALUES ('SuperUser');
/*!40000 ALTER TABLE `SuperUsers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeamHistory`
--

DROP TABLE IF EXISTS `TeamHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TeamHistory` (
  `time_formed` datetime NOT NULL,
  `team_id` varchar(64) NOT NULL,
  `dev1` varchar(64) DEFAULT NULL,
  `dev2` varchar(64) DEFAULT NULL,
  `dev3` varchar(64) DEFAULT NULL,
  `dev4` varchar(64) DEFAULT NULL,
  `dev5` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`time_formed`,`team_id`),
  KEY `fk_teamhistoryid` (`team_id`),
  KEY `fk_teamhistory1` (`dev1`),
  KEY `fk_teamhistory2` (`dev2`),
  KEY `fk_teamhistory3` (`dev3`),
  KEY `fk_teamhistory4` (`dev4`),
  KEY `fk_teamhistory5` (`dev5`),
  CONSTRAINT `fk_teamhistory1` FOREIGN KEY (`dev1`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamhistory2` FOREIGN KEY (`dev2`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamhistory3` FOREIGN KEY (`dev3`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamhistory4` FOREIGN KEY (`dev4`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamhistory5` FOREIGN KEY (`dev5`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamhistoryid` FOREIGN KEY (`team_id`) REFERENCES `Teams` (`team_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeamHistory`
--

LOCK TABLES `TeamHistory` WRITE;
/*!40000 ALTER TABLE `TeamHistory` DISABLE KEYS */;
INSERT INTO `TeamHistory` VALUES ('2017-11-28 22:50:20','testteam1','testuser4','testuser6',NULL,NULL,NULL),('2017-11-28 22:50:47','testteam1','testuser4',NULL,NULL,NULL,NULL),('2017-11-28 22:51:03','testteam1','testuser4','testuser6',NULL,NULL,NULL),('2017-11-28 23:02:41','testteam2','testuser4',NULL,NULL,NULL,NULL),('2017-11-28 23:03:23','testteam3','testuser6',NULL,NULL,NULL,NULL),('2017-12-06 22:20:07','testteam2','testuser4','testuser6','testuser11',NULL,NULL);
/*!40000 ALTER TABLE `TeamHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Team_Bid_Project`
--

DROP TABLE IF EXISTS `Team_Bid_Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Team_Bid_Project` (
  `project_id` varchar(64) NOT NULL,
  `team_id` varchar(64) NOT NULL,
  `bid` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`team_id`),
  KEY `fk_TeamBidsTeams` (`team_id`),
  CONSTRAINT `fk_TeamBidsProject` FOREIGN KEY (`project_id`) REFERENCES `PendingProjects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_TeamBidsTeams` FOREIGN KEY (`team_id`) REFERENCES `Teams` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Team_Bid_Project`
--

LOCK TABLES `Team_Bid_Project` WRITE;
/*!40000 ALTER TABLE `Team_Bid_Project` DISABLE KEYS */;
INSERT INTO `Team_Bid_Project` VALUES ('0','testteam1',200.00),('0','testteam2',150.00);
/*!40000 ALTER TABLE `Team_Bid_Project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teams`
--

DROP TABLE IF EXISTS `Teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Teams` (
  `team_id` varchar(64) NOT NULL,
  `dev1` varchar(64) DEFAULT NULL,
  `dev2` varchar(64) DEFAULT NULL,
  `dev3` varchar(64) DEFAULT NULL,
  `dev4` varchar(64) DEFAULT NULL,
  `dev5` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`team_id`),
  KEY `fk_teamdev1` (`dev1`),
  KEY `fk_teamdev2` (`dev2`),
  KEY `fk_teamdev3` (`dev3`),
  KEY `fk_teamdev4` (`dev4`),
  KEY `fk_teamdev5` (`dev5`),
  CONSTRAINT `fk_teamdev1` FOREIGN KEY (`dev1`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamdev2` FOREIGN KEY (`dev2`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamdev3` FOREIGN KEY (`dev3`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamdev4` FOREIGN KEY (`dev4`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_teamdev5` FOREIGN KEY (`dev5`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teams`
--

LOCK TABLES `Teams` WRITE;
/*!40000 ALTER TABLE `Teams` DISABLE KEYS */;
INSERT INTO `Teams` VALUES ('testteam1','testuser4','testuser6',NULL,NULL,NULL),('testteam2','testuser4','testuser6','testuser11',NULL,NULL),('testteam3','testuser6',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Teams` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger teamChange after insert on Teams for each row
insert TeamHistory values (NOW(), NEW.team_id, NEW.dev1, NEW.dev2, NEW.dev3, NEW.dev4, NEW.dev5) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger teamChange2 after update on Teams for each row
insert TeamHistory values (NOW(), NEW.team_id, NEW.dev1, NEW.dev2, NEW.dev3, NEW.dev4, NEW.dev5) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `TransactionHistory`
--

DROP TABLE IF EXISTS `TransactionHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TransactionHistory` (
  `transaction_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` decimal(8,2) DEFAULT NULL,
  `transaction_date` datetime NOT NULL,
  `receiver` varchar(64) DEFAULT NULL,
  `sender` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `fk_transactionsender` (`receiver`),
  KEY `fk_transactionreceiver` (`sender`),
  KEY `transactionid2` (`transaction_id`),
  CONSTRAINT `fk_transactionreceiver` FOREIGN KEY (`sender`) REFERENCES `Users` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_transactionsender` FOREIGN KEY (`receiver`) REFERENCES `Users` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=469 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TransactionHistory`
--

LOCK TABLES `TransactionHistory` WRITE;
/*!40000 ALTER TABLE `TransactionHistory` DISABLE KEYS */;
INSERT INTO `TransactionHistory` VALUES (1,500.00,'2017-12-06 13:48:03','testuser4','testuser2'),(2,12.50,'2017-12-06 13:48:03','SuperUser','testuser4'),(3,500.00,'2017-12-06 13:48:03','testuser6','testuser2'),(4,12.50,'2017-12-06 13:48:03','SuperUser','testuser6'),(5,25.00,'2017-12-06 13:48:03','SuperUser','testuser2'),(6,500.00,'2017-12-06 13:56:55','testuser4','testuser2'),(7,12.50,'2017-12-06 13:56:55','SuperUser','testuser4'),(8,500.00,'2017-12-06 13:56:55','testuser6','testuser2'),(9,12.50,'2017-12-06 13:56:55','SuperUser','testuser6'),(10,25.00,'2017-12-06 13:56:55','SuperUser','testuser2'),(11,500.00,'2017-12-06 13:58:14','testuser4','testuser2'),(12,12.50,'2017-12-06 13:58:14','SuperUser','testuser4'),(13,500.00,'2017-12-06 13:58:14','testuser6','testuser2'),(14,12.50,'2017-12-06 13:58:14','SuperUser','testuser6'),(15,25.00,'2017-12-06 13:58:14','SuperUser','testuser2'),(16,500.00,'2017-12-06 13:59:02','testuser4','testuser2'),(17,12.50,'2017-12-06 13:59:02','SuperUser','testuser4'),(18,500.00,'2017-12-06 13:59:02','testuser6','testuser2'),(19,12.50,'2017-12-06 13:59:02','SuperUser','testuser6'),(20,25.00,'2017-12-06 13:59:02','SuperUser','testuser2'),(21,500.00,'2017-12-06 15:26:55','testuser4','testuser2'),(22,12.50,'2017-12-06 15:26:55','SuperUser','testuser4'),(23,500.00,'2017-12-06 15:26:55','testuser6','testuser2'),(24,12.50,'2017-12-06 15:26:55','SuperUser','testuser6'),(25,25.00,'2017-12-06 15:26:55','SuperUser','testuser2'),(26,500.00,'2017-12-06 15:28:32','testuser4','testuser2'),(27,12.50,'2017-12-06 15:28:32','SuperUser','testuser4'),(28,500.00,'2017-12-06 15:28:32','testuser6','testuser2'),(29,12.50,'2017-12-06 15:28:32','SuperUser','testuser6'),(30,25.00,'2017-12-06 15:28:32','SuperUser','testuser2'),(31,500.00,'2017-12-06 15:30:25','testuser4','testuser2'),(32,12.50,'2017-12-06 15:30:25','SuperUser','testuser4'),(33,500.00,'2017-12-06 15:30:25','testuser6','testuser2'),(34,12.50,'2017-12-06 15:30:25','SuperUser','testuser6'),(35,25.00,'2017-12-06 15:30:25','SuperUser','testuser2'),(36,500.00,'2017-12-06 15:31:15','testuser4','testuser2'),(37,12.50,'2017-12-06 15:31:15','SuperUser','testuser4'),(38,500.00,'2017-12-06 15:31:15','testuser6','testuser2'),(39,12.50,'2017-12-06 15:31:15','SuperUser','testuser6'),(40,25.00,'2017-12-06 15:31:15','SuperUser','testuser2'),(41,500.00,'2017-12-06 15:31:25','testuser4','testuser2'),(42,12.50,'2017-12-06 15:31:25','SuperUser','testuser4'),(43,500.00,'2017-12-06 15:31:25','testuser6','testuser2'),(44,12.50,'2017-12-06 15:31:25','SuperUser','testuser6'),(45,25.00,'2017-12-06 15:31:25','SuperUser','testuser2'),(46,500.00,'2017-12-06 15:32:28','testuser4','testuser2'),(47,12.50,'2017-12-06 15:32:28','SuperUser','testuser4'),(48,500.00,'2017-12-06 15:32:28','testuser6','testuser2'),(49,12.50,'2017-12-06 15:32:28','SuperUser','testuser6'),(50,25.00,'2017-12-06 15:32:28','SuperUser','testuser2'),(51,500.00,'2017-12-06 15:44:28','testuser4','testuser2'),(52,12.50,'2017-12-06 15:44:28','SuperUser','testuser4'),(53,500.00,'2017-12-06 15:44:28','testuser6','testuser2'),(54,12.50,'2017-12-06 15:44:28','SuperUser','testuser6'),(55,25.00,'2017-12-06 15:44:28','SuperUser','testuser2'),(56,500.00,'2017-12-06 17:17:20','testuser4','testuser2'),(57,12.50,'2017-12-06 17:17:20','SuperUser','testuser4'),(58,500.00,'2017-12-06 17:17:20','testuser6','testuser2'),(59,12.50,'2017-12-06 17:17:20','SuperUser','testuser6'),(60,25.00,'2017-12-06 17:17:20','SuperUser','testuser2'),(61,100.00,'2017-12-06 19:43:28','testuser10','testuser2'),(62,500.00,'2017-12-06 19:50:44','testuser4','testuser2'),(63,12.50,'2017-12-06 19:50:44','SuperUser','testuser4'),(64,500.00,'2017-12-06 19:50:44','testuser6','testuser2'),(65,12.50,'2017-12-06 19:50:44','SuperUser','testuser6'),(66,25.00,'2017-12-06 19:50:44','SuperUser','testuser2'),(67,125.00,'2017-12-06 19:57:10','testuser4','testuser2'),(68,125.00,'2017-12-06 19:57:10','testuser6','testuser2'),(69,125.00,'2017-12-06 19:57:10','testuser4','testuser2'),(70,125.00,'2017-12-06 19:57:10','testuser6','testuser2'),(74,12.50,'2017-12-06 19:57:10','SuperUser','testuser4'),(75,12.50,'2017-12-06 19:57:10','SuperUser','testuser6'),(76,25.00,'2017-12-06 19:57:10','SuperUser','testuser2'),(77,125.00,'2017-12-06 20:18:06','testuser4','testuser2'),(78,125.00,'2017-12-06 20:18:06','testuser6','testuser2'),(79,125.00,'2017-12-06 20:18:06','testuser4','testuser2'),(80,125.00,'2017-12-06 20:18:06','testuser6','testuser2'),(84,12.50,'2017-12-06 20:18:06','SuperUser','testuser4'),(85,12.50,'2017-12-06 20:18:06','SuperUser','testuser6'),(86,25.00,'2017-12-06 20:18:06','SuperUser','testuser2'),(87,125.00,'2017-12-06 21:57:09','testuser4','testuser2'),(88,125.00,'2017-12-06 21:57:09','testuser6','testuser2'),(89,125.00,'2017-12-06 21:57:09','testuser4','testuser2'),(90,125.00,'2017-12-06 21:57:09','testuser6','testuser2'),(94,12.50,'2017-12-06 21:57:09','SuperUser','testuser4'),(95,12.50,'2017-12-06 21:57:09','SuperUser','testuser6'),(96,25.00,'2017-12-06 21:57:09','SuperUser','testuser2'),(97,125.00,'2017-12-06 21:57:27','testuser4','testuser2'),(98,125.00,'2017-12-06 21:57:27','testuser6','testuser2'),(99,125.00,'2017-12-06 21:57:27','testuser4','testuser2'),(100,125.00,'2017-12-06 21:57:27','testuser6','testuser2'),(104,12.50,'2017-12-06 21:57:27','SuperUser','testuser4'),(105,12.50,'2017-12-06 21:57:27','SuperUser','testuser6'),(106,25.00,'2017-12-06 21:57:27','SuperUser','testuser2'),(107,125.00,'2017-12-06 21:58:05','testuser4','testuser2'),(108,125.00,'2017-12-06 21:58:05','testuser6','testuser2'),(109,125.00,'2017-12-06 21:58:05','testuser4','testuser2'),(110,125.00,'2017-12-06 21:58:05','testuser6','testuser2'),(114,12.50,'2017-12-06 21:58:05','SuperUser','testuser4'),(115,12.50,'2017-12-06 21:58:05','SuperUser','testuser6'),(116,25.00,'2017-12-06 21:58:05','SuperUser','testuser2'),(117,125.00,'2017-12-06 21:58:20','testuser4','testuser2'),(118,125.00,'2017-12-06 21:58:20','testuser6','testuser2'),(119,125.00,'2017-12-06 21:58:20','testuser4','testuser2'),(120,125.00,'2017-12-06 21:58:20','testuser6','testuser2'),(124,12.50,'2017-12-06 21:58:20','SuperUser','testuser4'),(125,12.50,'2017-12-06 21:58:20','SuperUser','testuser6'),(126,25.00,'2017-12-06 21:58:20','SuperUser','testuser2'),(127,125.00,'2017-12-06 21:59:58','testuser4','testuser2'),(128,125.00,'2017-12-06 21:59:58','testuser6','testuser2'),(129,125.00,'2017-12-06 21:59:58','testuser4','testuser2'),(130,125.00,'2017-12-06 21:59:58','testuser6','testuser2'),(134,12.50,'2017-12-06 21:59:58','SuperUser','testuser4'),(135,12.50,'2017-12-06 21:59:58','SuperUser','testuser6'),(136,25.00,'2017-12-06 21:59:58','SuperUser','testuser2'),(137,125.00,'2017-12-06 22:13:42','testuser4','testuser2'),(138,125.00,'2017-12-06 22:13:42','testuser6','testuser2'),(139,125.00,'2017-12-06 22:13:42','testuser4','testuser2'),(140,125.00,'2017-12-06 22:13:42','testuser6','testuser2'),(144,12.50,'2017-12-06 22:13:42','SuperUser','testuser4'),(145,12.50,'2017-12-06 22:13:42','SuperUser','testuser6'),(146,25.00,'2017-12-06 22:13:42','SuperUser','testuser2'),(147,125.00,'2017-12-06 22:14:32','testuser4','testuser2'),(148,125.00,'2017-12-06 22:14:32','testuser6','testuser2'),(149,125.00,'2017-12-06 22:14:32','testuser4','testuser2'),(150,125.00,'2017-12-06 22:14:32','testuser6','testuser2'),(154,12.50,'2017-12-06 22:14:32','SuperUser','testuser4'),(155,12.50,'2017-12-06 22:14:32','SuperUser','testuser6'),(156,25.00,'2017-12-06 22:14:32','SuperUser','testuser2'),(157,125.00,'2017-12-06 22:14:48','testuser4','testuser2'),(158,125.00,'2017-12-06 22:14:48','testuser6','testuser2'),(159,125.00,'2017-12-06 22:14:48','testuser4','testuser2'),(160,125.00,'2017-12-06 22:14:48','testuser6','testuser2'),(164,12.50,'2017-12-06 22:14:48','SuperUser','testuser4'),(165,12.50,'2017-12-06 22:14:48','SuperUser','testuser6'),(166,25.00,'2017-12-06 22:14:48','SuperUser','testuser2'),(167,125.00,'2017-12-06 22:21:53','testuser4','testuser2'),(168,125.00,'2017-12-06 22:21:53','testuser6','testuser2'),(169,125.00,'2017-12-06 22:21:53','testuser4','testuser2'),(170,125.00,'2017-12-06 22:21:53','testuser6','testuser2'),(174,12.50,'2017-12-06 22:21:53','SuperUser','testuser4'),(175,12.50,'2017-12-06 22:21:53','SuperUser','testuser6'),(176,25.00,'2017-12-06 22:21:53','SuperUser','testuser2'),(177,125.00,'2017-12-06 22:22:11','testuser4','testuser2'),(178,125.00,'2017-12-06 22:22:11','testuser6','testuser2'),(179,125.00,'2017-12-06 22:22:11','testuser4','testuser2'),(180,125.00,'2017-12-06 22:22:11','testuser6','testuser2'),(184,12.50,'2017-12-06 22:22:11','SuperUser','testuser4'),(185,12.50,'2017-12-06 22:22:11','SuperUser','testuser6'),(186,25.00,'2017-12-06 22:22:11','SuperUser','testuser2'),(187,125.00,'2017-12-06 22:22:25','testuser4','testuser2'),(188,125.00,'2017-12-06 22:22:25','testuser6','testuser2'),(189,125.00,'2017-12-06 22:22:25','testuser4','testuser2'),(190,125.00,'2017-12-06 22:22:25','testuser6','testuser2'),(194,12.50,'2017-12-06 22:22:25','SuperUser','testuser4'),(195,12.50,'2017-12-06 22:22:25','SuperUser','testuser6'),(196,25.00,'2017-12-06 22:22:25','SuperUser','testuser2'),(197,125.00,'2017-12-06 22:23:50','testuser4','testuser2'),(198,125.00,'2017-12-06 22:23:50','testuser6','testuser2'),(199,125.00,'2017-12-06 22:23:50','testuser4','testuser2'),(200,125.00,'2017-12-06 22:23:50','testuser6','testuser2'),(204,12.50,'2017-12-06 22:23:50','SuperUser','testuser4'),(205,12.50,'2017-12-06 22:23:50','SuperUser','testuser6'),(206,25.00,'2017-12-06 22:23:50','SuperUser','testuser2'),(207,100.00,'2017-12-06 22:23:50','testuser4','testuser5'),(208,100.00,'2017-12-06 22:23:50','testuser6','testuser5'),(209,100.00,'2017-12-06 22:23:50','testuser11','testuser5'),(210,100.00,'2017-12-06 22:23:50','testuser4','testuser5'),(211,100.00,'2017-12-06 22:23:50','testuser6','testuser5'),(212,100.00,'2017-12-06 22:23:50','testuser11','testuser5'),(214,10.00,'2017-12-06 22:23:50','SuperUser','testuser4'),(215,10.00,'2017-12-06 22:23:50','SuperUser','testuser6'),(216,10.00,'2017-12-06 22:23:50','SuperUser','testuser11'),(217,30.00,'2017-12-06 22:23:50','SuperUser','testuser5'),(218,125.00,'2017-12-06 22:24:31','testuser4','testuser2'),(219,125.00,'2017-12-06 22:24:31','testuser6','testuser2'),(220,125.00,'2017-12-06 22:24:31','testuser4','testuser2'),(221,125.00,'2017-12-06 22:24:31','testuser6','testuser2'),(225,12.50,'2017-12-06 22:24:31','SuperUser','testuser4'),(226,12.50,'2017-12-06 22:24:31','SuperUser','testuser6'),(227,25.00,'2017-12-06 22:24:31','SuperUser','testuser2'),(228,100.00,'2017-12-06 22:24:31','testuser4','testuser5'),(229,100.00,'2017-12-06 22:24:31','testuser6','testuser5'),(230,100.00,'2017-12-06 22:24:31','testuser11','testuser5'),(231,100.00,'2017-12-06 22:24:31','testuser4','testuser5'),(232,100.00,'2017-12-06 22:24:31','testuser6','testuser5'),(233,100.00,'2017-12-06 22:24:31','testuser11','testuser5'),(235,10.00,'2017-12-06 22:24:31','SuperUser','testuser4'),(236,10.00,'2017-12-06 22:24:31','SuperUser','testuser6'),(237,10.00,'2017-12-06 22:24:31','SuperUser','testuser11'),(238,30.00,'2017-12-06 22:24:31','SuperUser','testuser5'),(239,125.00,'2017-12-06 22:24:47','testuser4','testuser2'),(240,125.00,'2017-12-06 22:24:47','testuser6','testuser2'),(241,125.00,'2017-12-06 22:24:47','testuser4','testuser2'),(242,125.00,'2017-12-06 22:24:47','testuser6','testuser2'),(246,12.50,'2017-12-06 22:24:47','SuperUser','testuser4'),(247,12.50,'2017-12-06 22:24:47','SuperUser','testuser6'),(248,25.00,'2017-12-06 22:24:47','SuperUser','testuser2'),(249,100.00,'2017-12-06 22:24:47','testuser4','testuser5'),(250,100.00,'2017-12-06 22:24:47','testuser6','testuser5'),(251,100.00,'2017-12-06 22:24:47','testuser11','testuser5'),(252,100.00,'2017-12-06 22:24:47','testuser4','testuser5'),(253,100.00,'2017-12-06 22:24:47','testuser6','testuser5'),(254,100.00,'2017-12-06 22:24:47','testuser11','testuser5'),(256,10.00,'2017-12-06 22:24:47','SuperUser','testuser4'),(257,10.00,'2017-12-06 22:24:47','SuperUser','testuser6'),(258,10.00,'2017-12-06 22:24:47','SuperUser','testuser11'),(259,30.00,'2017-12-06 22:24:47','SuperUser','testuser5'),(260,125.00,'2017-12-06 22:25:24','testuser4','testuser2'),(261,125.00,'2017-12-06 22:25:24','testuser6','testuser2'),(262,125.00,'2017-12-06 22:25:24','testuser4','testuser2'),(263,125.00,'2017-12-06 22:25:24','testuser6','testuser2'),(267,12.50,'2017-12-06 22:25:24','SuperUser','testuser4'),(268,12.50,'2017-12-06 22:25:24','SuperUser','testuser6'),(269,25.00,'2017-12-06 22:25:24','SuperUser','testuser2'),(270,100.00,'2017-12-06 22:25:25','testuser4','testuser5'),(271,100.00,'2017-12-06 22:25:25','testuser6','testuser5'),(272,100.00,'2017-12-06 22:25:25','testuser11','testuser5'),(273,100.00,'2017-12-06 22:25:25','testuser4','testuser5'),(274,100.00,'2017-12-06 22:25:25','testuser6','testuser5'),(275,100.00,'2017-12-06 22:25:25','testuser11','testuser5'),(277,10.00,'2017-12-06 22:25:25','SuperUser','testuser4'),(278,10.00,'2017-12-06 22:25:25','SuperUser','testuser6'),(279,10.00,'2017-12-06 22:25:25','SuperUser','testuser11'),(280,30.00,'2017-12-06 22:25:25','SuperUser','testuser5'),(281,125.00,'2017-12-06 22:27:24','testuser4','testuser2'),(282,125.00,'2017-12-06 22:27:24','testuser6','testuser2'),(283,125.00,'2017-12-06 22:27:24','testuser4','testuser2'),(284,125.00,'2017-12-06 22:27:24','testuser6','testuser2'),(288,12.50,'2017-12-06 22:27:24','SuperUser','testuser4'),(289,12.50,'2017-12-06 22:27:24','SuperUser','testuser6'),(290,25.00,'2017-12-06 22:27:24','SuperUser','testuser2'),(291,125.00,'2017-12-06 22:30:14','testuser4','testuser2'),(292,125.00,'2017-12-06 22:30:14','testuser6','testuser2'),(293,125.00,'2017-12-06 22:30:14','testuser4','testuser2'),(294,125.00,'2017-12-06 22:30:14','testuser6','testuser2'),(298,12.50,'2017-12-06 22:30:14','SuperUser','testuser4'),(299,12.50,'2017-12-06 22:30:14','SuperUser','testuser6'),(300,25.00,'2017-12-06 22:30:14','SuperUser','testuser2'),(301,125.00,'2017-12-06 22:30:27','testuser4','testuser2'),(302,125.00,'2017-12-06 22:30:27','testuser6','testuser2'),(303,125.00,'2017-12-06 22:30:27','testuser4','testuser2'),(304,125.00,'2017-12-06 22:30:27','testuser6','testuser2'),(308,12.50,'2017-12-06 22:30:27','SuperUser','testuser4'),(309,12.50,'2017-12-06 22:30:27','SuperUser','testuser6'),(310,25.00,'2017-12-06 22:30:27','SuperUser','testuser2'),(311,125.00,'2017-12-06 22:31:23','testuser4','testuser2'),(312,125.00,'2017-12-06 22:31:23','testuser6','testuser2'),(313,125.00,'2017-12-06 22:31:23','testuser4','testuser2'),(314,125.00,'2017-12-06 22:31:23','testuser6','testuser2'),(318,12.50,'2017-12-06 22:31:23','SuperUser','testuser4'),(319,12.50,'2017-12-06 22:31:23','SuperUser','testuser6'),(320,25.00,'2017-12-06 22:31:23','SuperUser','testuser2'),(321,125.00,'2017-12-06 22:32:25','testuser4','testuser2'),(322,125.00,'2017-12-06 22:32:25','testuser6','testuser2'),(323,125.00,'2017-12-06 22:32:25','testuser4','testuser2'),(324,125.00,'2017-12-06 22:32:25','testuser6','testuser2'),(328,12.50,'2017-12-06 22:32:25','SuperUser','testuser4'),(329,12.50,'2017-12-06 22:32:25','SuperUser','testuser6'),(330,25.00,'2017-12-06 22:32:25','SuperUser','testuser2'),(331,125.00,'2017-12-06 22:32:49','testuser4','testuser2'),(332,125.00,'2017-12-06 22:32:49','testuser6','testuser2'),(333,125.00,'2017-12-06 22:32:49','testuser4','testuser2'),(334,125.00,'2017-12-06 22:32:49','testuser6','testuser2'),(338,12.50,'2017-12-06 22:32:49','SuperUser','testuser4'),(339,12.50,'2017-12-06 22:32:49','SuperUser','testuser6'),(340,25.00,'2017-12-06 22:32:49','SuperUser','testuser2'),(341,125.00,'2017-12-06 22:32:57','testuser4','testuser2'),(342,125.00,'2017-12-06 22:32:57','testuser6','testuser2'),(343,125.00,'2017-12-06 22:32:57','testuser4','testuser2'),(344,125.00,'2017-12-06 22:32:57','testuser6','testuser2'),(348,12.50,'2017-12-06 22:32:57','SuperUser','testuser4'),(349,12.50,'2017-12-06 22:32:57','SuperUser','testuser6'),(350,25.00,'2017-12-06 22:32:57','SuperUser','testuser2'),(351,125.00,'2017-12-06 22:34:29','testuser4','testuser2'),(352,125.00,'2017-12-06 22:34:29','testuser6','testuser2'),(353,125.00,'2017-12-06 22:34:29','testuser4','testuser2'),(354,125.00,'2017-12-06 22:34:29','testuser6','testuser2'),(358,12.50,'2017-12-06 22:34:29','SuperUser','testuser4'),(359,12.50,'2017-12-06 22:34:29','SuperUser','testuser6'),(360,25.00,'2017-12-06 22:34:29','SuperUser','testuser2'),(361,125.00,'2017-12-06 22:36:43','testuser4','testuser2'),(362,125.00,'2017-12-06 22:36:43','testuser6','testuser2'),(363,125.00,'2017-12-06 22:36:43','testuser4','testuser2'),(364,125.00,'2017-12-06 22:36:43','testuser6','testuser2'),(368,12.50,'2017-12-06 22:36:43','SuperUser','testuser4'),(369,12.50,'2017-12-06 22:36:43','SuperUser','testuser6'),(370,25.00,'2017-12-06 22:36:43','SuperUser','testuser2'),(371,125.00,'2017-12-06 22:37:05','testuser4','testuser2'),(372,125.00,'2017-12-06 22:37:05','testuser6','testuser2'),(373,125.00,'2017-12-06 22:37:05','testuser4','testuser2'),(374,125.00,'2017-12-06 22:37:05','testuser6','testuser2'),(378,12.50,'2017-12-06 22:37:05','SuperUser','testuser4'),(379,12.50,'2017-12-06 22:37:05','SuperUser','testuser6'),(380,25.00,'2017-12-06 22:37:05','SuperUser','testuser2'),(381,125.00,'2017-12-06 22:39:10','testuser4','testuser2'),(382,125.00,'2017-12-06 22:39:10','testuser6','testuser2'),(383,125.00,'2017-12-06 22:39:10','testuser4','testuser2'),(384,125.00,'2017-12-06 22:39:10','testuser6','testuser2'),(388,12.50,'2017-12-06 22:39:10','SuperUser','testuser4'),(389,12.50,'2017-12-06 22:39:10','SuperUser','testuser6'),(390,25.00,'2017-12-06 22:39:10','SuperUser','testuser2'),(391,125.00,'2017-12-06 22:39:47','testuser4','testuser2'),(392,125.00,'2017-12-06 22:39:47','testuser6','testuser2'),(393,125.00,'2017-12-06 22:39:47','testuser4','testuser2'),(394,125.00,'2017-12-06 22:39:47','testuser6','testuser2'),(398,12.50,'2017-12-06 22:39:47','SuperUser','testuser4'),(399,12.50,'2017-12-06 22:39:47','SuperUser','testuser6'),(400,25.00,'2017-12-06 22:39:47','SuperUser','testuser2'),(401,125.00,'2017-12-06 22:40:38','testuser4','testuser2'),(402,125.00,'2017-12-06 22:40:38','testuser6','testuser2'),(403,125.00,'2017-12-06 22:40:38','testuser4','testuser2'),(404,125.00,'2017-12-06 22:40:38','testuser6','testuser2'),(408,12.50,'2017-12-06 22:40:38','SuperUser','testuser4'),(409,12.50,'2017-12-06 22:40:38','SuperUser','testuser6'),(410,25.00,'2017-12-06 22:40:38','SuperUser','testuser2'),(411,200.00,'2017-12-06 22:40:38','testuser4','testuser5'),(412,10.00,'2017-12-06 22:40:38','SuperUser','testuser4'),(413,200.00,'2017-12-06 22:40:38','testuser6','testuser5'),(414,10.00,'2017-12-06 22:40:38','SuperUser','testuser6'),(415,200.00,'2017-12-06 22:40:38','testuser11','testuser5'),(416,10.00,'2017-12-06 22:40:38','SuperUser','testuser11'),(417,30.00,'2017-12-06 22:40:38','SuperUser','testuser5'),(418,125.00,'2017-12-06 22:45:39','testuser4','testuser2'),(419,125.00,'2017-12-06 22:45:39','testuser6','testuser2'),(420,125.00,'2017-12-06 22:45:39','testuser4','testuser2'),(421,125.00,'2017-12-06 22:45:39','testuser6','testuser2'),(425,12.50,'2017-12-06 22:45:39','SuperUser','testuser4'),(426,12.50,'2017-12-06 22:45:39','SuperUser','testuser6'),(427,25.00,'2017-12-06 22:45:39','SuperUser','testuser2'),(428,200.00,'2017-12-06 22:45:39','testuser4','testuser5'),(429,10.00,'2017-12-06 22:45:40','SuperUser','testuser4'),(430,200.00,'2017-12-06 22:45:40','testuser6','testuser5'),(431,10.00,'2017-12-06 22:45:40','SuperUser','testuser6'),(432,200.00,'2017-12-06 22:45:40','testuser11','testuser5'),(433,10.00,'2017-12-06 22:45:40','SuperUser','testuser11'),(434,30.00,'2017-12-06 22:45:40','SuperUser','testuser5'),(435,125.00,'2017-12-07 13:13:55','testuser4','testuser2'),(436,125.00,'2017-12-07 13:13:55','testuser6','testuser2'),(437,125.00,'2017-12-07 13:13:55','testuser4','testuser2'),(438,125.00,'2017-12-07 13:13:55','testuser6','testuser2'),(442,12.50,'2017-12-07 13:13:55','SuperUser','testuser4'),(443,12.50,'2017-12-07 13:13:55','SuperUser','testuser6'),(444,25.00,'2017-12-07 13:13:55','SuperUser','testuser2'),(445,200.00,'2017-12-07 13:13:56','testuser4','testuser5'),(446,10.00,'2017-12-07 13:13:56','SuperUser','testuser4'),(447,200.00,'2017-12-07 13:13:56','testuser6','testuser5'),(448,10.00,'2017-12-07 13:13:56','SuperUser','testuser6'),(449,200.00,'2017-12-07 13:13:56','testuser11','testuser5'),(450,10.00,'2017-12-07 13:13:56','SuperUser','testuser11'),(451,30.00,'2017-12-07 13:13:56','SuperUser','testuser5'),(452,125.00,'2017-12-07 15:50:58','testuser4','testuser2'),(453,125.00,'2017-12-07 15:50:58','testuser6','testuser2'),(454,125.00,'2017-12-07 15:50:58','testuser4','testuser2'),(455,125.00,'2017-12-07 15:50:58','testuser6','testuser2'),(459,12.50,'2017-12-07 15:50:58','SuperUser','testuser4'),(460,12.50,'2017-12-07 15:50:58','SuperUser','testuser6'),(461,25.00,'2017-12-07 15:50:58','SuperUser','testuser2'),(462,200.00,'2017-12-07 15:50:59','testuser4','testuser5'),(463,10.00,'2017-12-07 15:50:59','SuperUser','testuser4'),(464,200.00,'2017-12-07 15:50:59','testuser6','testuser5'),(465,10.00,'2017-12-07 15:50:59','SuperUser','testuser6'),(466,200.00,'2017-12-07 15:50:59','testuser11','testuser5'),(467,10.00,'2017-12-07 15:50:59','SuperUser','testuser11'),(468,30.00,'2017-12-07 15:50:59','SuperUser','testuser5');
/*!40000 ALTER TABLE `TransactionHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TransactionPending`
--

DROP TABLE IF EXISTS `TransactionPending`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TransactionPending` (
  `transaction_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` decimal(8,2) DEFAULT NULL,
  `transaction_date` datetime NOT NULL,
  `receiver` varchar(64) DEFAULT NULL,
  `sender` varchar(64) DEFAULT NULL,
  `project_id` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `fk_transactionsender` (`receiver`),
  KEY `fk_transactionreceiver` (`sender`),
  KEY `transaction_id1` (`transaction_id`),
  KEY `fk_pendingtransactionproject` (`project_id`),
  CONSTRAINT `fk_pendingreceiver` FOREIGN KEY (`receiver`) REFERENCES `users` (`user_id`),
  CONSTRAINT `fk_pendingsender` FOREIGN KEY (`sender`) REFERENCES `users` (`user_id`),
  CONSTRAINT `fk_pendingtransactionproject` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=463 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TransactionPending`
--

LOCK TABLES `TransactionPending` WRITE;
/*!40000 ALTER TABLE `TransactionPending` DISABLE KEYS */;
/*!40000 ALTER TABLE `TransactionPending` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserInterests`
--

DROP TABLE IF EXISTS `UserInterests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserInterests` (
  `user_id` varchar(64) NOT NULL,
  `IOS` int(1) DEFAULT 0,
  `Android` int(1) DEFAULT 0,
  `DesktopApp` int(1) DEFAULT 0,
  `Java` int(1) DEFAULT 0,
  `Python` int(1) DEFAULT 0,
  `Cpp` int(1) DEFAULT 0,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_userinterst` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserInterests`
--

LOCK TABLES `UserInterests` WRITE;
/*!40000 ALTER TABLE `UserInterests` DISABLE KEYS */;
INSERT INTO `UserInterests` VALUES ('SuperUser',0,1,0,0,0,1),('testuser10',0,0,1,0,0,0),('testuser11',0,0,0,0,0,0),('testuser12',0,0,0,0,0,0),('testuser13',1,0,1,0,1,0),('testuser14',0,0,0,0,0,0),('testuser2',1,1,0,0,1,0),('testuser3',0,0,0,0,0,0),('testuser4',0,1,1,0,1,1),('testuser5',1,0,0,0,1,1),('testuser6',1,1,1,0,0,0),('testuser7',0,0,1,1,0,0),('testuser8',1,0,1,0,1,0),('testuser9',0,0,1,1,1,1);
/*!40000 ALTER TABLE `UserInterests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `user_id` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  `user_type` int(1) NOT NULL,
  `balance` decimal(8,2) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `warnings` int(1) DEFAULT 0,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('SuperUser','',0,103790.00,'','',0),('testuser10','',2,10000.00,'','',0),('testuser11','',2,22560.00,'','',0),('testuser12','',2,10000.00,'','',0),('testuser13','',2,500.00,'','',0),('testuser14','',2,500.00,'','',0),('testuser2','',1,73475.00,'123 40th St. Queens, NY','testuser@gmail.com',0),('testuser3','',1,2000.00,'123 40th St. Queens, NY','testuser@gmail.com',0),('testuser4','password',2,37410.00,'456 70th Street, Queens, NY','testuser4@gmail.com',0),('testuser5','',1,83380.00,'testuser5@gmail.com','100 Convent Ave. NY, NY',0),('testuser6','',2,37422.50,'100 Convent Ave. NY, NY','testuser6@gmail.com',0),('testuser7','',1,10000.00,'','',0),('testuser8','',1,10000.00,'','',0),('testuser9','',1,10000.00,'','',0);
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger insert_dev
after insert on users
for each row
begin
if NEW.user_type = 2 then
  insert Developers (user_id) values (NEW.user_id);
  end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger insert_client
after insert on users
for each row
begin
if NEW.user_type = 1 then
  insert Clients values (NEW.user_id, NULL);
  end if;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger insertInterests after insert on Users for each row insert UserInterests (user_id) values (NEW.user_id) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `application`
--

DROP TABLE IF EXISTS `application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `application` (
  `user_id` varchar(64) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_applications` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `application`
--

LOCK TABLES `application` WRITE;
/*!40000 ALTER TABLE `application` DISABLE KEYS */;
INSERT INTO `application` VALUES ('testuser13'),('testuser14');
/*!40000 ALTER TABLE `application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `finished_individual_project`
--

DROP TABLE IF EXISTS `finished_individual_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `finished_individual_project` (
  `project_id` varchar(64) NOT NULL,
  `dev_id` varchar(64) DEFAULT NULL,
  `bid` decimal(8,2) DEFAULT NULL,
  `date_submit` datetime DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `fk_Finished_IndivProjDev` (`dev_id`),
  CONSTRAINT `fk_Finished_IndivProjDev` FOREIGN KEY (`dev_id`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_Finished_IndivProjId` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finished_individual_project`
--

LOCK TABLES `finished_individual_project` WRITE;
/*!40000 ALTER TABLE `finished_individual_project` DISABLE KEYS */;
INSERT INTO `finished_individual_project` VALUES ('proj6','testuser10',200.00,NULL);
/*!40000 ALTER TABLE `finished_individual_project` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger individualprojectfinish after insert on Finished_Individual_Project for each row begin
update Projects set project_status = "Finished" where project_id = NEW.project_id;
delete from Current_Individual_Project where project_id = NEW.project_id;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `finished_team_project`
--

DROP TABLE IF EXISTS `finished_team_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `finished_team_project` (
  `project_id` varchar(64) NOT NULL,
  `teamrating` int(1) DEFAULT NULL,
  `team_id` varchar(64) DEFAULT NULL,
  `teamreview` varchar(128) DEFAULT NULL,
  `bid` decimal(8,2) DEFAULT NULL,
  `date_submit` datetime DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `fk_FinishedTeamProjectTeam` (`team_id`),
  CONSTRAINT `fk_FinishedTeamProjectId` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_FinishedTeamProjectTeam` FOREIGN KEY (`team_id`) REFERENCES `Teams` (`team_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finished_team_project`
--

LOCK TABLES `finished_team_project` WRITE;
/*!40000 ALTER TABLE `finished_team_project` DISABLE KEYS */;
INSERT INTO `finished_team_project` VALUES ('proj5',NULL,'testteam1',NULL,100.00,NULL),('testproject',5,'testteam1','Good Project',500.00,'2017-12-07 15:50:58'),('testproject2',3,'testteam2','Bad Review',600.00,'2017-12-07 15:50:59');
/*!40000 ALTER TABLE `finished_team_project` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger teamprojectfinish after insert on Finished_Team_Project for each row begin
delete from Current_Team_Project where project_id = NEW.project_id;
update Projects set project_status = "Finished" where project_id = NEW.project_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `sender` varchar(64) DEFAULT NULL,
  `receiver` varchar(64) DEFAULT NULL,
  `message` varchar(128) DEFAULT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`time`),
  KEY `fk_messagereceiver` (`receiver`),
  KEY `fk_messagesender` (`sender`),
  CONSTRAINT `fk_messagereceiver` FOREIGN KEY (`receiver`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_messagesender` FOREIGN KEY (`sender`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES ('testuser4','testuser6','testmessage','2017-12-02 00:00:00'),('testuser4','testuser6','testmessage','2017-12-04 23:40:03'),('testuser4','testuser6','testmessage','2017-12-05 00:26:35'),('testuser4','testuser6','testmessage','2017-12-05 01:29:04'),('testuser4','testuser6','testmessage','2017-12-05 01:29:35'),('testuser4','testuser6','testmessage','2017-12-05 01:29:50'),('testuser4','testuser6','testmessage','2017-12-05 01:29:54'),('testuser4','testuser6','testmessage','2017-12-05 13:08:47'),('testuser4','testuser6','testmessage','2017-12-05 13:10:32'),('testuser4','testuser6','testmessage','2017-12-05 13:11:11'),('testuser4','testuser6','testmessage','2017-12-05 13:15:26'),('testuser4','testuser6','testmessage','2017-12-05 13:23:34'),('testuser4','testuser6','testmessage','2017-12-05 13:25:38'),('testuser4','testuser6','testmessage','2017-12-05 13:26:42'),('testuser4','testuser6','testmessage','2017-12-05 13:29:15'),('testuser4','testuser6','testmessage','2017-12-05 13:48:57'),('testuser4','testuser6','testmessage','2017-12-05 17:39:58'),('testuser4','testuser6','testmessage','2017-12-05 17:40:07'),('testuser4','testuser6','testmessage','2017-12-06 13:09:38'),('testuser4','testuser6','testmessage','2017-12-06 13:10:13'),('testuser4','testuser6','testmessage','2017-12-06 13:18:46'),('testuser4','testuser6','testmessage','2017-12-06 13:23:24'),('testuser4','testuser6','testmessage','2017-12-06 13:29:35'),('testuser4','testuser6','testmessage','2017-12-06 13:31:09'),('testuser4','testuser6','testmessage','2017-12-06 13:48:03'),('testuser4','testuser6','testmessage','2017-12-06 13:59:02'),('testuser4','testuser6','testmessage','2017-12-06 15:26:55'),('testuser4','testuser6','testmessage','2017-12-06 15:28:32'),('testuser4','testuser6','testmessage','2017-12-06 15:30:25'),('testuser4','testuser6','testmessage','2017-12-06 15:31:15'),('testuser4','testuser6','testmessage','2017-12-06 15:31:25'),('testuser4','testuser6','testmessage','2017-12-06 15:32:28'),('testuser4','testuser6','testmessage','2017-12-06 15:44:29'),('testuser4','testuser6','testmessage','2017-12-06 17:17:21'),('testuser4','testuser6','testmessage','2017-12-06 19:50:44'),('testuser4','testuser6','testmessage','2017-12-06 19:57:11'),('testuser4','testuser6','testmessage','2017-12-06 20:18:06'),('testuser4','testuser6','testmessage','2017-12-06 21:57:27'),('testuser4','testuser6','testmessage','2017-12-06 21:58:05'),('testuser4','testuser6','testmessage','2017-12-06 21:58:20'),('testuser4','testuser6','testmessage','2017-12-06 21:59:58'),('testuser4','testuser6','testmessage','2017-12-06 22:13:42'),('testuser4','testuser6','testmessage','2017-12-06 22:14:32'),('testuser4','testuser6','testmessage','2017-12-06 22:14:48'),('testuser4','testuser6','testmessage','2017-12-06 22:22:11'),('testuser4','testuser6','testmessage','2017-12-06 22:22:25'),('testuser4','testuser6','testmessage','2017-12-06 22:23:50'),('testuser4','testuser6','testmessage','2017-12-06 22:24:31'),('testuser4','testuser6','testmessage','2017-12-06 22:24:48'),('testuser4','testuser6','testmessage','2017-12-06 22:25:25'),('testuser4','testuser6','testmessage','2017-12-06 22:27:24'),('testuser4','testuser6','testmessage','2017-12-06 22:30:15'),('testuser4','testuser6','testmessage','2017-12-06 22:30:28'),('testuser4','testuser6','testmessage','2017-12-06 22:31:24'),('testuser4','testuser6','testmessage','2017-12-06 22:32:50'),('testuser4','testuser6','testmessage','2017-12-06 22:32:58'),('testuser4','testuser6','testmessage','2017-12-06 22:34:30'),('testuser4','testuser6','testmessage','2017-12-06 22:36:43'),('testuser4','testuser6','testmessage','2017-12-06 22:37:06'),('testuser4','testuser6','testmessage','2017-12-06 22:40:38'),('testuser4','testuser6','testmessage','2017-12-06 22:45:40'),('testuser4','testuser6','testmessage','2017-12-07 13:13:56'),('testuser4','testuser6','testmessage','2017-12-07 15:50:59');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects` (
  `project_id` varchar(64) NOT NULL,
  `client_id` varchar(64) DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `project_status` varchar(32) DEFAULT NULL,
  `project_type` varchar(32) DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  `date_posted` datetime DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `fk_ProjectClient` (`client_id`),
  CONSTRAINT `fk_ProjectClient` FOREIGN KEY (`client_id`) REFERENCES `Clients` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES ('0','testuser2',NULL,'Pending',NULL,'2017-12-31','2017-12-07 13:07:37'),('1','testuser2',NULL,'Pending',NULL,'2017-12-31','2017-12-07 13:07:37'),('2','testuser5',NULL,'Pending',NULL,'2017-12-31','2017-12-07 13:07:37'),('3','testuser8','description','Pending',NULL,'2017-12-30','2017-12-07 13:07:37'),('4','testuser9','','Pending',NULL,'2017-12-31','2017-12-07 13:07:37'),('currentteam1project','testuser2','','Current','Team','2017-12-30','2017-12-07 13:07:37'),('proj5','testuser2','','Finished','Team','2017-12-15','2017-12-07 13:07:37'),('proj6','testuser2','','Finished','Individual','2017-12-15','2017-12-07 13:07:37'),('testcurrentproject','testuser2','','Current','Individual','2017-12-30','2017-12-07 13:07:37'),('testproject','testuser2','testproject','Finished','Team','2017-12-30','2017-12-07 15:50:58'),('testproject2','testuser5','testproject2','Finished','Team','2017-12-29','2017-12-07 15:50:59');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teamreviews`
--

DROP TABLE IF EXISTS `teamreviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teamreviews` (
  `dev_id` varchar(64) NOT NULL,
  `receiver_id` varchar(64) NOT NULL,
  `review` varchar(256) DEFAULT NULL,
  `rating` int(1) DEFAULT NULL,
  `team_id` varchar(64) NOT NULL,
  PRIMARY KEY (`dev_id`,`receiver_id`,`team_id`),
  KEY `fk_TeamReviewReceiver` (`receiver_id`),
  KEY `fk_teamreviewteam` (`team_id`),
  CONSTRAINT `fk_TeamReviewReceiver` FOREIGN KEY (`receiver_id`) REFERENCES `Developers` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_TeamReviewSender` FOREIGN KEY (`dev_id`) REFERENCES `Developers` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_teamreviewteam` FOREIGN KEY (`team_id`) REFERENCES `Teams` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teamreviews`
--

LOCK TABLES `teamreviews` WRITE;
/*!40000 ALTER TABLE `teamreviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `teamreviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-07 15:54:36
