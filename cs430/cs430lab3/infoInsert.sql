INSERT INTO Author VALUES
(101, 'Bobby', 'Ewing'),
(102, 'Red', 'Skelton'),
(201, 'Thomas', 'Magnum'),
(202, 'Julie', 'Barnes'),
(203, 'Roger', 'Ramjet'),
(204, 'Mickey', 'Hart'),
(205, 'Grace', 'Slick'),
(206, 'Perry', 'Mason'),
(207, 'Dickey', 'Betts'),
(208, 'Waco', 'Kid'),
(209, 'Roger', 'Thornhill'),
(210, 'Scottie', 'Ferguson'),
(301, 'Barbara', 'Wright'),
(302, 'John', 'Crichton'),
(303, 'Aeon', 'Flux'),
(304, 'Robert', 'Crawley');


INSERT INTO Publisher VALUES
(10000, 'Wiley'),
(10001, 'McGraw-Hill'),
(10002, 'Coyote Publishing'),
(10003, 'Amazon'),
(10004, 'Jerrys Ice Cream'),
(10005, 'Buy a Boat'),
(10006, 'Flagstaff Publishing'),
(10007, 'Ram West');


INSERT INTO Phone VALUES
('970-555-1000', '(c)'),
('970-555-1010', '(h)'),
('970-555-1100', '(o)'),
('303-555-1200', '(h)'),
('303-555-1210', '(c)'),
('970-555-1400', '(c)'),
('970-555-1600', '(h)'),
('970-555-1800', '(c)'),
('970-555-1900', '(h)'),
('970-555-2000', '(h)'),
('970-555-2010', '(c)'),
('970-555-2001', '(h)'),
('970-555-2020', '(c)'),
('970-555-2300', '(o)'),
('970-555-2400', '(h)'),
('970-555-2401', '(c)'),
('970-555-2403', '(o)'),
('970-555-2402', '(c)');


INSERT INTO Phone VALUES
('970-555-5000', '(o)'),
('970-555-5010', '(o)'),
('970-555-5020', '(o)'),
('970-555-5030', '(o)'),
('970-555-5040', '(o)'),
('970-555-5050', '(o)'),
('970-555-5060', '(o)'),
('970-555-5070', '(c)'),
('970-555-5080', '(o)');


INSERT INTO PublisherPhone VALUES
(10000, '970-555-5000'),
(10001, '970-555-5010'),
(10002, '970-555-5020'),
(10003, '970-555-5030'),
(10004, '970-555-5040'),
(10005, '970-555-5050'),
(10006, '970-555-5060'),
(10006, '970-555-5070'),
(10007, '970-555-5080');

INSERT INTO AuthorPhone VALUES
(101, '970-555-1000'),
(101, '970-555-1010'),
(102, '970-555-1100'),
(201, '303-555-1200'),
(202, '303-555-1200'),
(202, '303-555-1210'),
(203, '970-555-1400'),
(205, '970-555-1600'),
(206, '970-555-1600'),
(207, '970-555-1800'),
(208, '970-555-1900'),
(209, '970-555-2000'),
(209, '970-555-2010'),
(210, '970-555-2001'),
(301, '970-555-2020'),
(302, '970-555-2300'),
(303, '970-555-2400'),
(303, '970-555-2401'),
(303, '970-555-2403'),
(304, '970-555-2400'),
(304, '970-555-2402'),
(304, '970-555-2403');

INSERT INTO Member VALUES
(1000, 'Wiley', 'Coyote', '1961-9-10', 'M'),
(1100, 'Bugs', 'Bunny', '1990-6-24', 'M'),
(1200, 'Olive', 'Oyl', '1989-7-19', 'F'),
(1300, 'Alice', 'Wonderland', '1989-7-19', 'F'),
(1400, 'Roger', 'Ramjet', '1985-1-13', 'M'),
(1500, 'Larry', 'Lujack', '1940-6-6', 'M'),
(1600, 'Thomas', 'Tankengine', '1991-4-1', 'M'),
(1700, 'Amber', 'Corwin', '1970-12-1', 'F'),
(1800, 'Dworkin', 'Barimen', '1950-12-2', 'M'),
(1900, 'Bel', 'Garion', '1983-1-1', 'M'),
(2000, 'Pol', 'Gara', '1963-1-10', 'F'),
(2001, 'Art', 'Clark', '2001-12-6', 'M'),
(2002, 'Edith', 'Crawley', '1962-9-4', 'F'),
(2003, 'John', 'Bates', '2001-12-12', 'M'),
(2004, 'Thomas', 'Barrow', '2005-5-5', 'M'),
(2005, 'John', 'Watson', '1975-2-22', 'M'),
(2006, 'Jim', 'Moriarty', '1967-3-12', 'M'),
(2007, 'Walter', 'White', '1983-5-14', 'M'),
(2008, 'Skyler', 'White', '1983-4-12', 'F'),
(2009, 'Dexter', 'Morgan', '1994-7-11', 'M'),
(2010, 'Rita', 'Bennett', '2001-11-12', 'F'),
(2011, 'Sun', 'Kwon', '1988-10-19', 'F'),
(2012, 'John', 'Locke', '2000-1-1', 'M'),
(2013, 'Clair', 'Littleton', '2001-2-1', 'F'),
(2015, 'Claire', 'Bennet', '2001-3-11', 'F'),
(2016, 'Mohinder', 'Suresh', '1993-4-15', 'M'),
(2017, 'Chloe', 'Sullivan', '2007-5-16', 'F'),
(2018, 'Martha', 'Kent', '1954-2-13', 'F'),
(2019, 'Paige', 'Matthews', '1977-3-16', 'F'),
(2020, 'Leo', 'Wyatt', '2000-10-1', 'M'),
(2021, 'Buffy', 'Summers', '2000-5-26', 'F'),
(2022, 'Xander', 'Harris', '2001-6-23', 'M');

INSERT INTO Book VALUES
('96-42103-11800', 'Blue is Your Friend', 2010, 10002),
('96-42103-10007', 'How to Digitally Sign', 2003, 10004),
('96-42103-10022', 'Challenging Puzzles', 1988, 10001),
('96-42103-10502', 'Gardening Tips', 1973, 10007),
('96-42103-10401', 'How to Grow Cucumbers', 1945, 10006),
('96-42103-10011', 'Database Theory', 2010, 10001),
('96-42103-10109', 'Red Burn', 2011, 10000),
('96-42103-10093', 'Fixing Computers', 2010, 10000),
('96-42103-10800', 'Green is Your Friend', 2000, 10006),
('96-42103-11709', 'Green Eggs', 1983, 10003),
('96-42103-10300', 'Eating Healthy', 1999, 10004),
('96-42103-10040', 'Where to Start', 2012, 10003),
('96-42103-10081', 'Escape from Gilligans Island', 2009, 10000),
('96-42103-10006', 'Last Train to Clarksville', 1999, 10004),
('96-42103-10002', 'Mr. Smith Goes to Washington', 2010, 10007),
('96-42103-10709', 'Too Many Cooks', 1983, 10006),
('96-42103-10004', 'To Have and To Cherish', 2011, 10003),
('96-42103-10005', 'Hal Finds a Home', 2001, 10003),
('96-42103-10604', 'Using the Library', 1993, 10003),
('96-42103-10068', 'Mr. Ed', 2009, 10001),
('96-42103-10001', 'How to Grow Tomatoes', 1963, 10006),
('96-42103-10003', 'Studying is Your Friend', 1955, 10000),
('96-42103-11604', 'Eating in the Fort', 1993, 10002),
('96-42103-10033', 'American Football', 2011, 10006),
('96-42103-11003', 'Missing Tomorrow', 2005, 10001),
('96-42103-10009', 'Downton Abbey', 2005, 10002),
('96-42103-10034', 'European Football', 2015, 10003),
('96-42103-10907', 'Cubs Win!', 2005, 10002),
('96-42103-10206', 'Taks McGrill', 2000, 10003),
('96-42103-10008', 'Sam Needs a Friend', 2013, 10005),
('96-42103-10054', 'Lacey Discovers Herself', 2013, 10002);

INSERT INTO WrittenBy VALUES
('96-42103-10011', 207),
('96-42103-10502', 201),
('96-42103-10007', 302),
('96-42103-10068', 210),
('96-42103-10008', 210),
('96-42103-10008', 209),
('96-42103-10401', 101),
('96-42103-10005', 204),
('96-42103-10040', 205),
('96-42103-10081', 101),
('96-42103-10011', 208),
('96-42103-10081', 204),
('96-42103-10054', 202),
('96-42103-10009', 304),
('96-42103-10109', 304),
('96-42103-11709', 201),
('96-42103-11800', 301),
('96-42103-11003', 207),
('96-42103-11709', 303),
('96-42103-10093', 102),
('96-42103-10502', 202),
('96-42103-10709', 303),
('96-42103-10800', 302),
('96-42103-11604', 201),
('96-42103-10001', 208),
('96-42103-10300', 208),
('96-42103-10003', 201),
('96-42103-10040', 203),
('96-42103-10109', 208),
('96-42103-10300', 207),
('96-42103-10002', 102),
('96-42103-10034', 202),
('96-42103-10907', 301),
('96-42103-10907', 102),
('96-42103-10401', 203),
('96-42103-10003', 203),
('96-42103-10206', 210),
('96-42103-10004', 304),
('96-42103-11003', 204),
('96-42103-11800', 302),
('96-42103-10709', 201),
('96-42103-10022', 203),
('96-42103-10604', 201),
('96-42103-11003', 205),
('96-42103-10004', 302),
('96-42103-10001', 101),
('96-42103-10008', 301),
('96-42103-10206', 301),
('96-42103-10054', 201),
('96-42103-11003', 206),
('96-42103-10033', 202),
('96-42103-10800', 301),
('96-42103-10006', 101),
('96-42103-10007', 102),
('96-42103-10004', 209);


INSERT INTO BorrowedBy VALUES
(1100, '96-42103-10604', 'Main', '2016-04-13', '2016-04-17'),
(1100, '96-42103-10604', 'Main', '2016-03-09', '2016-03-10'),
(1100, '96-42103-10003', 'Main', '2016-03-23', '2016-03-24'),
(1100, '96-42103-10401', 'Main', '2016-05-14', '2016-05-16'),
(1100, '96-42103-10001', 'Main', '2016-04-27', '2016-04-30'),
(1100, '96-42103-10040', 'Main', '2016-05-16', '2016-05-16'),
(1100, '96-42103-10709', 'Main', '2016-05-18', '2016-05-21'),
(1100, '96-42103-10081', 'Main', '2016-03-15', '2016-03-17'),
(1200, '96-42103-10081', 'Main', '2016-04-10', '2016-04-16'),
(1200, '96-42103-10093', 'Main', '2016-03-27', '2016-03-29'),
(1200, '96-42103-10109', 'Main', '2016-04-15', '2016-04-18'),
(1300, '96-42103-10022', 'Main', '2016-03-09', '2016-03-10'),
(1300, '96-42103-10206', 'Main', '2016-05-11', '2016-05-14'),
(1300, '96-42103-10007', 'Main', '2016-05-11', '2016-05-12'),
(1300, '96-42103-10001', 'Main', '2016-03-28', '2016-04-04'),
(1300, '96-42103-10008', 'Main', '2016-04-20', '2016-04-26'),
(1400, '96-42103-10033', 'Main', '2016-03-26', '2016-03-29'),
(1400, '96-42103-10800', 'Main', '2016-03-04', '2016-03-06'),
(1400, '96-42103-10008', 'Main', '2016-05-24', '2016-05-29'),
(1400, '96-42103-10007', 'Main', '2016-05-06', '2016-05-11'),
(1400, '96-42103-11003', 'Main', '2016-03-05', '2016-03-10'),
(1400, '96-42103-10022', 'Main', '2016-03-04', '2016-03-07'),
(1500, '96-42103-10004', 'Main', '2016-05-14', '2016-05-16'),
(1500, '96-42103-10800', 'Main', '2016-04-02', '2016-04-05'),
(1600, '96-42103-10206', 'Main', '2016-05-21', '2016-05-27'),
(1600, '96-42103-10002', 'Main', '2016-05-04', '2016-05-09'),
(1600, '96-42103-10011', 'Main', '2016-03-20', '2016-03-20'),
(1600, '96-42103-10800', 'Main', '2016-05-10', '2016-05-13'),
(1600, '96-42103-10300', 'Main', '2016-03-22', '2016-03-24'),
(1700, '96-42103-10040', 'Main', '2016-05-18', '2016-05-21'),
(1700, '96-42103-10604', 'Main', '2016-04-17', '2016-04-18'),
(1700, '96-42103-11003', 'Main', '2016-04-17', '2016-04-20'),
(1700, '96-42103-10004', 'Main', '2016-04-05', '2016-04-11'),
(1700, '96-42103-10081', 'Main', '2016-03-05', '2016-03-08'),
(1700, '96-42103-10800', 'Main', '2016-04-22', '2016-04-28'),
(1800, '96-42103-10011', 'Main', '2016-04-25', '2016-04-26'),
(1900, '96-42103-10008', 'Main', '2016-05-01', '2016-05-01'),
(2000, '96-42103-10093', 'Main', '2016-04-12', '2016-04-12'),
(2000, '96-42103-10005', 'Main', '2016-05-17', '2016-05-21'),
(2000, '96-42103-10109', 'Main', '2016-05-09', '2016-05-11'),
(2000, '96-42103-10006', 'Main', '2016-05-08', '2016-05-11'),
(2001, '96-42103-10040', 'Main', '2016-04-22', '2016-04-25'),
(2002, '96-42103-10040', 'Main', '2016-05-22', '2016-05-27'),
(2002, '96-42103-10008', 'Main', '2016-04-21', '2016-04-25'),
(2002, '96-42103-10081', 'Main', '2016-03-04', '2016-03-06'),
(2002, '96-42103-10006', 'Main', '2016-04-27', '2016-05-02'),
(2003, '96-42103-10040', 'Main', '2016-04-09', '2016-04-14'),
(2003, '96-42103-10033', 'Main', '2016-03-14', '2016-03-15'),
(2003, '96-42103-10068', 'Main', '2016-04-12', '2016-04-16'),
(2004, '96-42103-10800', 'Main', '2016-05-13', '2016-05-17'),
(2004, '96-42103-10040', 'Main', '2016-04-27', '2016-05-02'),
(2004, '96-42103-10007', 'Main', '2016-04-21', '2016-04-23'),
(2004, '96-42103-10907', 'Main', '2016-05-09', '2016-05-10'),
(2004, '96-42103-10800', 'Main', '2016-05-24', '2016-05-28'),
(2005, '96-42103-10011', 'Main', '2016-04-20', '2016-04-22'),
(2006, '96-42103-10800', 'Main', '2016-04-04', '2016-04-04'),
(2007, '96-42103-10709', 'Main', '2016-03-13', '2016-03-17'),
(2007, '96-42103-10033', 'Main', '2016-03-19', '2016-03-24'),
(2007, '96-42103-10068', 'Main', '2016-04-19', '2016-04-20'),
(2008, '96-42103-10502', 'Main', '2016-03-12', '2016-03-14'),
(2008, '96-42103-11003', 'Main', '2016-04-04', '2016-04-08'),
(2009, '96-42103-10022', 'Main', '2016-03-24', '2016-03-30'),
(2009, '96-42103-10709', 'Main', '2016-04-12', '2016-04-15'),
(2009, '96-42103-10022', 'Main', '2016-04-10', '2016-04-10'),
(2009, '96-42103-10009', 'Main', '2016-03-20', '2016-03-22'),
(2009, '96-42103-10033', 'Main', '2016-04-30', '2016-05-02'),
(2009, '96-42103-10007', 'Main', '2016-03-07', '2016-03-13'),
(2009, '96-42103-10002', 'Main', '2016-04-12', '2016-04-13'),
(2009, '96-42103-10709', 'Main', '2016-04-30', '2016-05-03'),
(2009, '96-42103-10054', 'Main', '2016-04-29', '2016-05-02'),
(2011, '96-42103-10093', 'Main', '2016-04-20', '2016-04-20'),
(2011, '96-42103-10011', 'Main', '2016-03-09', '2016-03-11'),
(2011, '96-42103-10081', 'Main', '2016-03-15', '2016-03-20'),
(2011, '96-42103-10800', 'Main', '2016-05-29', NULL),
(2011, '96-42103-11003', 'Main', '2016-03-06', '2016-03-08'),
(2011, '96-42103-10040', 'Main', '2016-03-10', '2016-03-16'),
(2012, '96-42103-10009', 'Main', '2016-03-28', '2016-03-29'),
(2012, '96-42103-10006', 'Main', '2016-03-24', '2016-03-28'),
(2012, '96-42103-11003', 'Main', '2016-04-04', '2016-04-09'),
(2012, '96-42103-10008', 'Main', '2016-04-26', '2016-04-28'),
(2012, '96-42103-10002', 'Main', '2016-05-27', NULL),
(2013, '96-42103-10008', 'Main', '2016-04-19', '2016-04-23'),
(2013, '96-42103-10054', 'Main', '2016-03-26', '2016-03-29'),
(2013, '96-42103-10033', 'Main', '2016-05-17', '2016-05-21'),
(2015, '96-42103-10009', 'Main', '2016-03-15', '2016-03-19'),
(2016, '96-42103-10033', 'Main', '2016-04-28', '2016-04-30'),
(2016, '96-42103-10907', 'Main', '2016-04-22', '2016-04-28'),
(2016, '96-42103-10206', 'Main', '2016-05-09', '2016-05-14'),
(2016, '96-42103-10907', 'Main', '2016-03-06', '2016-03-08'),
(2016, '96-42103-10907', 'Main', '2016-03-21', '2016-03-22'),
(2016, '96-42103-10001', 'Main', '2016-04-07', '2016-04-08'),
(2016, '96-42103-10206', 'Main', '2016-05-15', '2016-05-15'),
(2017, '96-42103-10709', 'Main', '2016-04-20', '2016-04-25'),
(2017, '96-42103-10300', 'Main', '2016-05-20', '2016-05-26'),
(2017, '96-42103-10093', 'Main', '2016-03-19', '2016-03-23'),
(2017, '96-42103-10300', 'Main', '2016-05-01', '2016-05-05'),
(2017, '96-42103-10004', 'Main', '2016-03-14', '2016-03-16'),
(2018, '96-42103-10033', 'Main', '2016-03-05', '2016-03-07'),
(2018, '96-42103-10004', 'Main', '2016-03-25', '2016-03-27'),
(2018, '96-42103-10907', 'Main', '2016-03-16', '2016-03-20'),
(2018, '96-42103-10008', 'Main', '2016-05-10', '2016-05-10'),
(2018, '96-42103-10033', 'Main', '2016-04-01', '2016-04-07'),
(2018, '96-42103-10300', 'Main', '2016-04-05', '2016-04-10'),
(2018, '96-42103-10206', 'Main', '2016-03-05', '2016-03-11'),
(2018, '96-42103-10709', 'Main', '2016-04-20', '2016-04-25'),
(2018, '96-42103-10206', 'Main', '2016-05-12', '2016-05-17'),
(2019, '96-42103-10009', 'Main', '2016-03-11', '2016-03-12'),
(2020, '96-42103-10022', 'Main', '2016-04-09', '2016-04-10'),
(2020, '96-42103-10206', 'Main', '2016-05-13', '2016-05-18'),
(2020, '96-42103-10093', 'Main', '2016-04-08', '2016-04-12'),
(2020, '96-42103-10401', 'Main', '2016-05-29', NULL),
(2021, '96-42103-10033', 'Main', '2016-03-14', '2016-03-16'),
(2021, '96-42103-10001', 'Main', '2016-05-21', '2016-05-26'),
(2021, '96-42103-10054', 'Main', '2016-04-29', '2016-04-30'),
(2022, '96-42103-10009', 'Main', '2016-03-25', '2016-03-29'),
(2022, '96-42103-10011', 'Main', '2016-05-03', '2016-05-06'),
(2022, '96-42103-10109', 'Main', '2016-04-16', '2016-04-21'),
(2022, '96-42103-11003', 'Main', '2016-06-01', NULL),
(2022, '96-42103-10081', 'Main', '2016-03-26', '2016-03-30'),
(2022, '96-42103-10093', 'Main', '2016-03-27', '2016-03-29'),
(2022, '96-42103-10502', 'Main', '2016-03-26', '2016-04-01'),
(2022, '96-42103-10003', 'Main', '2016-05-06', '2016-05-09');



INSERT INTO Library VALUES
('Main', '42 South Main', 'Fort Collins', 'CO'),
('South Park', '4000 South College', 'Fort Collins', 'CO');



INSERT INTO LocatedAt VALUES
('96-42103-10001', 'Main', 1, 1, 3, 3),
('96-42103-10002', 'Main', 1, 1, 0, 1),
('96-42103-10003', 'Main', 1, 1, 1, 1),
('96-42103-10004', 'Main', 1, 2, 2, 2),
('96-42103-10005', 'Main', 1, 2, 1, 1),
('96-42103-10006', 'Main', 1, 2, 1, 1),
('96-42103-10007', 'Main', 1, 3, 2, 2),
('96-42103-10008', 'Main', 1, 3, 2, 2),
('96-42103-10009', 'Main', 1, 3, 2, 2),
('96-42103-10011', 'Main', 1, 4, 2, 2),
('96-42103-10022', 'Main', 1, 4, 3, 3),
('96-42103-10033', 'Main', 1, 4, 3, 3),
('96-42103-10034', 'Main', 2, 5, 1, 1),
('96-42103-10040', 'Main', 2, 5, 2, 2),
('96-42103-10054', 'Main', 2, 5, 2, 2),
('96-42103-10068', 'Main', 2, 6, 1, 1),
('96-42103-10081', 'Main', 2, 6, 1, 1),
('96-42103-10093', 'Main', 2, 6, 1, 1),
('96-42103-10109', 'Main', 2, 6, 1, 1),
('96-42103-10206', 'Main', 2, 7, 1, 1),
('96-42103-10300', 'Main', 2, 7, 2, 2),
('96-42103-10401', 'Main', 2, 7, 1, 2),
('96-42103-10502', 'Main', 2, 7, 1, 1),
('96-42103-10604', 'Main', 2, 8, 2, 2),
('96-42103-10709', 'Main', 2, 8, 3, 3),
('96-42103-10800', 'Main', 2, 8, 1, 2),
('96-42103-10907', 'Main', 2, 8, 7, 7),
('96-42103-11003', 'Main', 2, 8, 2, 3),
('96-42103-10001', 'South Park', 3, 8, 1, 1),
('96-42103-10002', 'South Park', 3, 8, 1, 1),
('96-42103-10003', 'South Park', 3, 8, 1, 1),
('96-42103-10004', 'South Park', 3, 8, 1, 1),
('96-42103-10005', 'South Park', 3, 8, 1, 1),
('96-42103-10006', 'South Park', 3, 8, 1, 1),
('96-42103-10007', 'South Park', 3, 7, 3, 3),
('96-42103-10008', 'South Park', 3, 7, 3, 3),
('96-42103-10009', 'South Park', 3, 7, 1, 1),
('96-42103-10011', 'South Park', 3, 7, 1, 1),
('96-42103-10022', 'South Park', 3, 7, 2, 2),
('96-42103-10033', 'South Park', 3, 7, 3, 3),
('96-42103-10040', 'South Park', 2, 4, 1, 1),
('96-42103-10054', 'South Park', 2, 4, 1, 1),
('96-42103-10068', 'South Park', 2, 4, 1, 1),
('96-42103-10081', 'South Park', 2, 4, 1, 1),
('96-42103-10093', 'South Park', 2, 4, 1, 1),
('96-42103-10109', 'South Park', 2, 4, 1, 1),
('96-42103-10206', 'South Park', 2, 4, 1, 1),
('96-42103-10300', 'South Park', 2, 4, 1, 1),
('96-42103-10401', 'South Park', 2, 3, 1, 1),
('96-42103-10502', 'South Park', 2, 3, 1, 1),
('96-42103-11604', 'South Park', 2, 3, 2, 2),
('96-42103-11709', 'South Park', 2, 3, 1, 1),
('96-42103-11800', 'South Park', 2, 3, 2, 2),
('96-42103-10907', 'South Park', 2, 3, 7, 7),
('96-42103-11003', 'South Park', 2, 3, 2, 2);
