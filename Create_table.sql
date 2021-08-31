Create Database `hospital`;
CREATE TABLE `Patients` (
  `Cust_ID` varchar(18) NOT NULL,
  `Customer_Name` varchar(255) NOT NULL,
  `Open_date` date NOT NULL,
  `Consult_Dt` date NOT NULL,
  `Vacc_type` char(5) NOT NULL,
  `Dr_Consulted` char(255) DEFAULT NULL,
  `State` char(5) DEFAULT NULL,
  `Country` char(5) NOT NULL,
  `PostCode` int(5) default 0,
  `DOB` date DEFAULT NULL,
  `Active_customer` char(1) NOT NULL,
  PRIMARY KEY (`Cust_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;