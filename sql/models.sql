CREATE TABLE IF NOT EXISTS models (
  model_id INT PRIMARY KEY AUTO_INCREMENT,
  model_name VARCHAR(15) NOT NULL,
  car_price INT NOT NULL,
  make_id INT NOT NULL,
  FOREIGN KEY (make_id) REFERENCES makes(make_id)
);
INSERT INTO
  models(model_name, car_price, make_id)
VALUES
  ('Civic', 12500, 2),
  ('Corolla', 15900, 1),
  ('Camry', 25730, 1),
  ('EClass', 31000, 3),
  ('Challenger', 32100, 4),
  ('Corvette', 70400, 6),
  ('X5', 41500, 5),
  ('F150', 33100, 7),
  ('Mustang', 24950, 7),
  ('Model3', 49500, 8),
  ('M3', 38000, 5),
  ('Accord', 26200, 2),
  ('Durango', 19800, 4),
  ('ModelX', 46000, 8),
  ('328', 22500, 5),
  ('Focus', 11500, 7),
  ('Rav4', 31100, 1),
  ('Charger', 22330, 4),
  ('Malibu', 14250, 4),
  ('Gwagon', 90000, 3)