-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 23, 2023 at 03:58 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ticketing`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline`
--

CREATE TABLE `airline` (
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airline`
--

INSERT INTO `airline` (`name`) VALUES
('Jet Blue'),
('Korean Air');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff`
--

CREATE TABLE `airline_staff` (
  `username` varchar(255) NOT NULL,
  `airline_name` varchar(255) NOT NULL,
  `password` varchar(32) DEFAULT NULL,
  `f_name` varchar(255) DEFAULT NULL,
  `l_name` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airline_staff`
--

INSERT INTO `airline_staff` (`username`, `airline_name`, `password`, `f_name`, `l_name`, `dob`) VALUES
('Nook', 'Korean Air', '1234', 'Nook', 'Damn', '2000-01-01'),
('staff123', 'Jet Blue', 'password', 'Jet', 'Blue', '2000-01-19'),
('staff33', 'Korean Air', 'Staff33', 'Jong Un', 'Kim', '1992-01-01');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff_email`
--

CREATE TABLE `airline_staff_email` (
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airline_staff_email`
--

INSERT INTO `airline_staff_email` (`username`, `email`) VALUES
('Nook', 'nook@koreanair.com'),
('staff123', 'staff@jetblue.com'),
('staff33', 'staff33@koreanair.com');

-- --------------------------------------------------------

--
-- Table structure for table `airline_staff_phone_num`
--

CREATE TABLE `airline_staff_phone_num` (
  `username` varchar(255) NOT NULL,
  `num` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airline_staff_phone_num`
--

INSERT INTO `airline_staff_phone_num` (`username`, `num`) VALUES
('Nook', '9175655974'),
('staff123', '0123456789'),
('staff33', '9189132394');

-- --------------------------------------------------------

--
-- Table structure for table `airplane`
--

CREATE TABLE `airplane` (
  `id` varchar(10) NOT NULL,
  `airline_name` varchar(255) NOT NULL,
  `num_seats` int(11) DEFAULT NULL,
  `manufacturer` varchar(255) DEFAULT NULL,
  `manufacture_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airplane`
--

INSERT INTO `airplane` (`id`, `airline_name`, `num_seats`, `manufacturer`, `manufacture_date`) VALUES
('KR245RK', 'Korean Air', 100, 'Boeing', '2020-01-01'),
('N0123BK', 'Jet Blue', 189, 'Boeing', '2023-01-01'),
('N1234YK', 'Jet Blue', 8, 'Airbus', '2023-03-07'),
('N1451KK', 'Jet Blue', 114, 'Boeing', '1981-01-01'),
('N2345TK', 'Jet Blue', 114, 'Boeing', '1997-01-01');

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `code` varchar(3) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `type` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`code`, `name`, `city`, `country`, `type`) VALUES
('ICN', 'Incheon Internation Airport', 'Incheon', 'Republic of Korea', 2),
('JFK', 'John F. Kennedy Airport', 'New York', 'United States', 2),
('LAX', 'Los Angeles Airport', 'Los Angeles', 'United States of America', 2),
('PVG', 'Shanghai Pudong International Airport', 'Shanghai', 'China', 2);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `email` varchar(255) NOT NULL,
  `password` varchar(32) DEFAULT NULL,
  `f_name` varchar(255) DEFAULT NULL,
  `l_name` varchar(255) DEFAULT NULL,
  `bldg_num` int(11) DEFAULT NULL,
  `st_name` varchar(255) DEFAULT NULL,
  `apt_num` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `passport_num` varchar(9) DEFAULT NULL,
  `passport_exp` date DEFAULT NULL,
  `passport_country` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`email`, `password`, `f_name`, `l_name`, `bldg_num`, `st_name`, `apt_num`, `city`, `state`, `zip_code`, `passport_num`, `passport_exp`, `passport_country`, `dob`) VALUES
('aSmith@jetblue.com', 'aSmith', 'Adam', 'Smith', 3, 'Bond Street', '11E', 'New York', 'New York', '10213', 'M123449', '2024-07-07', 'United States of America', '1997-07-01'),
('hk2994@nyu.edu', 'hk2994nyu', 'Brian', 'Kim', 437, 'Franklin Ave', '2F', 'Brooklyn', 'NY', '11238', 'M12345678', '2023-07-25', 'Republic of Korea', '2000-01-19'),
('jamesBond@gmail.com', '1234', 'James', 'Bond', 23, 'Bon Street', '34B', 'New York', 'New York', '10001', 'M104212', '1991-01-01', 'United States of America', '2024-05-05'),
('lz1111@nyu.edu', 'password', 'hoshi', 'kim', 42, 'west 32rd', '1b', 'new york', 'ny', '10001', 'M123456', '2028-05-05', 'Nigeria', '2001-07-07'),
('tk2316@nyu.edu', 'tk2316nyu', 'Taehun', 'Kim', 42, 'W 33rd St', '23', 'New York', 'NY', '10001', 'M11223344', '2023-07-25', 'Republic of Korea', '1997-07-09'),
('yk1234@nyu.edu', 'yk1234nyu', 'Yujeong', 'Kim', 437, 'Franklin Ave', '2F', 'Brooklyn', 'NY', '11238', 'M87654321', '2023-07-25', 'Republic of Korea', '1999-03-07');

-- --------------------------------------------------------

--
-- Table structure for table `customer_phone_num`
--

CREATE TABLE `customer_phone_num` (
  `email` varchar(255) NOT NULL,
  `num` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_phone_num`
--

INSERT INTO `customer_phone_num` (`email`, `num`) VALUES
('hk2994@nyu.edu', '8458254576'),
('tk2316@nyu.edu', '0101234567'),
('yk1234@nyu.edu', '2266065120');

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `num` varchar(6) NOT NULL,
  `departure_datetime` datetime NOT NULL,
  `airline_name` varchar(255) NOT NULL,
  `arrival_datetime` datetime DEFAULT NULL,
  `base_price` decimal(10,2) DEFAULT NULL,
  `departure_airport_code` varchar(3) NOT NULL,
  `arrival_airport_code` varchar(3) NOT NULL,
  `airplane_id` varchar(10) NOT NULL,
  `status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flight`
--

INSERT INTO `flight` (`num`, `departure_datetime`, `airline_name`, `arrival_datetime`, `base_price`, `departure_airport_code`, `arrival_airport_code`, `airplane_id`, `status`) VALUES
('A10101', '2023-05-22 00:00:00', 'Korean Air', '2023-05-23 00:00:00', '1400.00', 'ICN', 'JFK', 'KR245RK', 'On time'),
('B15678', '2023-06-14 17:30:00', 'Jet Blue', '2023-06-15 17:30:00', '2750.00', 'PVG', 'JFK', 'N1451KK', 'on time'),
('B51234', '2023-04-06 17:30:00', 'Jet Blue', '2023-04-07 08:30:00', '2350.00', 'JFK', 'PVG', 'N2345TK', 'On time'),
('B61234', '2023-04-05 17:30:00', 'Jet Blue', '2023-04-06 08:30:00', '2350.00', 'JFK', 'PVG', 'N0123BK', 'delayed'),
('B65678', '2023-06-08 17:30:00', 'Jet Blue', '2023-06-09 17:30:00', '2750.00', 'JFK', 'PVG', 'N1234YK', 'on time'),
('K61234', '2023-05-06 00:00:00', 'Korean Air', '2023-06-07 00:00:00', '1000.00', 'ICN', 'JFK', 'KR245RK', 'On time'),
('KR111', '2023-06-06 00:00:00', 'Korean Air', '2023-06-07 00:00:00', '1000.00', 'ICN', 'JFK', 'KR245RK', 'On time');

-- --------------------------------------------------------

--
-- Table structure for table `flight_rating`
--

CREATE TABLE `flight_rating` (
  `ticket_id` varchar(13) NOT NULL,
  `flight_num` varchar(6) NOT NULL,
  `departure_datetime` datetime NOT NULL,
  `airline_name` varchar(255) NOT NULL,
  `rating` decimal(2,1) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `flight_rating`
--

INSERT INTO `flight_rating` (`ticket_id`, `flight_num`, `departure_datetime`, `airline_name`, `rating`, `comment`) VALUES
('bcde2345', 'B65678', '2023-06-08 17:30:00', 'Jet Blue', '5.0', 'Very good'),
('TKA112', 'KR111', '2023-06-06 00:00:00', 'Korean Air', '5.0', 'It was so hot!');

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `id` varchar(13) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `f_name` varchar(255) DEFAULT NULL,
  `l_name` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `payment_type` varchar(8) DEFAULT NULL,
  `payment_num` varchar(19) DEFAULT NULL,
  `payment_name` varchar(255) DEFAULT NULL,
  `payment_exp_date` date DEFAULT NULL,
  `purchase_datetime` datetime DEFAULT NULL,
  `flight_number` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`id`, `email`, `f_name`, `l_name`, `dob`, `payment_type`, `payment_num`, `payment_name`, `payment_exp_date`, `purchase_datetime`, `flight_number`) VALUES
('aaa1112', 'tk2316@nyu.edu', 'Taehun', 'Kim', '1997-07-09', 'Credit', '1000010010010', 'Taehun Kim', '2025-01-01', '2023-05-22 16:26:40', 'B65678'),
('abcd1234', 'hk2994@nyu.edu', 'Brian', 'Kim', '2023-01-19', 'credit', '1234123412341234', 'Brian Kim', '2023-12-31', '2023-04-05 12:00:00', 'B61234'),
('BB4444', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'A10101'),
('bcde2345', 'tk2316@nyu.edu', 'Taehun', 'Kim', '1997-07-09', 'credit', '1234123412341234', 'Taehun Kim', '2023-12-31', '2023-04-05 12:00:00', 'B65678'),
('TKA111', 'jamesBond@gmail.com', 'James', 'Bond', '2024-05-05', 'Credit', '1000010010010', 'Taehun Kim', '2024-01-01', '2023-05-22 16:41:04', 'KR111'),
('TKA112', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'KR111');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD PRIMARY KEY (`username`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airline_staff_email`
--
ALTER TABLE `airline_staff_email`
  ADD PRIMARY KEY (`username`,`email`);

--
-- Indexes for table `airline_staff_phone_num`
--
ALTER TABLE `airline_staff_phone_num`
  ADD PRIMARY KEY (`username`,`num`);

--
-- Indexes for table `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`id`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`code`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `customer_phone_num`
--
ALTER TABLE `customer_phone_num`
  ADD PRIMARY KEY (`email`,`num`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`num`,`departure_datetime`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `departure_airport_code` (`departure_airport_code`),
  ADD KEY `arrival_airport_code` (`arrival_airport_code`),
  ADD KEY `airplane_id` (`airplane_id`);

--
-- Indexes for table `flight_rating`
--
ALTER TABLE `flight_rating`
  ADD PRIMARY KEY (`ticket_id`,`flight_num`,`departure_datetime`),
  ADD KEY `flight_num` (`flight_num`,`departure_datetime`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`id`),
  ADD KEY `email` (`email`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airline_staff`
--
ALTER TABLE `airline_staff`
  ADD CONSTRAINT `airline_staff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `airline_staff_email`
--
ALTER TABLE `airline_staff_email`
  ADD CONSTRAINT `airline_staff_email_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `airline_staff_phone_num`
--
ALTER TABLE `airline_staff_phone_num`
  ADD CONSTRAINT `airline_staff_phone_num_ibfk_1` FOREIGN KEY (`username`) REFERENCES `airline_staff` (`username`);

--
-- Constraints for table `airplane`
--
ALTER TABLE `airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `customer_phone_num`
--
ALTER TABLE `customer_phone_num`
  ADD CONSTRAINT `customer_phone_num_ibfk_1` FOREIGN KEY (`email`) REFERENCES `customer` (`email`);

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`departure_airport_code`) REFERENCES `airport` (`code`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`arrival_airport_code`) REFERENCES `airport` (`code`),
  ADD CONSTRAINT `flight_ibfk_4` FOREIGN KEY (`airplane_id`) REFERENCES `airplane` (`id`);

--
-- Constraints for table `flight_rating`
--
ALTER TABLE `flight_rating`
  ADD CONSTRAINT `flight_rating_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`id`),
  ADD CONSTRAINT `flight_rating_ibfk_2` FOREIGN KEY (`flight_num`,`departure_datetime`) REFERENCES `flight` (`num`, `departure_datetime`),
  ADD CONSTRAINT `flight_rating_ibfk_3` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`email`) REFERENCES `customer` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
