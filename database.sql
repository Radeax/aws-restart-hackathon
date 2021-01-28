CREATE TABLE IF NOT EXISTS cars (
  car_id INT PRIMARY KEY AUTO_INCREMENT,
  car_make VARCHAR(15) NOT NULL,
  car_model VARCHAR(15) NOT NULL,
  car_year SMALLINT NOT NULL,
  car_color VARCHAR(15) NOT NULL,
  car_price DECIMAL(8, 2) NOT NULL
);
INSERT INTO
  cars (
    car_id,
    car_make,
    car_model,
    car_year,
    car_color,
    car_price
  )
VALUES
  (
    '01',
    'Toyota',
    'Camry',
    '2020',
    'White',
    '22995'
  ),
  (
    '02',
    'Honda',
    'Accord',
    '2021',
    'Black',
    '23995'
  ),
  (
    '03',
    'Tesla',
    'Model3',
    '2019',
    'White',
    '49500'
  ),
  (
    '04',
    'Ford',
    'Mustang',
    '2021',
    'Black',
    '27000'
  ),
  (
    '05',
    'Chevy',
    'Corvette',
    '2020',
    'Red',
    '75000'
  ),
  ('06', 'Ford', 'F150', '2019', 'Blue', '29900'),
  ('07', 'Volvo', 'XC90', '2021', 'Grey', '42000');
SELECT
  *
FROM
  cars;
DROP TABLE cars;
SELECT
  *
FROM
  cars
WHERE
  car_make = 'Ford';
SELECT
  *
FROM
  cars
WHERE
  car_color = 'Black';
SELECT
  *
FROM
  cars
WHERE
  car_year > 2020;