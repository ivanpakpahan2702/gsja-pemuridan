-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.14-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for db_gereja_gsja
CREATE DATABASE IF NOT EXISTS `db_gereja_gsja` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `db_gereja_gsja`;

-- Dumping structure for table db_gereja_gsja.tabel_akun
CREATE TABLE IF NOT EXISTS `tabel_akun` (
  `id_akun` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `nama` int(255) DEFAULT NULL,
  `nomor_hp` varchar(15) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_akun`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table db_gereja_gsja.tabel_akun: ~0 rows (approximately)
/*!40000 ALTER TABLE `tabel_akun` DISABLE KEYS */;
/*!40000 ALTER TABLE `tabel_akun` ENABLE KEYS */;

-- Dumping structure for table db_gereja_gsja.tabel_download
CREATE TABLE IF NOT EXISTS `tabel_download` (
  `id_download` int(11) NOT NULL AUTO_INCREMENT,
  `judul` varchar(50) DEFAULT NULL,
  `path` varchar(50) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  PRIMARY KEY (`id_download`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table db_gereja_gsja.tabel_download: ~6 rows (approximately)
/*!40000 ALTER TABLE `tabel_download` DISABLE KEYS */;
INSERT INTO `tabel_download` (`id_download`, `judul`, `path`, `tanggal`) VALUES
	(1, 'Jadwal Doa 10 Hari 2023', 'Jadwal Doa 10 Hari.docx', '2023-07-04'),
	(2, 'Jadwal Doa Puasa', 'Jadwal Doa Puasa.docx', '2023-07-04'),
	(3, 'Jadwal Ibadah Keluarga 2021', 'Jadwal Ibadah Keluarga 2021.xlsx', '2023-07-04'),
	(4, 'Jadwal Ibadah RT 2023', 'Jadwal Ibadah RT 2023.docx', '2023-07-04'),
	(5, 'Jadwal Ibadah', 'Jadwal Ibadah.docx', '2023-07-04'),
	(6, 'Jadwal Pelayanan Ibadah Raya', 'Jadwal Pelayanan Ibadah Raya.xlsx', '2023-07-04');
/*!40000 ALTER TABLE `tabel_download` ENABLE KEYS */;

-- Dumping structure for table db_gereja_gsja.tabel_galeri
CREATE TABLE IF NOT EXISTS `tabel_galeri` (
  `id_galeri` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(50) DEFAULT NULL,
  `path` varchar(500) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_galeri`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table db_gereja_gsja.tabel_galeri: ~14 rows (approximately)
/*!40000 ALTER TABLE `tabel_galeri` DISABLE KEYS */;
INSERT INTO `tabel_galeri` (`id_galeri`, `caption`, `path`, `tanggal`, `created_at`) VALUES
	(1, 'Testing', 'noimage.png', '2021-12-10', '0000-00-00 00:00:00'),
	(2, 'Assemblies Of God', '14_12_2021_01_33_54_pm_AGWebpreview.jpg', '2021-12-14', '0000-00-00 00:00:00'),
	(3, 'Perayaan Natal 2021 [1]', '14_12_2021_10_04_50_pm_GsjaNatal2021.jpeg', '2021-12-14', '0000-00-00 00:00:00'),
	(4, 'Perayaan Natal 2021 [2]', '14_12_2021_10_05_26_pm_Gsja_Pemuridan_2.jpeg', '2021-12-14', '0000-00-00 00:00:00'),
	(5, 'Perayaan Natal 2021 [3]', '14_12_2021_10_05_58_pm_Gsja_Pemuridan_3.jpeg', '2021-12-14', '0000-00-00 00:00:00'),
	(6, 'Perayaan Natal 2021 [4]', '14_12_2021_10_06_35_pm_Gsja_Pemuridan_4.jpeg', '2021-12-14', '0000-00-00 00:00:00'),
	(7, 'Perayaan Natal 2021 [5]', '15_12_2021_03_42_20_pm_IMG-20211214-WA0009.jpg', '2021-12-14', '0000-00-00 00:00:00'),
	(8, 'Ucapan Syukur Di Lais', '30_12_2021_01_49_11_pm_IMG-20211230-WA0003.jpg', '2021-12-30', '0000-00-00 00:00:00'),
	(9, 'Ucapan Syukur Di Lais [2]', '30_12_2021_01_50_42_pm_IMG-20211230-WA0006.jpg', '2021-12-30', '0000-00-00 00:00:00'),
	(10, 'Ucapan Syukur Di Lais [3]', '30_12_2021_01_51_41_pm_IMG-20211230-WA0004.jpg', '2021-12-30', '0000-00-00 00:00:00'),
	(11, 'Ucapan Syukur Di Lais [4]', '30_12_2021_01_52_57_pm_IMG-20211230-WA0005.jpg', '2021-12-30', '0000-00-00 00:00:00'),
	(12, 'Kaum Pria GSJA Pemuridan', '18_08_2022_02_52_39_pm_Kaum_Pria_GSJA_Pemuridan.jpeg', '2022-07-31', '0000-00-00 00:00:00'),
	(13, 'Perayaan HUT RI 77 GSJA Pemuridan', '18_08_2022_05_37_19_pm_WhatsApp_Image_2022-08-14_at_13_44_10.jpeg', '2022-08-14', '0000-00-00 00:00:00'),
	(14, 'Peringatan HUT RI 77 GSJA Pemuridan', '18_08_2022_05_38_52_pm_WhatsApp_Image_2022-08-14_at_13_44_10__1_.jpeg', '2022-08-14', '0000-00-00 00:00:00');
/*!40000 ALTER TABLE `tabel_galeri` ENABLE KEYS */;

-- Dumping structure for table db_gereja_gsja.tabel_galeri_kegiatan
CREATE TABLE IF NOT EXISTS `tabel_galeri_kegiatan` (
  `id_galeri_kegiatan` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(500) NOT NULL,
  PRIMARY KEY (`id_galeri_kegiatan`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table db_gereja_gsja.tabel_galeri_kegiatan: ~6 rows (approximately)
/*!40000 ALTER TABLE `tabel_galeri_kegiatan` DISABLE KEYS */;
INSERT INTO `tabel_galeri_kegiatan` (`id_galeri_kegiatan`, `path`) VALUES
	(2, '2.png'),
	(3, '3.png'),
	(4, '4.png'),
	(5, '5.png'),
	(6, '14_12_2021_10_05_26_pm_Gsja_Pemuridan_2.png'),
	(8, '1.png');
/*!40000 ALTER TABLE `tabel_galeri_kegiatan` ENABLE KEYS */;

-- Dumping structure for table db_gereja_gsja.tabel_jadwal_kegiatan
CREATE TABLE IF NOT EXISTS `tabel_jadwal_kegiatan` (
  `id_jadwal_kegiatan` int(11) NOT NULL AUTO_INCREMENT,
  `kegiatan` varchar(255) DEFAULT NULL,
  `hari` varchar(50) DEFAULT NULL,
  `waktu` time DEFAULT NULL,
  `tempat` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_jadwal_kegiatan`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table db_gereja_gsja.tabel_jadwal_kegiatan: ~9 rows (approximately)
/*!40000 ALTER TABLE `tabel_jadwal_kegiatan` DISABLE KEYS */;
INSERT INTO `tabel_jadwal_kegiatan` (`id_jadwal_kegiatan`, `kegiatan`, `hari`, `waktu`, `tempat`) VALUES
	(1, 'Ibadah Raya', 'Minggu', '10:00:00', 'Gereja'),
	(2, 'Ibadah Sekolah Minggu', 'Minggu', '09:00:00', 'Pastori'),
	(3, 'Doa Puasa', 'Jum\'at', '18:30:00', 'Ditentukan'),
	(4, 'Ibadah Rumah Tangga', 'Selasa (Minggu ke-2 & 4)', '16:00:00', 'Ditentukan'),
	(5, 'Ibadah Kaum Pria', 'Rabu (Minggu ke-4)', '19:00:00', 'Ditentukan'),
	(6, 'Ibadah di Lais', 'Minggu ke-2 & 4', '19:00:00', 'Lais'),
	(7, 'Ibadah KKA Unit 10', 'Rabu (Minggu ke-3)', '19:00:00', 'Unit 10'),
	(8, 'Ibadah Doa 10 Hari', 'Di Bulan Mei', '18:30:00', 'Keliling (Ditentukan)'),
	(9, 'Ibadah di Tanah Hitam', 'Minggu', '18:30:00', 'Tanah Hitam');
/*!40000 ALTER TABLE `tabel_jadwal_kegiatan` ENABLE KEYS */;

-- Dumping structure for table db_gereja_gsja.tabel_kategori
CREATE TABLE IF NOT EXISTS `tabel_kategori` (
  `id_kategori` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_kategori`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table db_gereja_gsja.tabel_kategori: ~2 rows (approximately)
/*!40000 ALTER TABLE `tabel_kategori` DISABLE KEYS */;
INSERT INTO `tabel_kategori` (`id_kategori`, `nama`) VALUES
	(1, 'Renungan'),
	(2, 'WPDA');
/*!40000 ALTER TABLE `tabel_kategori` ENABLE KEYS */;

-- Dumping structure for table db_gereja_gsja.tabel_komentar
CREATE TABLE IF NOT EXISTS `tabel_komentar` (
  `id_komentar` int(11) NOT NULL AUTO_INCREMENT,
  `penulis` varchar(255) NOT NULL,
  `status_komentar` enum('Show','Hide') NOT NULL,
  `tanggal` datetime NOT NULL,
  `isi` longtext DEFAULT NULL,
  `postingan` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_komentar`),
  KEY `FK_tabel_komentar_tabel_postingan` (`postingan`),
  CONSTRAINT `FK_tabel_komentar_tabel_postingan` FOREIGN KEY (`postingan`) REFERENCES `tabel_postingan` (`id_postingan`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table db_gereja_gsja.tabel_komentar: ~18 rows (approximately)
/*!40000 ALTER TABLE `tabel_komentar` DISABLE KEYS */;
INSERT INTO `tabel_komentar` (`id_komentar`, `penulis`, `status_komentar`, `tanggal`, `isi`, `postingan`) VALUES
	(1, 'Elijah O\'Sullivan', 'Show', '2023-07-08 13:40:30', 'Good, Thanks', 1),
	(2, 'Robert Levy II', 'Show', '2023-07-08 13:40:56', 'Love ya!', 1),
	(3, 'Tajus Kruminis', 'Show', '2023-07-08 13:41:16', 'Hmmm very Good', 2),
	(4, 'River Williams', 'Show', '2023-07-08 13:42:06', '^_^', 2),
	(5, 'SilverRyan', 'Hide', '2023-07-08 13:42:32', 'Nevermind', 1),
	(6, 'SilverRyan', 'Hide', '2023-07-08 13:42:32', 'Zzzzz', 2),
	(7, 'Ivan', 'Hide', '2023-07-08 13:42:32', 'Hello', 1),
	(8, 'Ivan', 'Hide', '0000-00-00 00:00:00', '<p><i><strong>Ivan</strong></i></p>', 3),
	(9, 'IvanDer', 'Hide', '2023-07-10 21:27:05', '<p><i><strong>Ivan Deras</strong></i></p>', 3),
	(10, 'Ivan Pakpahan', 'Hide', '2023-07-10 21:31:29', '<p><i><strong>Halloo</strong></i></p>', 3),
	(12, 'Hello', 'Show', '2023-07-10 21:39:50', '<p><a href="https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette">https://www.programiz.com/python-programming/datetime/current-datetime#google_vignette</a></p><p>Testing</p>', 3),
	(13, 'Ivan', 'Hide', '2023-07-11 08:59:35', '<p>Defana</p>', 4),
	(14, 'Ivan', 'Hide', '2023-07-11 09:01:48', '<p><i><strong>Defano</strong></i></p>', 4),
	(15, 'Tes', 'Hide', '2023-07-11 09:03:32', '<p>Haloo</p>', 4),
	(16, 'Rigen', 'Hide', '2023-07-11 11:05:01', '<p>Give Alok</p>', 2),
	(17, 'Jasman Parde', 'Show', '2023-07-11 11:13:43', '<p><strong>Poin-poin yang harus dicek</strong></p><ol><li>Ketelitian</li><li>Keteraturan</li></ol><blockquote><p>Teruslah <strong>Berjuang </strong><i>Dan Berusaha</i></p></blockquote>', 4),
	(18, 'Robertsen', 'Hide', '2023-07-12 08:53:47', '<p>Havana</p>', 5),
	(19, 'DebUnks', 'Hide', '2023-07-12 08:56:49', '<p>Plea</p>', 5);
/*!40000 ALTER TABLE `tabel_komentar` ENABLE KEYS */;

-- Dumping structure for table db_gereja_gsja.tabel_postingan
CREATE TABLE IF NOT EXISTS `tabel_postingan` (
  `id_postingan` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(500) DEFAULT NULL,
  `thumbnail` varchar(255) DEFAULT NULL,
  `judul` varchar(500) DEFAULT NULL,
  `isi` longtext DEFAULT NULL,
  `tanggal` datetime DEFAULT NULL,
  `penulis` varchar(255) DEFAULT NULL,
  `kategori` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_postingan`) USING BTREE,
  UNIQUE KEY `slug` (`slug`),
  KEY `FK_tabel_postingan_tabel_kategori` (`kategori`),
  CONSTRAINT `FK_tabel_postingan_tabel_kategori` FOREIGN KEY (`kategori`) REFERENCES `tabel_kategori` (`id_kategori`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table db_gereja_gsja.tabel_postingan: ~5 rows (approximately)
/*!40000 ALTER TABLE `tabel_postingan` DISABLE KEYS */;
INSERT INTO `tabel_postingan` (`id_postingan`, `slug`, `thumbnail`, `judul`, `isi`, `tanggal`, `penulis`, `kategori`) VALUES
	(1, 'Renungan-Malam', 'no_image.png', 'Renungan Malam', '<h1 style="text-align:center"><strong>Renungan Malam</strong></h1><p style="text-align:center"><strong>(13) Pencobaan-pencobaan yang kamu alami ialah pencobaan-pencobaan biasa, yang tidak melebihi kekuatan manusia. Sebab Allah setia dan karena itu Ia tidak akan membiarkan kamu dicobai melampaui kekuatanmu. Pada waktu kamu dicobai Ia akan memberikan kepadamu jalan ke luar, sehingga kamu dapat menanggungnya. (14) Karena itu, saudara-saudaraku yang kekasih, jauhilah penyembahan berhala!</strong></p>', '2023-07-06 18:44:45', 'Ivan Pakpahan', 1),
	(2, 'Renungan-Pagi', 'no_image.png', 'Renungan Pagi', '<h1 style="text-align:center"><strong>Renungan Pagi</strong></h1><p style="text-align:center"><strong>(13) Pencobaan-pencobaan yang kamu alami ialah pencobaan-pencobaan biasa, yang tidak melebihi kekuatan manusia. Sebab Allah setia dan karena itu Ia tidak akan membiarkan kamu dicobai melampaui kekuatanmu. Pada waktu kamu dicobai Ia akan memberikan kepadamu jalan ke luar, sehingga kamu dapat menanggungnya. (14) Karena itu, saudara-saudaraku yang kekasih, jauhilah penyembahan berhala!</strong></p>', '2023-07-06 18:46:45', 'Ivan Pakpahan', 1),
	(3, 'Renungan-Sore', 'no_image.png', 'Renungan Sore', '<h1 style="text-align:center"><strong>Renungan Sore</strong></h1><p style="text-align:center"><strong>(13) Pencobaan-pencobaan yang kamu alami ialah pencobaan-pencobaan biasa, yang tidak melebihi kekuatan manusia. Sebab Allah setia dan karena itu Ia tidak akan membiarkan kamu dicobai melampaui kekuatanmu. Pada waktu kamu dicobai Ia akan memberikan kepadamu jalan ke luar, sehingga kamu dapat menanggungnya. (14) Karena itu, saudara-saudaraku yang kekasih, jauhilah penyembahan berhala!</strong></p>', '2023-07-06 18:48:03', 'Ivan Pakpahan', 1),
	(4, 'WPDA-Maret', 'no_image.png', 'WPDA Maret', '<h1 style="text-align:center"><strong>WPDA Maret</strong></h1><p style="text-align:center"><strong>(13) Pencobaan-pencobaan yang kamu alami ialah pencobaan-pencobaan biasa, yang tidak melebihi kekuatan manusia. Sebab Allah setia dan karena itu Ia tidak akan membiarkan kamu dicobai melampaui kekuatanmu. Pada waktu kamu dicobai Ia akan memberikan kepadamu jalan ke luar, sehingga kamu dapat menanggungnya. (14) Karena itu, saudara-saudaraku yang kekasih, jauhilah penyembahan berhala!</strong></p>', '2023-07-06 19:18:30', 'Ivan Pakpahan', 2),
	(5, 'WPDA-Agustus', 'thumbs_test.png', 'WPDA Agustus', '<h1 style="text-align:center"><strong>WPDA Agustus</strong></h1><p style="text-align:center"><strong>(13) Pencobaan-pencobaan yang kamu alami ialah pencobaan-pencobaan biasa, yang tidak melebihi kekuatan manusia. Sebab Allah setia dan karena itu Ia tidak akan membiarkan kamu dicobai melampaui kekuatanmu. Pada waktu kamu dicobai Ia akan memberikan kepadamu jalan ke luar, sehingga kamu dapat menanggungnya. (14) Karena itu, saudara-saudaraku yang kekasih, jauhilah penyembahan berhala!</strong></p>', '2023-07-08 09:53:00', 'Ivan Pakpahan', 2);
/*!40000 ALTER TABLE `tabel_postingan` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
