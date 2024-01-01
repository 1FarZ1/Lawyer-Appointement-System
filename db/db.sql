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

