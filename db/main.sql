-- SELECT * FROM `user`;

-- --  get lawyers

-- SELECT * FROM lawyer


-- DROP TABLE users


-- DROP Table  

-- -- GET THE categories of the lawyers
-- SELECT categories.name FROM lawyers JOIN categories ON lawyers.categories_id = categories.id



-- --  insert some lawyers , here is the SCHEMA
-- --  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
-- --    name = Column(String(50))
-- --    fname = Column(String(50))
-- --    email = Column(String(100), unique=True)
-- --    phone = Column(String(20))
-- --    address = Column(String(255))
-- --    description = Column(String(255))
-- --    avocat_image = Column(String(255))
-- --    categories = Column(String(255))  # Assuming a comma-separated string for categories
-- --    schedule = Column(String(255))  # Assuming a serialized format for schedule
-- --    rating = Column(Float)
-- --    comments = Column(String(255))  # Assuming a serialized format for comments
-- --    social = Column(String(255))
-- --    wilaya = Column(String(50))
-- --    longitude = Column(Float)
-- --    latitude = Column(Float)

-- INSERT INTO lawyer (phone, address, description, avocat_image, rating, social, wilaya, longitude, latitude, categories_id, user_id)
-- VALUES
--     ('987-654-3210','456 Elm St, Anytown, CA', 'Expert in criminal defense and personal injury', 'https://example.com/lawyer-image2.jpg', 4.8,  'https://facebook.com/janesmith', 'Oran', 35.6953, -0.6335,1,1),
--     ( '555-1212', '789 Oak St, Anytown, CA', 'Specializes in business law and estate planning', 'https://example.com/lawyer-image3.jpg', 4.2,  'https://facebook.com/peterjohnson', 'Annaba', 36.9054, 7.7559,1,6);
--     -- ('444-5555', '901 Pine St, Anytown, CA', 'Helping clients with immigration and employment law issues', 'https://example.com/lawyer-image4.jpg', 3.9,  'https://facebook.com/mariagarcia', 'Constantine', 36.3650, 6.6150,3),
--     -- ( '333-6666', '102 Birch St, Anytown, CA', 'Experienced in intellectual property and real estate law', 'https://example.com/lawyer-image5.jpg', 4.7,  'https://facebook.com/davidlee', 'Tlemcen', 34.8758, -1.3154,4),
--     -- ( '222-7777', '113 Maple St, Anytown, CA', 'Providing legal counsel for businesses and individuals', 'https://example.com/lawyer-image6.jpg', 4.1, 'https://facebook.com/emilywang', 'Sétif', 36.1919, 5.4154,5)




-- --  insert some users , here is the SCHEMA
-- INSERT INTO user (id,fname,lname,email,hashed_password)

-- -- give me a json of the user 
-- {

-- -- REMOVE all the rows in the lawyers table

-- -- remove column SCHEDULE and comments from lawyers table

-- ALTER TABLE lawyers
-- DROP COLUMN schedule,
-- DROP COLUMN comments;



-- -- add table commens

-- CREATE TABLE comments (
--     id INTEGER NOT NULL,
--     comment VARCHAR(255) NOT NULL,
--     lawyer_id INTEGER NOT NULL,
--     PRIMARY KEY (id)
-- );

-- -- add table schedules

-- CREATE TABLE schedules (
--     id INTEGER NOT NULL,
--     schedule VARCHAR(255) NOT NULL,
--     lawyer_id INTEGER NOT NULL,
--     PRIMARY KEY (id)
-- );


-- -- insert soem comments

-- INSERT INTO comments (id, comment, lawyer_id)
-- VALUES
--     (1, 'Great lawyer, very knowledgeable', 1),
--     (2, 'I would recommend this lawyer', 1),
--     (3, 'I would not recommend this lawyer', 2),
--     (4, 'Very professional and courteous', 3),
--     (5, 'I would recommend this lawyer', 3),
--     (6, 'I would not recommend this lawyer', 4),
--     (7, 'Great lawyer, very knowledgeable', 4),
--     (8, 'I would recommend this lawyer', 5),
--     (9, 'I would not recommend this lawyer', 5);



-- -- insert some schedules

-- INSERT INTO schedules (id, schedule, lawyer_id)
-- VALUES
--     (1, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 1),
--     (2, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 2),
--     (3, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 3),
--     (4, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 4),
--     (5, 'Monday: 9:00 AM - 5:00 PM, Tuesday: 9:00 AM - 5:00 PM, Wednesday: 9:00 AM - 5:00 PM, Thursday: 9:00 AM - 5:00 PM, Friday: 9:00 AM - 5:00 PM, Saturday: Closed, Sunday: Closed', 5);    

-- DELETE FROM lawyers


-- --  create table categories

-- CREATE TABLE categories (
--     id INTEGER NOT NULL,
--     name VARCHAR(50) NOT NULL,
--     PRIMARY KEY (id)
-- );

-- -- and now change the categories column in lawyers table to be a foreign key to categories table

-- ALTER TABLE lawyers
-- ADD COLUMN categories_id INTEGER NOT NULL REFERENCES categories (id);


-- --  remove the categories column from lawyers table

-- ALTER TABLE lawyers
-- DROP COLUMN categories;


-- --  insert some categories
-- -- this values "Droit administratif", "Droit bancaire", "Droit civil", "Droit commercial", "Droit de l'environnement", "Droit de l'immobilier", "Droit de la consommation", "Droit de la santé", "Droit des assurances", "Droit des entreprises", "Droit des transports", "Droit du sport", "Droit du travail", "Droit familial", "Droit pénal", "Droit routier"
-- INSERT INTO categorie (id , name)
-- VALUES
--     (1, 'Droit administratif'),
--     (2, 'Droit bancaire'),
--     (3, 'Droit civil'),
--     (4, 'Droit commercial'),
--     (5, 'Droit de l\'environnement'),
--     (6, 'Droit de l\'immobilier'),
--     (7, 'Droit de la consommation'),
--     (8, 'Droit de la santé'),
--     (9, 'Droit des assurances'),
--     (10, 'Droit des entreprises'),
--     (11, 'Droit des transports'),
--     (12, 'Droit du sport'),
--     (13, 'Droit du travail'),
--     (14, 'Droit familial'),
--     (15, 'Droit pénal'),
--     (16, 'Droit routier');


-- -- get the categories
-- SELECT  * FROM categories


-- SELECT * FROM lawyers 


-- SELECT * FROM comments


-- SELECT * FROM schedules







-- CREATE TABLE reviews (
--     id INTEGER NOT NULL,
--     lawyer_id INTEGER NOT NULL,
--     user_id INTEGER NOT NULL,
--     rating INTEGER NOT NULL,
--     description VARCHAR(255) NOT NULL,
--     PRIMARY KEY (id),
--     FOREIGN KEY(lawyer_id) REFERENCES lawyers (id),
--     FOREIGN KEY(user_id) REFERENCES users (id)
-- );


-- -- insert some reviews , used id i have are 1,6,8,9  and lawyerrs id : 22,23,24,25,26,27,33,34,35

INSERT INTO review (id, lawyer_id, user_id, rating, description)
VALUES
    (1, 1, 5, 'Great lawyer, very knowledgeable'),
--     (2, 23, 1, 4, 'I would recommend this lawyer'),
--     (3, 24, 1, 3, 'I would not recommend this lawyer'),
--     (4, 25, 1, 5, 'Great lawyer, very knowledgeable'),
--     (5, 26, 1, 4, 'I would recommend this lawyer'),
--     (6, 27, 1, 3, 'I would not recommend this lawyer'),
--     (7, 33, 1, 5, 'Great lawyer, very knowledgeable'),
--     (8, 34, 1, 4, 'I would recommend this lawyer'),
--     (9, 35, 1, 3, 'I would not recommend this lawyer'),
--     (10, 22, 6, 5, 'Great lawyer, very knowledgeable'),
--     (11, 23, 6, 4, 'I would recommend this lawyer'),
--     (12, 24, 6, 3, 'I would not recommend this lawyer'),
--     (13, 25, 6, 5, 'Great lawyer, very knowledgeable'),
--     (14, 26, 6, 4, 'I would recommend this lawyer'),
--     (15, 27, 6, 3, 'I would not recommend this lawyer'),
--     (16, 33, 6, 5, 'Great lawyer, very knowledgeable'),
--     (17, 34, 6, 4, 'I would recommend this lawyer'),
--     (18, 35, 6, 3, 'I would not recommend this lawyer'),
--     (19, 22, 8, 5, 'Great lawyer, very knowledgeable'),
--     (20, 23, 8, 4, 'I would recommend this lawyer'),
--     (21, 24, 8, 3, 'I would not recommend this lawyer'),
--     (22, 25, 8, 5, 'Great lawyer, very knowledgeable'),
--     (23, 26, 8, 4, 'I would recommend this lawyer'),
--     (24, 27, 8, 3, 'I would not recommend this lawyer'),
--     (25, 33, 8, 5, 'Great lawyer, very knowledgeable'),
--     (26, 34, 8, 4, 'I would recommend this lawyer'),
--     (27, 35, 8, 3, 'I would not recommend this lawyer'),
--     (28, 22, 9, 5, 'Great lawyer, very knowledgeable'),
--     (29, 23, 9, 4, 'I would recommend this lawyer'),
--     (30, 24, 9, 3, 'I would not recommend this lawyer'),
--     (31, 25, 9, 5, 'Great lawyer, very knowledgeable'),
--     (32, 26, 9, 4, 'I would recommend this lawyer'),
--     (33, 27, 9, 3, 'I would not recommend this lawyer'),
--     (34, 33, 9, 5, 'Great lawyer, very knowledgeable'),
--     (35, 34, 9, 4, 'I would recommend this lawyer'),
--     (36, 35, 9, 3, 'I would not recommend this lawyer');


-- SELECT * FROM reviews

-- -- view all the tables

