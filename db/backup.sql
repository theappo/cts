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
-- Table structure for table `Application`
--

DROP TABLE IF EXISTS `Application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Application` (
  `user_id` varchar(64) NOT NULL,
  `deposit` decimal(8,2) DEFAULT NULL,
  `type` int(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_applications` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Application`
--

LOCK TABLES `Application` WRITE;
/*!40000 ALTER TABLE `Application` DISABLE KEYS */;
/*!40000 ALTER TABLE `Application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BlackList`
--

DROP TABLE IF EXISTS `BlackList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BlackList` (
  `user_id` varchar(64) NOT NULL,
  `ban_date` date DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_blacklist` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BlackList`
--

LOCK TABLES `BlackList` WRITE;
/*!40000 ALTER TABLE `BlackList` DISABLE KEYS */;
/*!40000 ALTER TABLE `BlackList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Clients`
--

DROP TABLE IF EXISTS `Clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Clients` (
  `user_id` varchar(64) NOT NULL,
  `avgrating` decimal(4,3) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_clientuser` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clients`
--

LOCK TABLES `Clients` WRITE;
/*!40000 ALTER TABLE `Clients` DISABLE KEYS */;
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
  `developer_id` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `fk_CurrentIndivProjDev` (`developer_id`),
  CONSTRAINT `fk_CurrentIndivProjDev` FOREIGN KEY (`developer_id`) REFERENCES `Developers` (`user_id`),
  CONSTRAINT `fk_CurrentIndivProjId` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Current_Individual_Project`
--

LOCK TABLES `Current_Individual_Project` WRITE;
/*!40000 ALTER TABLE `Current_Individual_Project` DISABLE KEYS */;
/*!40000 ALTER TABLE `Current_Individual_Project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Current_Team_Project`
--

DROP TABLE IF EXISTS `Current_Team_Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Current_Team_Project` (
  `project_id` varchar(64) NOT NULL,
  `team_id` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`project_id`),
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
/*!40000 ALTER TABLE `Current_Team_Project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Developers`
--

DROP TABLE IF EXISTS `Developers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Developers` (
  `user_id` varchar(64) NOT NULL,
  `avgrating` decimal(4,3) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_devuser` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Developers`
--

LOCK TABLES `Developers` WRITE;
/*!40000 ALTER TABLE `Developers` DISABLE KEYS */;
/*!40000 ALTER TABLE `Developers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Finished_Individual_Project`
--

DROP TABLE IF EXISTS `Finished_Individual_Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Finished_Individual_Project` (
  `project_id` varchar(64) NOT NULL,
  `dev_id` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `fk_Finished_IndivProjDev` (`dev_id`),
  CONSTRAINT `fk_Finished_IndivProjDev` FOREIGN KEY (`dev_id`) REFERENCES `Developers` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_Finished_IndivProjId` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Finished_Individual_Project`
--

LOCK TABLES `Finished_Individual_Project` WRITE;
/*!40000 ALTER TABLE `Finished_Individual_Project` DISABLE KEYS */;
/*!40000 ALTER TABLE `Finished_Individual_Project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Finished_Team_Project`
--

DROP TABLE IF EXISTS `Finished_Team_Project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Finished_Team_Project` (
  `project_id` varchar(64) NOT NULL,
  `teamrating` int(1) DEFAULT NULL,
  `team_id` varchar(64) DEFAULT NULL,
  `teamreview` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `fk_FinishedTeamProjectTeam` (`team_id`),
  CONSTRAINT `fk_FinishedTeamProjectId` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_FinishedTeamProjectTeam` FOREIGN KEY (`team_id`) REFERENCES `Teams` (`team_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Finished_Team_Project`
--

LOCK TABLES `Finished_Team_Project` WRITE;
/*!40000 ALTER TABLE `Finished_Team_Project` DISABLE KEYS */;
/*!40000 ALTER TABLE `Finished_Team_Project` ENABLE KEYS */;
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
/*!40000 ALTER TABLE `Individual_Bid_Project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Messages`
--

DROP TABLE IF EXISTS `Messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Messages` (
  `message_id` int(11) NOT NULL,
  `sender` varchar(64) DEFAULT NULL,
  `receiver` varchar(64) DEFAULT NULL,
  `message` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`message_id`),
  KEY `fk_messagereceiver` (`receiver`),
  KEY `fk_messagesender` (`sender`),
  CONSTRAINT `fk_messagereceiver` FOREIGN KEY (`receiver`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_messagesender` FOREIGN KEY (`sender`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Messages`
--

LOCK TABLES `Messages` WRITE;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `Messages` ENABLE KEYS */;
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
  CONSTRAINT `fk_ReviewsProjectId` FOREIGN KEY (`project_id`) REFERENCES `Projects` (`project_id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_ReviewsReceiver` FOREIGN KEY (`receiver_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `fk_ReviewsSender` FOREIGN KEY (`sender_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProjectReviews`
--

LOCK TABLES `ProjectReviews` WRITE;
/*!40000 ALTER TABLE `ProjectReviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `ProjectReviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Projects`
--

DROP TABLE IF EXISTS `Projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Projects` (
  `project_id` varchar(64) NOT NULL,
  `client_id` varchar(64) DEFAULT NULL,
  `description` varchar(64) DEFAULT NULL,
  `project_status` varchar(32) DEFAULT NULL,
  `project_type` varchar(32) DEFAULT NULL,
  `deadline` date DEFAULT NULL,
  PRIMARY KEY (`project_id`),
  KEY `fk_ProjectClient` (`client_id`),
  CONSTRAINT `fk_ProjectClient` FOREIGN KEY (`client_id`) REFERENCES `Clients` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Projects`
--

LOCK TABLES `Projects` WRITE;
/*!40000 ALTER TABLE `Projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `Projects` ENABLE KEYS */;
UNLOCK TABLES;

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
/*!40000 ALTER TABLE `TeamHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeamReviews`
--

DROP TABLE IF EXISTS `TeamReviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TeamReviews` (
  `dev_id` varchar(64) NOT NULL,
  `receiver_id` varchar(64) NOT NULL,
  `review` varchar(256) DEFAULT NULL,
  `rating` int(1) DEFAULT NULL,
  PRIMARY KEY (`dev_id`,`receiver_id`),
  KEY `fk_TeamReviewReceiver` (`receiver_id`),
  CONSTRAINT `fk_TeamReviewReceiver` FOREIGN KEY (`receiver_id`) REFERENCES `Developers` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_TeamReviewSender` FOREIGN KEY (`dev_id`) REFERENCES `Developers` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeamReviews`
--

LOCK TABLES `TeamReviews` WRITE;
/*!40000 ALTER TABLE `TeamReviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `TeamReviews` ENABLE KEYS */;
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
/*!40000 ALTER TABLE `Teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TransactionHistory`
--

DROP TABLE IF EXISTS `TransactionHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TransactionHistory` (
  `transaction_id` int(11) NOT NULL,
  `amount` decimal(8,2) DEFAULT NULL,
  `transaction_date` datetime DEFAULT NULL,
  `receiver` varchar(64) DEFAULT NULL,
  `sender` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `fk_transactionsender` (`receiver`),
  KEY `fk_transactionreceiver` (`sender`),
  CONSTRAINT `fk_transactionreceiver` FOREIGN KEY (`sender`) REFERENCES `Users` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_transactionsender` FOREIGN KEY (`receiver`) REFERENCES `Users` (`user_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TransactionHistory`
--

LOCK TABLES `TransactionHistory` WRITE;
/*!40000 ALTER TABLE `TransactionHistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `TransactionHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserInterests`
--

DROP TABLE IF EXISTS `UserInterests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserInterests` (
  `user_id` varchar(64) NOT NULL,
  `interest` varchar(32) NOT NULL,
  PRIMARY KEY (`user_id`,`interest`),
  CONSTRAINT `fk_userinterst` FOREIGN KEY (`user_id`) REFERENCES `Users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserInterests`
--

LOCK TABLES `UserInterests` WRITE;
/*!40000 ALTER TABLE `UserInterests` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserInterests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` varchar(64) NOT NULL,
  `password` varchar(64) NOT NULL,
  `user_type` int(1) NOT NULL,
  `balance` decimal(8,2) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('testuser2','password2',1,NULL,NULL,NULL),('testuser3','password3',1,1000.00,NULL,NULL),('testuser4','',2,500.00,NULL,NULL);
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

-- Dump completed on 2017-11-21 16:45:44
