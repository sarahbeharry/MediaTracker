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

ALTER TABLE media
ADD COLUMN last_updated TIMESTAMP
