CREATE_SHORTER_TABLE_IF_NOT_EXISTS = """
CREATE TABLE IF NOT EXISTS shorter_url (
  shorter_url VARCHAR(45) NOT NULL,
  original_url VARCHAR(450) NOT NULL,
  expiration_date TIMESTAMP NOT NULL,
  created_time TIMESTAMP NOT NULL DEFAULT NOW(),
  PRIMARY KEY (shorter_url)
)
"""

GET_UNEXPIRED_SHORT_URLS = """
SELECT * FROM shorter_url
WHERE expiration_date > NOW()
"""

INSERT_SHORT_URL = """
INSERT INTO public.shorter_url
VALUES (%s, %s, %s)
"""
