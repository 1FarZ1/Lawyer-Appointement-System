-- Active: 1701266548715@@127.0.0.1@3306@genie


SELECT * FROM `user`;

SELECT * FROM categorie


SELECT * FROM lawyer


SELECT * FROM review


SELECT * FROM appointement


-- add appointment
INSERT INTO appointement (id, lawyer_id, user_id, date, time, status)
VALUES
    (1, 1, 1, '2021-05-20', '10:00:00', 'pending'),
    (2, 1, 1, '2021-05-20', '11:00:00', 'pending'),
    (3, 1, 1, '2021-05-20', '12:00:00', 'pending'),
    (4, 1, 1, '2021-05-20', '13:00:00', 'pending'),
    (5, 1, 1, '2021-05-20', '14:00:00', 'pending'),
    (6, 1, 1, '2021-05-20', '15:00:00', 'pending'),
    (7, 1, 1, '2021-05-20', '16:00:00', 'pending'),
    (8, 1, 1, '2021-05-20', '17:00:00', 'pending'),
    (9, 1, 1, '2021-05-20', '18:00:00', 'pending'),
    (10, 1, 1, '2021-05-20', '19:00:00', 'pending'),
    (11, 1, 1, '2021-05-20', '20:00:00', 'pending'),
    (12, 1, 1, '2021-05-20', '21:00:00', 'pending'),
    (13, 1, 1, '2021-05-20', '22:00:00', 'pending'),
    (14, 1, 1, '2021-05-20', '23:00:00', 'pending'),
    (15, 1, 1, '2021-05-20', '00:00:00', 'pending'),
    (16, 1, 1, '2021-05-20', '01:00:00', 'pending'),
    (17, 1, 1, '2021-05-20', '02:00:00', 'pending');



-- add lawyer SCHEDULE
INSERT INTO lawyer_schedule (id, lawyer_id, day_of_week, start_time, end_time)
VALUES   (1, 1, 'Monday', '08:00:00', '10:00:00'),
    (2, 1, 'Tuesday', '10:00:00', '12:00:00'),
    (3, 1, 'Wednesday', '12:00:00', '14:00:00'),
    (4, 1, 'Thursday', '14:00:00', '16:00:00'),
    (5, 1, 'Friday', '16:00:00', '18:00:00'),
    (6, 1, 'Saturday', '18:00:00', '20:00:00'),
    (7, 1, 'Sunday', '08:00:00', '10:00:00'),
    (8, 1, 'Monday', '10:00:00', '12:00:00'),
    (9, 1, 'Tuesday', '12:00:00', '14:00:00'),
    (10, 1, 'Wednesday', '14:00:00', '16:00:00');



-- delete all the rows in user TABLE
DELETE FROM user;




-- add some schedule into the schedule table
INSERT INTO lawyer_schedule (id, lawyer_id, date, start_time, end_time)
VALUES   (1, 1, 'Monday', '08:00:00', '10:00:00'),
    (2, 1, 'Tuesday', '10:00:00', '12:00:00'),
    (3, 1, 'Wednesday', '12:00:00', '14:00:00'),
    (4, 1, 'Thursday', '14:00:00', '16:00:00'),
    (5, 1, 'Friday', '16:00:00', '18:00:00'),
    (6, 1, 'Saturday', '18:00:00', '20:00:00'),
    (7, 1, 'Sunday', '08:00:00', '10:00:00'),
    (8, 1, 'Monday', '10:00:00', '12:00:00'),
    (9, 1, 'Tuesday', '12:00:00', '14:00:00'),
    (10, 1, 'Wednesday', '14:00:00', '16:00:00');