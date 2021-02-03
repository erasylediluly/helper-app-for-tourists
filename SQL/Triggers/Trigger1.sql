CREATE OR REPLACE TRIGGER routes_after_delete
AFTER DELETE ON place
DECLARE
v_id VARCHAR2(50);
BEGIN  
    FOR I IN (SELECT places FROM routes)
    LOOP
        FOR J IN(SELECT regexp_substr(I.places,'[^$]+', 1, level) as p from dual connect by regexp_substr(I.places, '[^$]+', 1, level) is not null)
        LOOP
        SELECT ID INTO v_id FROM place WHERE name = J.p;
        IF(v_id IS NOT NULL) THEN
            DELETE FROM routes WHERE places = I.places;
        END IF;
        END LOOP;
    END LOOP;
END;
/
DELETE FROM place WHERE id = 8;
SELECT places FROM routes;
COMMIT;