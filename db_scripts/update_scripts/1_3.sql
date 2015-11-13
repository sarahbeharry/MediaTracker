CREATE TABLE bug (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(256) NOT NULL,
  description varchar(256) NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE bug CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
