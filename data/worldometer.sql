REPLACE INTO city (country)
SELECT
    country.country
FROM
    country
JOIN
    city
ON
    country.country = city.country;


UPDATE country
SET country = 'South Korea'
WHERE country = 'Korea, South';

UPDATE country
SET country = 'North Korea'
WHERE country = 'Korea, North';

UPDATE country
SET country = 'Czechia'
WHERE country = 'Czech Republic';

UPDATE city
SET country = 'South Korea'
WHERE country = 'Korea, South';

UPDATE city
SET country = 'North Korea'
WHERE country = 'Korea, North';

UPDATE city
SET country = 'Czechia'
WHERE country = 'Czech Republic';
