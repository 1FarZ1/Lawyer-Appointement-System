SELECT * FROM users

--  get lawyers

SELECT * FROM lawyers


-- GET THE categories of the lawyers
SELECT categories.name FROM lawyers JOIN categories ON lawyers.categories_id = categories.id



--  insert some lawyers , here is the SCHEMA
--  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
--    name = Column(String(50))
--    fname = Column(String(50))
--    email = Column(String(100), unique=True)
--    phone = Column(String(20))
--    address = Column(String(255))
--    description = Column(String(255))
--    avocat_image = Column(String(255))
--    categories = Column(String(255))  # Assuming a comma-separated string for categories
--    schedule = Column(String(255))  # Assuming a serialized format for schedule
--    rating = Column(Float)
--    comments = Column(String(255))  # Assuming a serialized format for comments
--    social = Column(String(255))
--    wilaya = Column(String(50))
--    longitude = Column(Float)
--    latitude = Column(Float)

INSERT INTO lawyers (name, fname, email, phone, address, description, avocat_image, schedule, rating, comments, social, wilaya, longitude, latitude, categories_id)
VALUES
    ('Jane', 'Smith', 'janesmith@example.com', '987-654-3210', '456 Elm St, Anytown, CA', 'Expert in criminal defense and personal injury', 'https://example.com/lawyer-image2.jpg', 1, 4.8, 1, 'https://facebook.com/janesmith', 'Oran', 35.6953, -0.6335,1),
    ('Peter', 'Johnson', 'peterjohnson@example.com', '555-1212', '789 Oak St, Anytown, CA', 'Specializes in business law and estate planning', 'https://example.com/lawyer-image3.jpg', 2, 4.2, 2, 'https://facebook.com/peterjohnson', 'Annaba', 36.9054, 7.7559,2),
    ('Maria', 'Garcia', 'mariagarcia@example.com', '444-5555', '901 Pine St, Anytown, CA', 'Helping clients with immigration and employment law issues', 'https://example.com/lawyer-image4.jpg', 3, 3.9, 3, 'https://facebook.com/mariagarcia', 'Constantine', 36.3650, 6.6150,3),
    ('David', 'Lee', 'davidlee@example.com', '333-6666', '102 Birch St, Anytown, CA', 'Experienced in intellectual property and real estate law', 'https://example.com/lawyer-image5.jpg', 4, 4.7, 4, 'https://facebook.com/davidlee', 'Tlemcen', 34.8758, -1.3154,4),
    ('Emily', 'Wang', 'emilywang@example.com', '222-7777', '113 Maple St, Anytown, CA', 'Providing legal counsel for businesses and individuals', 'https://example.com/lawyer-image6.jpg', 5, 4.1,5 , 'https://facebook.com/emilywang', 'Sétif', 36.1919, 5.4154,5)




-- REMOVE all the rows in the lawyers table

-- remove column SCHEDULE and comments from lawyers table

ALTER TABLE lawyers
DROP COLUMN schedule,
DROP COLUMN comments;



-- add table commens

CREATE TABLE comments (
    id INTEGER NOT NULL,
    comment VARCHAR(255) NOT NULL,
    lawyer_id INTEGER NOT NULL,
    PRIMARY KEY (id)
);

-- add table schedules

CREATE TABLE schedules (
    id INTEGER NOT NULL,
    schedule VARCHAR(255) NOT NULL,
    lawyer_id INTEGER NOT NULL,
    PRIMARY KEY (id)
);


-- insert soem comments

INSERT INTO comments (id, comment, lawyer_id)
VALUES
    (1, 'Great lawyer, very knowledgeable', 1),
    (2, 'I would recommend this lawyer', 1),
    (3, 'I would not recommend this lawyer', 2),
    (4, 'Very professional and courteous', 3),
    (5, 'I would recommend this lawyer', 3),
    (6, 'I would not recommend this lawyer', 4),
    (7, 'Great lawyer, very knowledgeable', 4),
    (8, 'I would recommend this lawyer', 5),
    (9, 'I would not recommend this lawyer', 5);



-- insert some schedules

INSERT INTO schedules (id, schedule, lawyer_id)
VALUES
    (1, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 1),
    (2, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 2),
    (3, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 3),
    (4, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 4),
    (5, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 5);    

DELETE FROM lawyers


--  create table categories

CREATE TABLE categories (
    id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- and now change the categories column in lawyers table to be a foreign key to categories table

ALTER TABLE lawyers
ADD COLUMN categories_id INTEGER NOT NULL REFERENCES categories (id);


--  remove the categories column from lawyers table

ALTER TABLE lawyers
DROP COLUMN categories;


--  insert some categories
-- this values "Droit administratif", "Droit bancaire", "Droit civil", "Droit commercial", "Droit de l'environnement", "Droit de l'immobilier", "Droit de la consommation", "Droit de la santé", "Droit des assurances", "Droit des entreprises", "Droit des transports", "Droit du sport", "Droit du travail", "Droit familial", "Droit pénal", "Droit routier"
INSERT INTO categories (id , name)
VALUES
    (1, 'Droit administratif'),
    (2, 'Droit bancaire'),
    (3, 'Droit civil'),
    (4, 'Droit commercial'),
    (5, 'Droit de l\'environnement'),
    (6, 'Droit de l\'immobilier'),
    (7, 'Droit de la consommation'),
    (8, 'Droit de la santé'),
    (9, 'Droit des assurances'),
    (10, 'Droit des entreprises'),
    (11, 'Droit des transports'),
    (12, 'Droit du sport'),
    (13, 'Droit du travail'),
    (14, 'Droit familial'),
    (15, 'Droit pénal'),
    (16, 'Droit routier');


-- get the categories
SELECT  * FROM categories


SELECT * FROM lawyers 


SELECT * FROM comments


SELECT * FROM schedules





