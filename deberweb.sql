-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.3.16-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para deberweb
CREATE DATABASE IF NOT EXISTS `deberweb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `deberweb`;

-- Volcando estructura para tabla deberweb.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla deberweb.plancuenta
CREATE TABLE IF NOT EXISTS `plancuenta` (
  `id_PC` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) NOT NULL DEFAULT '0',
  `grupo` int(11) NOT NULL DEFAULT 0,
  `descripcion` varchar(50) NOT NULL DEFAULT '0',
  `naturaleza` varchar(50) NOT NULL DEFAULT '0',
  `estado` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_PC`),
  KEY `FK_plancuenta_grupo` (`grupo`),
  CONSTRAINT `FK_plancuenta_grupo` FOREIGN KEY (`grupo`) REFERENCES `grupo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
