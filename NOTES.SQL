BIKES
- model_name
- model_code
- current_price

ORDERS
- primary_id serial
- time_of_order

BIKE_ORDER
- primary_key serial
- model_code
- price_at_purchase
- notes
- order_primary_id

psql

create database Bernies_Bikes

CREATE TABLE bikes (
model_code TEXT PRIMARY KEY,
model_name TEXT NOT NULL UNIQUE,
current_price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE orders (
	order_number SERIAL PRIMARY KEY,
	order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_bike (
	bike_order_number SERIAL PRIMARY KEY,
	model_code TEXT NOT NULL REFERENCES bikes,
	price_at_purchase DECIMAL(10, 2) NOT NULL,
	notes TEXT NOT NULL DEFAULT '',
	order_number INT NOT NULL REFERENCES orders
);

INSERT INTO stars (name, temperature_in_kelvin) VALUES (‘The Sun’, 5800), (‘Proxima Centauri’, 3042), (‘Gliese 876’, 3192);

INSERT INTO bikes (model_name, model_code, current_price) VALUES ('The Flyer', 'FLY', 500),
																('The Big Haul', 'HAUL', 600),
																('The Skinny', 'SKIN', 700),
																('Big Buddy', 'BUD', 800);

INSERT INTO orders DEFAULT VALUES;

INSERT INTO order_bike (model_code, price_at_purchase, notes, order_number) VALUES ('FLY', 500, 'add kickstand', 1);
INSERT INTO order_bike (model_code, price_at_purchase, notes, order_number) VALUES ('HAUL', 600, 'paint pink', 1);

INSERT INTO order_bike (model_code, price_at_purchase, order_number) VALUES ('BUD', 800, 2);
