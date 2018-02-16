INSERT INTO "expenses" (name, amount, date, "user_id", "category_id") VALUES ('comida china', 34.5, current_timestamp, 1, 2),
('comida china', 34.5, current_timestamp, 1, 2),
('Recurse Center', 34.5, current_timestamp, 1, 27),
('Saga', 34.5, current_timestamp, 1, 28),
('Vietnamita', 34.5, current_timestamp, 1, 2);


INSERT INTO "expenses" (name, amount, date, "user_id", "category_id") VALUES ('comida china', 34.5, current_timestamp, 4, 2),
('comida china', 34.5, current_timestamp, 4, 2),
('Recurse Center', 34.5, current_timestamp, 4, 27),
('Saga', 34.5, current_timestamp, 4, 28),
('Vietnamita', 34.5, current_timestamp, 4, 2);


INSERT INTO "months" (year_month_usr, user_id) VALUES 
(201821, 1),
(201811, 1),
(2017121, 1),
(2017111, 1),
(2017101, 1);



INSERT INTO "expenses" (name, amount, date, "user_id", "category_id", "month_id") VALUES
('comida china', 34.5, '2001-09-29 03:00', 1, 2, 201821),
('comida china', 31.5, '2001-09-29 03:00', 1, 2, 201821),
('Recurse Center', 31.5, '2001-09-29 03:00', 1, 27, 201811),
('Saga', 31.5, '2001-09-29 03:00', 1, 28, 201821),
('comida china', 31.5, '2001-09-29 03:00', 1, 2, 201811),
('comida china', 31.5, '2017-09-29 03:00', 1, 2, 201811),
('Recurse Center', 31.5, '2017-09-29 03:00', 1, 27, 201811),
('Saga', 31.5, '2017-09-29 03:00', 1, 28, 2017121),
('comida china', 31.5, '2017-09-29 03:00', 1, 2, 2017121),
('comida china', 31.5, '2017-09-29 03:00', 1, 2, 2017121),
('Recurse Center', 31.5, '2017-10-29 03:00', 1, 27, 2017121),
('Saga', 31.5, '2017-10-29 03:00', 1, 28, 2017111),
('comida china', 31.5, '2017-10-29 03:00', 1, 2, 2017111),
('comida china', 31.5, '2017-12-29 03:00', 1, 2, 2017111),
('Recurse Center', 31.5, '2017-12-29 03:00', 1, 27, 2017101),
('Saga', 31.5, '2017-12-29 03:00', 1, 28, 2017101),
('Vietnamita', 31.5, '2017-12-29 03:00', 1, 2, 2017101);