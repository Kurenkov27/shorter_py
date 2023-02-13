CREATE_SHORTER_TABLE_IF_NOT_EXISTS = """
CREATE TABLE IF NOT EXISTS shorter_url (
  shorter_url varchar(45) NOT NULL,
  original_url varchar(450) NOT NULL,
  expiration_date integer NOT NULL DEFAULT '1',
  PRIMARY KEY (shorter_url)
)
"""
