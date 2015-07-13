-- phpMyAdmin SQL Dump
-- version 4.3.8
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 13, 2015 at 02:02 AM
-- Server version: 10.0.20-MariaDB
-- PHP Version: 5.6.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `tis100`
--

-- --------------------------------------------------------

--
-- Table structure for table `solutions`
--

CREATE TABLE IF NOT EXISTS `solutions` (
  `int` int(11) NOT NULL,
  `master` int(11) NOT NULL,
  `forkno` int(11) NOT NULL,
  `@0` text NOT NULL,
  `@1` text NOT NULL,
  `@2` text NOT NULL,
  `@3` text NOT NULL,
  `@4` text NOT NULL,
  `@5` text NOT NULL,
  `@6` text NOT NULL,
  `@7` text NOT NULL,
  `@8` text NOT NULL,
  `@9` text NOT NULL,
  `@10` text NOT NULL,
  `@11` text NOT NULL,
  `ports` text NOT NULL,
  `levelcode` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `solutions`
--
ALTER TABLE `solutions`
  ADD PRIMARY KEY (`int`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `solutions`
--
ALTER TABLE `solutions`
  MODIFY `int` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
