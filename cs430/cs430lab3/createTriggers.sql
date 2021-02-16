DELIMITER $$

create trigger add_author after insert on Author
    for each row begin
    insert into Audit values (null,'Author', 'INSERT', NOW());
end;
$$
DELIMITER ;


DELIMITER $$

create trigger add_Book_from_library after insert on LocatedAt
    for each row begin
    insert into Audit values (null,'LocatedAt', 'INSERT', NOW());
end;
$$
DELIMITER ;


DELIMITER $$

create trigger delete_Book_from_library after delete on LocatedAt
    for each row begin
    insert into Audit values (null,'LocatedAt', 'DELETE', NOW());
end;
$$
DELIMITER ;

DELIMITER $$

create trigger mod_num_of_copies after update on LocatedAt
    for each row begin

    if NEW.TotalCopies <> OLD.TotalCopies
    THEN
        insert into Audit values (null,'LocatedAt', 'UPDATE', NOW());
    END IF;
end;
$$
DELIMITER ;