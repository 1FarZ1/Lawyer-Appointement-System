SELECT * FROM users





--  get lawyers

SELECT * FROM lawyers




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

INSERT INTO lawyers (name, fname, email, phone, address, description, avocat_image, categories, schedule, rating, comments, social, wilaya, longitude, latitude)
VALUES
    ('Jane', 'Smith', 'janesmith@example.com', '987-654-3210', '456 Elm St, Anytown, CA', 'Expert in criminal defense and personal injury', 'https://example.com/lawyer-image2.jpg', 'Criminal Law, Personal Injury, DUI', 'serialized_schedule2', 4.8, 'serialized_comments2', 'https://facebook.com/janesmith', 'Oran', 35.6953, -0.6335),
    ('Peter', 'Johnson', 'peterjohnson@example.com', '555-1212', '789 Oak St, Anytown, CA', 'Specializes in business law and estate planning', 'https://example.com/lawyer-image3.jpg', 'Business Law, Estate Planning, Contracts', 'serialized_schedule3', 4.2, 'serialized_comments3', 'https://facebook.com/peterjohnson', 'Annaba', 36.9054, 7.7559),
    ('Maria', 'Garcia', 'mariagarcia@example.com', '444-5555', '901 Pine St, Anytown, CA', 'Helping clients with immigration and employment law issues', 'https://example.com/lawyer-image4.jpg', 'Immigration Law, Employment Law, Labor Law', 'serialized_schedule4', 3.9, 'serialized_comments4', 'https://facebook.com/mariagarcia', 'Constantine', 36.3650, 6.6150),
    ('David', 'Lee', 'davidlee@example.com', '333-6666', '102 Birch St, Anytown, CA', 'Experienced in intellectual property and real estate law', 'https://example.com/lawyer-image5.jpg', 'Intellectual Property, Real Estate, Contracts', 'serialized_schedule5', 4.7, 'serialized_comments5', 'https://facebook.com/davidlee', 'Tlemcen', 34.8758, -1.3154),
    ('Emily', 'Wang', 'emilywang@example.com', '222-7777', '113 Maple St, Anytown, CA', 'Providing legal counsel for businesses and individuals', 'https://example.com/lawyer-image6.jpg', 'Business Law, Contract Law, Litigation', 'serialized_schedule6', 4.1, 'serialized_comments6', 'https://facebook.com/emilywang', 'Sétif', 36.1919, 5.4154)
