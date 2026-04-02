-- 1. Upsert (Добавить или Обновить)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- 2. Массовая вставка с валидацией
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names VARCHAR[], 
    p_phones VARCHAR[],
    INOUT failed_records TEXT[] DEFAULT ARRAY[]::TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_length(p_names, 1) LOOP
        -- Простая валидация: номер должен быть от 7 до 15 цифр
        IF p_phones[i] ~ '^[0-9\-\+]{7,15}$' THEN
            CALL upsert_contact(p_names[i], p_phones[i]);
        ELSE
            failed_records := array_append(failed_records, p_names[i] || ':' || p_phones[i]);
        END IF;
    END LOOP;
END;
$$;

-- 3. Удаление
CREATE OR REPLACE PROCEDURE delete_contact(p_search VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts 
    WHERE name = p_search OR phone = p_search;
END;
$$;