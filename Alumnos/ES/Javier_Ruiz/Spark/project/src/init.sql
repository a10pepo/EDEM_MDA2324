-- init.sql

DROP TABLE IF EXISTS mercadona;
CREATE TABLE mercadona (
    id SERIAL ,
    supermarket VARCHAR(255),
    category VARCHAR(255),
    name VARCHAR(255),
    price DECIMAL(10, 2),
    reference_price DECIMAL(10, 2),
    reference_unit VARCHAR(50),
    insert_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS clientes;
CREATE TABLE clientes (
    id SERIAL ,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender VARCHAR(10),
    email VARCHAR(255)
);

DROP TABLE IF EXISTS sandias;
CREATE TABLE sandias (
    id SERIAL ,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    reference_price DECIMAL(10, 2),
    reference_unit VARCHAR(50)
);


DROP TABLE IF EXISTS generos;
CREATE TABLE generos (
    gender VARCHAR(10),
    conteo_total INT,
    most_consumed_category VARCHAR(255)
);

DROP TABLE IF EXISTS frutacara;
CREATE TABLE frutacara (
    name VARCHAR(255),
    max_reference_price DECIMAL(10, 2),
    reference_unit VARCHAR(50)
);

DROP TABLE IF EXISTS frutabarata;
CREATE TABLE frutabarata (
    name VARCHAR(255),
    AVG_reference_price DECIMAL(10, 2),
    reference_unit VARCHAR(50)
);

