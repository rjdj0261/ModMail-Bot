CREATE DATABASE IF NOT EXISTS `railway`;
USE `railway`;


CREATE TABLE IF NOT EXISTS `playlist` (
  `user` varchar(32) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `title` varchar(512) DEFAULT NULL,
  `link` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE IF NOT EXISTS `queue` (
  `server` varchar(32) NOT NULL,
  `isPlaying` tinyint(4) DEFAULT NULL,
  `requester` varchar(50) DEFAULT NULL,
  `textChannel` varchar(50) DEFAULT NULL,
  `track` varchar(128) DEFAULT NULL,
  `title` varchar(512) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `index` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE IF NOT EXISTS `server` (
  `server` varchar(32) NOT NULL,
  `prefix` varchar(10) DEFAULT NULL,
  `loop` tinyint(4) DEFAULT NULL,
  `loopQueue` tinyint(4) DEFAULT NULL,
  `djRole` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE IF NOT EXISTS `skip` (
  `server` varchar(50) DEFAULT NULL,
  `user` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
