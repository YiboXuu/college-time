CREATE SQL SECURITY INVOKER VIEW BookLocatedAt AS
SELECT Book.Title, GROUP_CONCAT(Author.LastName, ' ',Author.FirstName) as Authors, LocatedAt.Shelf, LocatedAt.LibraryName
FROM (Book NATURAL JOIN WrittenBy NATURAL JOIN Author) NATURAL JOIN LocatedAt
Group by  Book.Title, LocatedAt.LibraryName;

select Title, Authors,Shelf,LibraryName
FROM BookLocatedAt
ORDER BY Title;