select *
FROM BorrowedBy;

SELECT LastName, FirstName, MemberID, Title, Library
FROM BorrowedBy O natural join Book B natural join Member M 
WHERE O.CheckinDate is null
order by MemberID;