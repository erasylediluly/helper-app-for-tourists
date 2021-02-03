CREATE OR REPLACE TRIGGER routes_before_insert
BEFORE INSERT ON routes
FOR EACH ROW
DECLARE 
    user_xcep EXCEPTION;
   PRAGMA EXCEPTION_INIT( user_xcep, -20001 );
BEGIN
  IF(:new.consumption <= 0 )
  THEN
    raise user_xcep;
  END IF;
END;
/
BEGIN
INSERT INTO routes VALUES('some places',1,-1,1,'fuel');
INSERT INTO routes VALUES('some places',1,2,1,'fuel');
EXCEPTION
WHEN others THEN
    ROLLBACK;
END;
/
DELETE FROM routes;
commit;