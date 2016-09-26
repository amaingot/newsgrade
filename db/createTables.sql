CREATE TABLE `newsgrade`.`sources` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NULL,
  `url` VARCHAR(256) NOT NULL,
  `last_fetched` DATETIME NULL,
  `last_error` DATETIME NULL,
  `source_type` VARCHAR(64) NOT NULL,
  `source_subtype` VARCHAR(64) NULL,
  `metadata` VARCHAR(1024) NULL,
  PRIMARY KEY (`id`, `last_fetched`));

CREATE TABLE `newsgrade`.`source_errors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `source_id` INT NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `error` VARCHAR(1024) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `source_id_idx` (`source_id` ASC),
  INDEX `timestamp_idx` (`timestamp` DESC, `source_id` ASC),
  CONSTRAINT `source_id`
    FOREIGN KEY (`source_id`)
    REFERENCES `newsgrade`.`sources` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
