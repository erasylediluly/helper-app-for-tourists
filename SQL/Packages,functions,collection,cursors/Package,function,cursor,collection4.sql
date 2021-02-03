CREATE OR REPLACE PACKAGE filterPlaces IS
TYPE stroka IS RECORD(
i NUMBER,
name VARCHAR2(200));
TYPE tablitsa IS TABLE OF stroka;
FUNCTION filterPlacesByTypeRegionName(p_type VARCHAR2,p_region_name VARCHAR2,p_name VARCHAR2) RETURN tablitsa PIPELINED;
END filterPlaces;
/
CREATE OR REPLACE PACKAGE BODY filterPlaces IS
FUNCTION filterPlacesByTypeRegionName(p_type VARCHAR2,p_region_name VARCHAR2,p_name VARCHAR2) RETURN tablitsa PIPELINED IS
    result tablitsa;
    t stroka;
BEGIN
    FOR r IN (SELECT place.id,place.name FROM place INNER JOIN region ON region.ID = place.regionid 
    WHERE lower(place.name) LIKE lower('%'||p_name||'%')
    AND lower(place.type) LIKE lower('%'||p_type||'%')
    AND lower(region.name) LIKE lower('%'||p_region_name||'%'))
    LOOP
        t.i := r.id;
        t.name := r.name;
        PIPE ROW(t);  
    END LOOP;
    RETURN;
END;
END filterPlaces;
/
SELECT i,Name FROM table(filterPlaces.filterPlacesByTypeRegionName('Активный отдых','','а'));
