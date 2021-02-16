
SELECT * FROM Book
ORDER BY ISBN;

SELECT * FROM Member
ORDER BY LastName, FirstName;

SELECT * FROM Author
ORDER BY LastName, FirstName;

SELECT * from Publisher
ORDER BY Pub_name;

SELECT * from Phone
ORDER BY PNumber;

SELECT * from AuthorPhone
ORDER BY AuthorID;

SELECT * FROM PublisherPhone
ORDER BY PubID;

Select * FROM BorrowedBy
ORDER BY ISBN;

SELECT * FROM WrittenBy
ORDER BY ISBN;

SELECT FirstName, LastName
FROM Member
WHERE LastName LIKE 'B%'
ORDER BY LastName;

SELECT *
FROM Book NATURAL JOIN Publisher
WHERE Pub_name = 'Coyote Publishing'
ORDER BY Title;

SELECT FirstName, LastName, MemberID, Title
FROM Member NATURAL JOIN BorrowedBy NATURAL JOIN Book
Where CheckinDate is NULL
Order BY MemberID;

SELECT FirstName, LastName, AuthorID, Title
FROM Author NATURAL JOIN WrittenBy NATURAL JOIN Book
Order BY AuthorID;

SELECT FirstName, LastName, P1.PNumber
FROM Author, AuthorPhone P1, AuthorPhone P2
WHERE Author.AuthorID = P1.AuthorID and
    P1.PNumber = P2.PNumber and
    P1.AuthorID != P2.AuthorID
ORDER BY P1.PNumber;