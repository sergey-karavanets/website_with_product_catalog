CREATE USER mysite WITH ENCRYPTED PASSWORD 'password';
CREATE DATABASE mysite_goods WITH OWNER mysite;
GRANT ALL ON DATABASE mysite_goods TO mysite;