CREATE TABLE cuopon (
	cuopon_id INTEGER PRIMARY KEY AUTOINCREMENT,
	cuopon_description TEXT NOT NULL
);

CREATE TABLE user (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	password TEXT NOT NULL,
	type TEXT NOT NULL
);

CREATE TABLE client (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	number TEXT,
	address TEXT,
	nit TEXT NOT NULL
);

CREATE TABLE bill (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	client_id INTEGER FOREIGN KEY REFERENCES client(id),
	total FLOAT(8,4),
	emission_date DATE,
	payment TEXT
);

CREATE TABLE inventario  (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	producto_id INTEGER FOREIGN KEY REFERENCES producto(id),
	cantidad FLOAT(8,4),
);

CREATE TABLE producto (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	proveedor_id INTEGER FOREIGN KEY REFERENCES proveedor(id),
	precio_compra FLOAT(8,4),
	precio_venta FLOAT(8,4),
	nombre TEXT,
	descripcion TEXT,
);