2 activities are not allowed by referential integrity:

	1.Delete Grace Slick from the Author table.

	2. Add a new book to the Main library, ISBN # 96-42013-10513, shelf 8, floor 2, Title Growing your own Weeds, published by pubid 90000 on 6/24/2012.




The result I got according to the output, that show below.


MariaDB [yiboxu]> source activity.sql
Query OK, 1 row affected (0.030 sec)

Query OK, 1 row affected (0.030 sec)

Query OK, 1 row affected (0.030 sec)
Rows matched: 1  Changed: 1  Warnings: 0

ERROR 1451 (23000) at line 17 in file: 'activity.sql': Cannot delete or update a parent row: a foreign key constraint fails (`yiboxu`.`WrittenBy`, CONSTRAINT `WrittenBy_ibfk_2` FOREIGN KEY (`AuthorID`) REFERENCES `Author` (`AuthorID`))
Query OK, 1 row affected (0.024 sec)

Query OK, 1 row affected (0.024 sec)

Query OK, 1 row affected (0.024 sec)

Query OK, 1 row affected (0.024 sec)

Query OK, 1 row affected (0.024 sec)

Query OK, 1 row affected (0.024 sec)
Rows matched: 1  Changed: 1  Warnings: 0

ERROR 1452 (23000) at line 47 in file: 'activity.sql': Cannot add or update a child row: a foreign key constraint fails (`yiboxu`.`Book`, CONSTRAINT `Book_ibfk_1` FOREIGN KEY (`PubID`) REFERENCES `Publisher` (`PubID`))
ERROR 1452 (23000) at line 50 in file: 'activity.sql': Cannot add or update a child row: a foreign key constraint fails (`yiboxu`.`LocatedAt`, CONSTRAINT `LocatedAt_ibfk_2` FOREIGN KEY (`ISBN`) REFERENCES `Book` (`ISBN`) ON DELETE CASCADE)
+----+-----------+--------+---------------------+
| id | TableName | Action | DateTime            |
+----+-----------+--------+---------------------+
|  1 | LocatedAt | INSERT | 2020-07-07 07:58:12 |
|  2 | LocatedAt | UPDATE | 2020-07-07 07:58:12 |
|  3 | Author    | INSERT | 2020-07-07 07:58:12 |
|  4 | LocatedAt | INSERT | 2020-07-07 07:58:12 |
|  5 | LocatedAt | DELETE | 2020-07-07 07:58:12 |
|  6 | LocatedAt | UPDATE | 2020-07-07 07:58:12 |
+----+-----------+--------+---------------------+
6 rows in set (0.001 sec)

