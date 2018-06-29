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

ALTER TABLE media ADD FOREIGN KEY (current_episode_id);
REFERENCES episode (id);

CREATE TABLE tag
(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name varchar(255) NOT NULL,
	colour char(7) NOT NULL
) ENGINE=INNODB;

CREATE TABLE media_tag
(
	media_id INTEGER NOT NULL,
	tag_id INTEGER NOT NULL,
	PRIMARY KEY (media_id, tag_id),
	FOREIGN KEY fk_mediatags_media (media_id) REFERENCES media (id),
	FOREIGN KEY fk_mediatags_tag (tag_id) REFERENCES tag (id)
) ENGINE=INNODB;

ALTER TABLE media ADD COLUMN last_updated TIMESTAMP;
ALTER TABLE media CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
ALTER TABLE media_tag CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
ALTER TABLE tag CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
ALTER TABLE episode CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

CREATE TABLE bug (
  id int(11) NOT NULL AUTO_INCREMENT,
  title varchar(256) NOT NULL,
  description varchar(256) NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE bug CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
ALTER TABLE tag ADD COLUMN `style` varchar(64);
ALTER TABLE tag ADD COLUMN `description` varchar(256);
