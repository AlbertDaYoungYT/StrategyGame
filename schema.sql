

IF DATABASE EXISTS `testdb` THEN DO
    DROP DATABASE `old_testdb`;
    
    ALTER DATABASE 'testdb' RENAME TO 'old_testdb';
    DROP DATABASE `testdb`;
END DO;

CREATE DATABASE 'testdb';
USE `testdb`;

-- --------------------------------------------------------

SET FOREIGN_KEY_CHECKS=0; --! IMPORTANT: Disable foreign key checks.

CREATE TABLE `users` (
  'id'          int(11) NOT NULL AUTO_INCREMENT,
  'username'    varchar(255) DEFAULT NULL,
  'password'   varchar(255) DEFAULT NULL,
  'email'      varchar(255) UNIQUE,
  'created_at'  timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  'updated_at'  timestamp ON UPDATE CURRENT_TIMESTAMP NOT NULL,
  ''

  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `users` (`id`, `username`) VALUES
(1, 'AlbertDaYoung');

-- --------------------------------------------------------


