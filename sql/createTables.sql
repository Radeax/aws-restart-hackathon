CREATE TABLE IF NOT EXISTS Owners (
  owner_id INT PRIMARY KEY AUTO_INCREMENT,
  firstName VARCHAR (15) NOT NULL,
  lastName VARCHAR (15) NOT NULL,
  email VARCHAR (20) NOT NULL
);
CREATE TABLE IF NOT EXISTS Makes (
  make_id INT PRIMARY KEY AUTO_INCREMENT,
  manufacturer VARCHAR (15)
);
CREATE TABLE IF NOT EXISTS Models (
  model_id INT PRIMARY KEY AUTO_INCREMENT,
  model_name VARCHAR(15) NOT NULL,
  car_price INT NOT NULL,
  make_id INT NOT NULL,
  FOREIGN KEY (make_id) REFERENCES Makes(make_id)
);
CREATE TABLE IF NOT EXISTS Cars (
  car_id INT PRIMARY KEY AUTO_INCREMENT,
  car_year INT NOT NULL,
  car_color VARCHAR (20) NOT NULL,
  owner_id INT NOT NULL,
  model_id INT NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES Owners(owner_id),
  FOREIGN KEY (model_id) REFERENCES Models(model_id)
);