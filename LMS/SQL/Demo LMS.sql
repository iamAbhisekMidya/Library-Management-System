-- MariaDB dump 10.19  Distrib 10.4.22-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: lms
-- ------------------------------------------------------
-- Server version	10.4.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `books_details`
--

DROP TABLE IF EXISTS `books_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_details` (
  `book_name` varchar(100) NOT NULL,
  `book_sub` varchar(20) NOT NULL,
  `author` varchar(20) NOT NULL,
  `shelf_no` varchar(5) NOT NULL,
  `no_book` int(11) NOT NULL,
  `rem_book` int(11) NOT NULL,
  `id_counter` int(11) NOT NULL,
  PRIMARY KEY (`book_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_details`
--

LOCK TABLES `books_details` WRITE;
/*!40000 ALTER TABLE `books_details` DISABLE KEYS */;
INSERT INTO `books_details` VALUES ('C++ Programming An Object Oriented Approach By Behrouz A. Forouzan','C++ Programing','Behrouz A. Forouzan','A1',3,1,601),('Computer System Architecture By Morris Mano','Architecture','Morris Mano','B1',3,3,301),('Core Java By Nageswara Rao','Java','Nageswara Rao','A1',4,3,1301),('Core Python By Nageswara Rao','Python','Nageswara Rao','B3',4,2,1901),('Data Communications And Networking By Behrouz A. Forouzan','Networking','Behrouz A. Forouzan','B3',4,2,1501),('Data Mining Concepts And Techniques By Jiawei Han','Data Mining','Jiawei Han','B2',2,0,901),('Data Structures Using C By E. Balagurusamy','C Programing','E. Balagurusamy','A2',4,4,701),('Database System Concepts By F.Korth','Dbms','F.Korth','B1',4,3,801),('Digital Image Processing By Richard E. Woods','Image Processing','Richard E. Woods','C1',2,2,1101),('Digital Logic And Computer Design By Morris Mano','Digital','Morris Mano','C1',3,3,1001),('Fundamentals Of Computer Algorithms By Sartaj Sahni','Algorithms','Sartaj Sahni','B1',3,3,101),('Introduction To Algorithms By Thomas H. Cormen','Algorithms','Thomas H. Cormen','B1',3,3,201),('Introduction To Cryptography And Network Security By Behrouz A. Forouzan','Information Security','Behrouz A. Forouzan','B3',1,1,1201),('Java The Complete Reference By Herbert Schildt','Java','Herbert Schildt','A2',2,2,1401),('Learn Python 3 The Hard Way By Zed A. Shaw','Python','Zed A. Shaw','A1',2,2,2001),('Let Us C By Yashavant Kanetkar','C Programing','Yashavant Kanetkar','C1',4,4,501),('Let Us Java By Yashavant Kanetkar','Java','Yashavant Kanetkar','C2',4,4,1601),('Microprocessor Architecture With The 8085 By Ramesh Gaonkar','Microprocessor 8085','Ramesh Gaonkar','C2',3,2,1701),('Operating System Concepts By P.B Galvin','Operating System','P.B Galvin','C3',4,4,1801),('Programming In Ansi C By E. Balagurusamy','C Programing','E. Balagurusamy','C3',4,2,401),('Unix Shell Programming By Yashwant Kanitkar','Shell Programming','Yashwant Kanitkar','C2',3,2,2101);
/*!40000 ALTER TABLE `books_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue_book`
--

DROP TABLE IF EXISTS `issue_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `issue_book` (
  `ref_no` varchar(30) NOT NULL,
  `member_id` int(11) NOT NULL,
  `book_id` varchar(10) NOT NULL,
  `book_name` varchar(100) NOT NULL,
  `book_ed` varchar(10) NOT NULL,
  `issue_date` date NOT NULL,
  `due_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  PRIMARY KEY (`ref_no`,`book_name`),
  UNIQUE KEY `ref_no` (`ref_no`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `issue_book_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member_details` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_book`
--

LOCK TABLES `issue_book` WRITE;
/*!40000 ALTER TABLE `issue_book` DISABLE KEYS */;
INSERT INTO `issue_book` VALUES ('1000120220514',10001,'1902','Core Python By Nageswara Rao','3rd','2022-05-14','2022-06-15',NULL),('1000220220514',10002,'403','Programming In Ansi C By E. Balagurusamy','6th','2022-05-14','2022-05-30',NULL),('1000320220514',10003,'404','Programming In Ansi C By E. Balagurusamy','4th','2022-05-14','2022-05-30',NULL),('1000420220514',10004,'1304','Core Java By Nageswara Rao','5th','2022-05-14','2022-06-15',NULL),('1000520220514',10005,'902','Data Mining Concepts And Techniques By Jiawei Han','6th','2022-05-14','2022-05-29',NULL),('1000620220514',10006,'1502','Data Communications And Networking By Behrouz A. Forouzan','3rd','2022-05-14','2022-05-25',NULL),('1000920220514',10009,'1702','Microprocessor Architecture With The 8085 By Ramesh Gaonkar','5th','2022-05-14','2022-06-01',NULL),('1001520220514',10015,'803','Database System Concepts By F.Korth','13th','2022-05-14','2022-05-20',NULL),('1001820220514',10018,'2103','Unix Shell Programming By Yashwant Kanitkar','2nd','2022-05-14','2022-05-29',NULL),('1003020220514',10030,'602','C++ Programming An Object Oriented Approach By Behrouz A. Forouzan','15th','2022-05-14','2022-06-05',NULL);
/*!40000 ALTER TABLE `issue_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lost_book`
--

DROP TABLE IF EXISTS `lost_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lost_book` (
  `book_id` varchar(10) NOT NULL,
  `book_name` varchar(100) NOT NULL,
  `lost_date` date DEFAULT NULL,
  PRIMARY KEY (`book_id`),
  KEY `book_name` (`book_name`),
  CONSTRAINT `lost_book_ibfk_1` FOREIGN KEY (`book_name`) REFERENCES `books_details` (`book_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lost_book`
--

LOCK TABLES `lost_book` WRITE;
/*!40000 ALTER TABLE `lost_book` DISABLE KEYS */;
/*!40000 ALTER TABLE `lost_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_details`
--

DROP TABLE IF EXISTS `member_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_details` (
  `member_type` varchar(10) NOT NULL,
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `address` varchar(50) NOT NULL,
  `dept` varchar(30) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `amount` int(11) NOT NULL DEFAULT 0,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`member_id`),
  UNIQUE KEY `mail` (`mail`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=10031 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_details`
--

LOCK TABLES `member_details` WRITE;
/*!40000 ALTER TABLE `member_details` DISABLE KEYS */;
INSERT INTO `member_details` VALUES ('Student',10001,'Abhisek','Midya','49/4 Garfa','B.Sc Computer Science','mid.abhi2000@gmail.com','7980609462',5000,'abhi'),('Student',10002,'Ahin','Subhra Haldar','78 Garia','B.Sc Computer Science','ahinsubhrahalder@gmail.com','6294580369',4000,'ahin'),('Student',10003,'Atish','Sarkar','191 Banerjee Para Road','B.Sc Computer Science','atish8972407182@gmail.com','8972407182',500,'Atish8972'),('Teacher',10004,'Aparna','Kisku Hansda','Jadavpur','B.Sc Computer Science','aparnakh19@gmail.com','9474879487',5000,'zOuKljQX'),('Student',10005,'Avijit','Halder','Kakdwip','B.Sc Computer Science','avijithalder15834@gmail.com','7384127333',5000,'VLqIOaPV'),('Student',10006,'Shibam','Saha','Kolkata','B.Sc Computer Science','shibamsaha001@gmail.com','7384122335',1000,'RpnJwipr'),('Student',10007,'Sayan ','Sikhdar','Kakdwip','B.Sc Computer Science','sayansikhdar152@gmail.com','9832514500',1100,'JHZBdXfK'),('Teacher',10008,'Ritwik','Sinha','Kolkata,Sreenagar','B.Sc Computer Science','sinharitwik2000@gmail.com','9333851200',2000,'DfiIqyJA'),('Student',10009,'Soumyadip','Maity','Kolkata','B.Sc Computer Science','soumyadipmaity111@gmail.com','8001572005',2500,'xMUlJqSy'),('Student',10010,'Subhaeep','Biswas','Kolkata','B.Sc Computer Science','subhadeepbiswas1588@gmail.com','9365814739',2500,'KWoaVlPU'),('Student',10011,'Soumyadip','Muniyan','Kolkata','B.Sc Computer Science','muniyansoumyadip12@gmail.com','9675148563',1500,'OLCVbqeH'),('Student',10012,'Sammohan','Maity','Kolkata','B.Sc Computer Science','maitysammy1999@gmail.com','9615278235',1700,'hhrzCYGB'),('Student',10013,'Gopal','Das','Kolkata','B.Sc Mathematics','gopudas156@gmail.com','7385128992',1900,'AaOFdlLb'),('Student',10014,'Bikki','Shaw','Kolkata','B.Sc Mathematics','bikkishaw2001@gmail.com','7384259758',2000,'NEITHJbq'),('Student',10015,'Roshan','Sharma','Kolkata','B.Sc Mathematics','roshansharma2001@gmail.com','9956841237',2500,'HedWujsc'),('Student',10016,'Bibek','Das','Kolkata','B.Com Commerce','bibekdas1998@gmail.com','9863147598',2500,'LafPjACp'),('Student',10017,'Aditya','Singh','Kolkata','B.A English','adityasingh2589@gmai.com','9645718278',1000,'OvEdpJXU'),('Student',10018,'Tuhin','Das','Kolkata','B.Sc Electronics','dastuhin1996@gmail.com','9863147589',2000,'AsolWBvm'),('Student',10019,'Anindya','Panda','Kakdwip','B.Sc Biological Science','aniindyapanda2001@gmail.com','9687563687',2500,'MOotQYjF'),('Student',10020,'Swarup','Das','Kolkata','B.Sc Electronics','swarupdas2005@gmail.com','8956175643',2500,'cIsSawvw'),('Student',10021,'Subha','Shil','Kakdwip','B.Sc Economics','subhashil007@gmail.com','8946713546',2500,'ngWRWMzM'),('Student',10022,'Sayan','Shil','Kakdwip','B.Sc Geography','sayanshil009@gmail.com','7896541256',2500,'mxghZubL'),('Student',10023,'Debmalya','Das','Kakdwip','B.Sc Geography','debudas0099@gmail.com','7849658134',2500,'ZpcFHQet'),('Student',10024,'Bijoy','Saho','Kolkata','B.Com Commerce','sahobijoy12345@gmail.com','9841237892',2500,'ItyJgpeI'),('Student',10025,'Binoy','Maity','Kolkata','B.Sc Electronics','binoysaho0077@gmail.com','8974651354',1500,'zaLAJPWF'),('Student',10026,'Ankan','Maity','Kakdwip','B.Sc Economics','ankanmaity0010@gmail.com','8641257390',2000,'uIwUUoqr'),('Student',10027,'Aritra','Maity','Kakdwip','B.Sc Biological Science','aritramaity00123@gmail.com','7599461348',1500,'vNCffhSY'),('Student',10028,'Souvik','Das','Kakdwip','B.Sc Geography','dassouvik1589@gmail.com','7345197986',1500,'YJuoWoJE'),('Student',10029,'Santanu','Das','Kakdwip','B.A Bengali','santanudas00123@gmail.com','8735124678',1500,'zhMNlOYC'),('Student',10030,'Animesh','Jana','Kakdwip','B.Sc Geography','janaanimesh123789@gmail.com','7364125789',1500,'blfqtAam');
/*!40000 ALTER TABLE `member_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pending`
--

DROP TABLE IF EXISTS `pending`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pending` (
  `member_id` int(11) NOT NULL,
  `ref_no` varchar(30) NOT NULL,
  `book_id` varchar(10) NOT NULL,
  PRIMARY KEY (`member_id`),
  CONSTRAINT `pending_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member_details` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pending`
--

LOCK TABLES `pending` WRITE;
/*!40000 ALTER TABLE `pending` DISABLE KEYS */;
INSERT INTO `pending` VALUES (10001,'1000120220514','1902'),(10002,'1000220220514','403'),(10003,'1000320220514','404'),(10004,'1000420220514','1304'),(10005,'1000520220514','902'),(10006,'1000620220514','1502'),(10009,'1000920220514','1702'),(10015,'1001520220514','803'),(10018,'1001820220514','2103'),(10030,'1003020220514','602');
/*!40000 ALTER TABLE `pending` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `serial`
--

DROP TABLE IF EXISTS `serial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `serial` (
  `ref_no` varchar(30) NOT NULL,
  `sr_no` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sr_no`),
  KEY `ref_no` (`ref_no`),
  CONSTRAINT `serial_ibfk_1` FOREIGN KEY (`ref_no`) REFERENCES `issue_book` (`ref_no`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serial`
--

LOCK TABLES `serial` WRITE;
/*!40000 ALTER TABLE `serial` DISABLE KEYS */;
INSERT INTO `serial` VALUES ('1000120220514',10),('1000220220514',9),('1000320220514',6),('1000420220514',7),('1000520220514',8),('1000620220514',1),('1000920220514',3),('1001520220514',4),('1001820220514',5),('1003020220514',2);
/*!40000 ALTER TABLE `serial` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-14 12:40:32
