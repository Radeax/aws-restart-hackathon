CREATE TABLE IF NOT EXISTS owners (
  owner_id INT PRIMARY KEY AUTO_INCREMENT,
  firstName VARCHAR (15) NOT NULL,
  lastName VARCHAR (15) NOT NULL,
  emails VARCHAR (20) NOT NULL
)