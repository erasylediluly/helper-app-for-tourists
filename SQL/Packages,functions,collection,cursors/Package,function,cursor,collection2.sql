CREATE OR REPLACE PACKAGE coordinates IS
TYPE stroka_4 IS RECORD(
coord1 VARCHAR2(1000),
coord2 VARCHAR2(1000)
);
TYPE tablitsa_4 IS TABLE OF stroka_4;
FUNCTION getCoordinates RETURN tablitsa_4 PIPELINED;
END coordinates;
/
CREATE OR REPLACE PACKAGE BODY coordinates IS
FUNCTION getCoordinates RETURN tablitsa_4 PIPELINED IS
    result tablitsa_4;
    t stroka_4;
    i NUMBER:=1;
    temp VARCHAR2(100):='0';
BEGIN
    FOR r IN (SELECT place.ID,place.coordinates FROM distances INNER JOIN place ON place.ID = distances.placeID1)
    LOOP
        t.coord1 := r.coordinates;
        SELECT place.coordinates INTO temp FROM distances INNER JOIN place ON place.ID = distances.placeID2 WHERE distances.placeID1 = r.id AND distances.ID = i;
        t.coord2 := temp;
        PIPE ROW(t);
        i:=i+1;
    END LOOP;
    RETURN;
END;
END coordinates;
/
SELECT * FROM TABLE(coordinates.getCoordinates);