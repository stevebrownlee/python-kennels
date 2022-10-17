DELETE FROM `Location`;
DELETE FROM Employee;
DELETE FROM Customer;
DELETE FROM Animal;

DROP TABLE IF EXISTS Animal;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS [Location];

CREATE TABLE `Location` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL
);

CREATE TABLE `Customer` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `address`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL
);


CREATE TABLE `Animal` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`customer_id` INTEGER NOT NULL,
	`location_id` INTEGER,
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);

CREATE TABLE `EmployeeAnimal` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`animal_id`  TEXT NOT NULL,
	`employee_id` TEXT NOT NULL,
	FOREIGN KEY(`animal_id`) REFERENCES `Animal`(`id`),
	FOREIGN KEY(`employee_id`) REFERENCES `Employee`(`id`)
);


CREATE TABLE `Employee` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)

);

INSERT INTO `EmployeeAnimal` VALUES (null, 1, 2);
INSERT INTO `EmployeeAnimal` VALUES (null, 4, 1);
INSERT INTO `EmployeeAnimal` VALUES (null, 3, 1);
INSERT INTO `EmployeeAnimal` VALUES (null, 5, 3);
INSERT INTO `EmployeeAnimal` VALUES (null, 3, 4);
INSERT INTO `EmployeeAnimal` VALUES (null, 2, 4);


INSERT INTO `Location` VALUES (null, 'Nashville North', "64 Washington Heights");
INSERT INTO `Location` VALUES (null, 'Nashville South', "101 Penn Ave");


INSERT INTO `Employee` VALUES (null, "Madi Peper", "35498 Madison Ave", 1);
INSERT INTO `Employee` VALUES (null, "Kristen Norris", "100 Main St", 1);
INSERT INTO `Employee` VALUES (null, "Meg Ducharme", "404 Unknown Ct", 2);
INSERT INTO `Employee` VALUES (null, "Hannah Hall", "204 Empty Ave", 1);
INSERT INTO `Employee` VALUES (null, "Leah Hoefling", "200 Success Way", 2);


INSERT INTO `Customer` VALUES (null, "Mo Silvera", "201 Created St", "mo@silvera.com", "password");
INSERT INTO `Customer` VALUES (null, "Bryan Nilsen", "500 Internal Error Blvd", "bryan@nilsen.com", "password");
INSERT INTO `Customer` VALUES (null, "Jenna Solis", "301 Redirect Ave", "jenna@solis.com", "password");
INSERT INTO `Customer` VALUES (null, "Emily Lemmon", "454 Mulberry Way", "emily@lemmon.com", "password");



INSERT INTO `Animal` VALUES (null, "Snickers", "Dalmation", "Recreation", 4, 1);
INSERT INTO `Animal` VALUES (null, "Jax", "Beagle", "Treatment", 1, 1);
INSERT INTO `Animal` VALUES (null, "Falafel", "Siamese", "Treatment", 4, 2);
INSERT INTO `Animal` VALUES (null, "Doodles", "Poodle", "Kennel", 3, 1);
INSERT INTO `Animal` VALUES (null, "Daps", "Boxer", "Kennel", 2, 2);



select * from EmployeeAnimal;
delete from EmployeeAnimal where id =3;
select * from Animal;



SELECT
    l.id,
    l.name,
    l.address,
    COUNT(a.id) animals
FROM location l
JOIN animal a ON a.location_id = l.id
GROUP BY a.location_id
;

SELECT
	e.id,
	e.name employee,
	a.name animal,
	a.id animal_id,
	a.status,
	a.breed,
	a.location_id,
	a.customer_id
FROM Employee e
LEFT JOIN EmployeeAnimal ea ON e.id = ea.employee_id
LEFT JOIN Animal a ON a.id = ea.animal_id
WHERE e.id = 3
;








