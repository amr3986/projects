-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Nov 28, 2020 at 08:51 PM
-- Server version: 10.4.16-MariaDB
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `menudb`
--

-- --------------------------------------------------------

--
-- Table structure for table `orderinfo`
--

CREATE TABLE `orderinfo` (
  `ID` int(6) UNSIGNED NOT NULL,
  `First_name` varchar(50) NOT NULL,
  `Last_name` varchar(50) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Street_name` varchar(50) NOT NULL,
  `Building_no` varchar(50) NOT NULL,
  `Food_type` varchar(50) NOT NULL,
  `Dishe_type` varchar(50) NOT NULL,
  `spice_level` varchar(50) NOT NULL,
  `Drink` varchar(50) NOT NULL,
  `Extra_flavor` varchar(50) NOT NULL,
  `Allergy` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderinfo`
--

INSERT INTO `orderinfo` (`ID`, `First_name`, `Last_name`, `Phone`, `Email`, `Street_name`, `Building_no`, `Food_type`, `Dishe_type`, `spice_level`, `Drink`, `Extra_flavor`, `Allergy`) VALUES
(24, 'AMR', 'Al gamal', '0554807501', 'amr.cb9@outlook.sa', 'albyan', '44', 'Indian Food', 'Indian Spiced Chicken', '10', 'pepsi', 'Pepper', 'No'),
(25, 'Reem', 'saleh', '0558906666', 'reem4@gmail.com', 'malaz', '322', 'Fast Food', 'Chicken burger meal', '2', 'Mirinda', 'salt', 'No'),
(26, 'Ali', 'mohmmed', '0558907561', 'saleh4@gmail.com', 'rwabi', '441', 'SeaFood', 'Fish Tacos with Lime', '1', 'pepsi', 'Pepper', 'No'),
(27, 'Khalid', 'saleh', '0558907561', 'Khalsid14@gmail.com', 'salam', '22', 'Arabian Food', 'Mandi Chicken', '2', 'pepsi', 'Nothing', 'No');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orderinfo`
--
ALTER TABLE `orderinfo`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orderinfo`
--
ALTER TABLE `orderinfo`
  MODIFY `ID` int(6) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
