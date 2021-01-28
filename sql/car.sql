CREATE TABLE IF NOT EXISTS car (
  car_id INT PRIMARY KEY AUTO_INCREMENT,
  car_year INT NOT NULL,
  car_color VARCHAR (20) NOT NULL,
  owner_id INT NOT NULL,
  model_id INT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES owners(owner_id),
  FOREIGN KEY (model_id) REFERENCES models(model_id)
);