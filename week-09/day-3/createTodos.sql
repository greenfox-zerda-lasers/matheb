SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Database: `todos`
--

-- --------------------------------------------------------

--
-- Table structure for table `todos`

CREATE TABLE `todos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(50) COLLATE latin1_general_ci NOT NULL DEFAULT '',
  `completed` varchar(25) COLLATE latin1_general_ci NOT NULL DEFAULT 'false',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
