CREATE TABLE IF NOT EXISTS makes (
  make_id INT PRIMARY KEY AUTO_INCREMENT,
  manufacturer VARCHAR (15)
)
INSERT INTO
  makes (manufacturer)
VALUES
  ('Toyota'),
  ('Honda'),
  ('Mercedes'),
  ('Dodge'),
  ('BMW'),
  ('Chevy'),
  ('Ford'),
  ('Tesla')