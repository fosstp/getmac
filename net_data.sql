/*!40101 SET NAMES utf8 */;

--
-- 資料庫： `st_pc`
--

-- --------------------------------------------------------

--
-- 資料表結構 `net_data`
--

CREATE TABLE IF NOT EXISTS `net_data` (
`id` int(3) NOT NULL,
  `name` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `mac` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `ip` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `udt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 已匯出資料表的索引
--

--
-- 資料表索引 `net_data`
--
ALTER TABLE `net_data`
 ADD PRIMARY KEY (`id`), ADD UNIQUE KEY `mac` (`mac`);

--
-- 在匯出的資料表使用 AUTO_INCREMENT
--

--
-- 使用資料表 AUTO_INCREMENT `net_data`
--
ALTER TABLE `net_data`
MODIFY `id` int(3) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;
