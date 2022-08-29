DROP TABLE agents;
CREATE TABLE agents(
	agent_id SERIAL NOT NULL,
	name VARCHAR(50) NOT NULL,
	is_active BOOLEAN DEFAULT true,
	PRIMARY KEY(agent_id)
);
INSERT INTO agents (name) VALUES ('soccer-default');
INSERT INTO agents (name) VALUES ('soccer-animated');


DROP TABLE plans;
CREATE TABLE plans(
	plan_id SERIAL NOT NULL,
	name VARCHAR(50) NOT NULL,
	price FLOAT NOT NULL DEFAULT 0,
	PRIMARY KEY(plan_id)
);
INSERT INTO plans (name, price) VALUES ('Basic', 129.9);
INSERT INTO plans (name, price) VALUES ('Essencials', 249.9);


DROP TABLE customers;
CREATE TABLE customers(
	customer_id SERIAL NOT NULL,
	name VARCHAR(50) NOT NULL,
	agent_id INT,
	whatsapp_number VARCHAR(15) NOT NULL,
	plan_id INT NOT NULL,
	is_active BOOLEAN DEFAULT true,
	PRIMARY KEY (customer_id),
	CONSTRAINT fk_agent
		FOREIGN KEY(agent_id)
			REFERENCES agents(agent_id),
	CONSTRAINT fk_plan
		FOREIGN KEY(plan_id)
			REFERENCES plans(plan_id)
);
INSERT INTO customers (name, agent_id, whatsapp_number, plan_id) VALUES ('Barcelona quadras', 1, '5515996993842', 2);
INSERT INTO customers (name, agent_id, whatsapp_number, plan_id) VALUES ('Ipaneminha CLUB', 2, '5515996993555', 1);
INSERT INTO customers (name, agent_id, whatsapp_number, plan_id) VALUES ('Quadra Irmãos Sorocaba', 1, '5515996993787', 2);


DROP TABLE places;
CREATE TABLE places(
	place_id SERIAL NOT NULL,
	name VARCHAR(50) NOT NULL,
	place_url VARCHAR(50),
	customer_id INT,
	PRIMARY KEY(place_id),
	CONSTRAINT fk_customer
		FOREIGN KEY customer_id
			REFERENCES customers(customer_id)
);
INSERT INTO places (name, place_url, customer_id) VALUES ('Rio ponche, 437 - Floripa', 'https://google.com/maps', 2);
INSERT INTO places (name, place_url, customer_id) VALUES ('Rio ponche, 433 - Floripa', 'https://google.com/maps', 1);
INSERT INTO places (name, place_url, customer_id) VALUES ('Rio ponche, 432 - Floripa', 'https://google.com/maps', 3);


DROP TABLE availability_groups;
CREATE TABLE avalilability_groups(
	availability_group_id SERIAL NOT NULL,
	name VARCHAR(50) NOT NULL,
	description TEXT,
	place_id INT,
	PRIMARY KEY (availability_group_id)
	CONSTRAINT fk_place
		FOREIGN KEY place_id
			REFERENCES places(place_id)
);
INSERT INTO availability_groups (name, description, place_id) VALUES ('Quadra society', 'lons description', 2);
INSERT INTO availability_groups (name, description, place_id) VALUES ('Quadra salçao', 'lons description', 1);
INSERT INTO availability_groups (name, description, place_id) VALUES ('Quadra voley', 'lons description', 3);
INSERT INTO availability_groups (name, description, place_id) VALUES ('Quadra voleyball', 'lons description', 2);


DROP TABLE services;
CREATE TABLE services(
	service_id SERIAL NOT NULL,
	name VARCHAR(50) NOT NULL,
	duration_min INT NOT NULL,
	price FLOAT NOT NULL DEFAULT 0,
	availability_group_id INT,
	PRIMARY KEY (service_id),
	CONSTRAINT fk_availability_group
		FOREIGN KEY availability_group_id
			REFERENCES availability_groups(availability_group_id)
);


@app.middleware("http")
async def get_customer_middleware(request: Request, call_next):
    global customer
    response = await call_next(request)
    customer = response.headers.get('customer')
    return response
