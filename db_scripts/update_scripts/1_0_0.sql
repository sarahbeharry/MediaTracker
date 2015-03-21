CREATE TABLE media (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(256) DEFAULT NULL,
  current_episode_id int(11) DEFAULT NULL,
  notes varchar(256) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE episode (
  id int(11) NOT NULL AUTO_INCREMENT,
  media_id int(11) NOT NULL,
  episode_number decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY media_id (media_id),
  CONSTRAINT episode_ibfk_1 FOREIGN KEY (media_id) REFERENCES media (id)
);

ALTER TABLE media
ADD FOREIGN KEY (current_episode_id)
REFERENCES episode (id);
