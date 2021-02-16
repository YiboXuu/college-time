
select *
from Library
ORDER BY Name;

select*
from LocatedAt
ORDER BY ISBN;


SELECT Book.Title, SO1.TotalCopies, SO1.LibraryName
FROM Book, LocatedAt SO1, LocatedAt SO2
WHERE Book.ISBN = SO1.ISBN and
    SO1.ISBN = SO2.ISBN and
    SO1.LibraryName != SO2.LibraryName
ORDER BY Book.Title;

select LibraryName,count(ISBN) as NumberOfTitles
FROM LocatedAt
GROUP BY LibraryName
ORDER BY LibraryName;


SELECT ISBN, Book.Title, GROUP_CONCAT(Author.FirstName, ' ',Author.LastName) as Authors FROM Book NATURAL JOIN WrittenBy NATURAL JOIN Author WHERE Book.ISBN = '96-42103-11800';


SELECT Author.FisrtName FROM WrittenBy NATURAL JOIN Author WHERE Book.ISBN = '96-42103-11800';
SELECT ISBN, Book.Title, GROUP_CONCAT(Author.FirstName, ' ',Author.LastName) as Authors FROM (Book NATURAL JOIN WrittenBy NATURAL JOIN Author) WHERE Book.Title LIKE 'Blue is Your Friend' order by  Book.Title;



select count(MemberID) as totalCheckedOut FROM Book Natural Join BorrowedBy where ISBN = '96-42103-11800' and CheckinDate is null;


SELECT sum(TotalCopies) as totalCopies 
				FROM LocatedAt
				WHERE ISBN = '96-42103-11800';