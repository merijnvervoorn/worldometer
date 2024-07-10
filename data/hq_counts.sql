CREATE TABLE hq_counts (
    country VARCHAR(20) PRIMARY KEY,
    hq_count INTEGER
);

INSERT INTO `hq_counts` VALUES ('Mexico',2),
	('United States',208),
	('Estonia',1),
	('India',6),
	('Philippines',11),
	('France',17),
	('Germany',28),
	('Trinidad and Tobago',1),
	('Czechia',7),
	('Korea, South',2),
	('China',7),
	('Croatia',1),
	('Sweden',6),
	('Malta',1),
	('South Africa',11),
	('Lithuania',3),
	('Israel',5),
	('Slovenia',1),
	('United Kingdom',35),
	('Spain',1),
	('Hungary',3),
	('Taiwan',2),
	('Cyprus',1),
	('Italy',13),
	('Bulgaria',1),
	('Japan',3),
	('New Zealand',2),
	('Australia',3),
	('Singapore',2),
	('United Arab Emirates',5),
	('Hong Kong',1),
	('Portugal',3),
	('Poland',1),
	('Canada',8),
	('Belgium',2),
	('Turkey',6),
	('Switzerland',3),
	('Finland',3),
	('Denmark',4),
	('Norway',2),
	('Colombia',2),
	('Bangladesh',1),
	('Netherlands',3),
	('Malaysia',1),
	('Venezuela',2),
	('Jordan',1);

UPDATE hq_counts
SET country = 'South Korea'
WHERE country = 'Korea, South';

UPDATE hq_counts
SET country = 'Czechia'
WHERE country = 'Czech Republic';
