CREATE OR REPLACE PACKAGE comboBoxItems IS
TYPE stroka_2 IS RECORD(
name VARCHAR2(50)
);
TYPE tablitsa_2 IS TABLE OF stroka_2;
FUNCTION getFuel RETURN tablitsa_2 PIPELINED;
FUNCTION getCities RETURN tablitsa_2 PIPELINED;
END comboBoxItems;
/
CREATE OR REPLACE PACKAGE BODY comboBoxItems IS
FUNCTION getFuel RETURN tablitsa_2 PIPELINED IS
    result tablitsa_2;
    t stroka_2;
BEGIN
    FOR r IN (SELECT id,name FROM fuel)
    LOOP
        t.name := r.name;
        PIPE ROW(t);
    END LOOP;
    RETURN;
END;
FUNCTION getCities RETURN tablitsa_2 PIPELINED IS
    result tablitsa_2;
    t stroka_2;
BEGIN
    FOR r IN (SELECT name FROM place WHERE type='Город')
    LOOP
        t.name := r.name;
        PIPE ROW(t);
    END LOOP;
    RETURN;
END;
END comboBoxItems;
/
SELECT name FROM table(comboBoxItems.getFuel());
SELECT name FROM table(comboBoxItems.getCities());
