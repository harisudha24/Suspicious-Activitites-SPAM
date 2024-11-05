-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 14, 2024 at 02:34 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `cyber_security_spam_mail`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', 'admin'),
('Authority', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `compose_mail`
--

CREATE TABLE `compose_mail` (
  `id` int(11) NOT NULL,
  `sender` varchar(100) NOT NULL,
  `receiver` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` varchar(1000) NOT NULL,
  `image` varchar(100) NOT NULL,
  `status` int(100) NOT NULL,
  `report` int(100) NOT NULL,
  `rdate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `compose_mail`
--

INSERT INTO `compose_mail` (`id`, `sender`, `receiver`, `subject`, `message`, `image`, `status`, `report`, `rdate`) VALUES
(6, 'arun@gmail.com', 'arun@gmail.com', 'kill', 'kill', 'b.txt', 3, 1, '14-01-24');

-- --------------------------------------------------------

--
-- Table structure for table `key_words`
--

CREATE TABLE `key_words` (
  `id` int(11) NOT NULL,
  `words` varchar(1000) NOT NULL,
  `rdate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `key_words`
--

INSERT INTO `key_words` (`id`, `words`, `rdate`) VALUES
(1, 'kill', '13-01-24'),
(2, 'bomb attack', '13-01-24');

-- --------------------------------------------------------

--
-- Table structure for table `user_register`
--

CREATE TABLE `user_register` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `rdate` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `l1` varchar(100) NOT NULL,
  `l2` varchar(100) NOT NULL,
  `mac` varchar(100) NOT NULL,
  `ip` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_register`
--

INSERT INTO `user_register` (`id`, `name`, `contact`, `email`, `address`, `username`, `password`, `rdate`, `status`, `l1`, `l2`, `mac`, `ip`) VALUES
(1, 'arun', '34534', 'arun@gmail.com', 'ttt', 'arun', '123', '2024-01-14', '0', '9.8107392', '77.9845632', '963358166490', '192.168.1.6');
