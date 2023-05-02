-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar

CREATE TABLE student
(student_id serial, first_name varchar(50), last_name varchar(50), birthday date, phone varchar)

-- 2. Добавить в таблицу student колонку middle_name varchar

ALTER TABLE student ADD COLUMN middle_name varchar(50)

-- 3. Удалить колонку middle_name

ALTER TABLE student DROP COLUMN middle_name

-- 4. Переименовать колонку birthday в birth_date

ALTER TABLE student RENAME COLUMN birthday TO birth_date

-- 5. Изменить тип данных колонки phone на varchar(32)

ALTER TABLE student DROP COLUMN middle_name

-- 6. Вставить три любых записи с автогенерацией идентификатора

INSERT INTO student (first_name, last_name, birth_date, phone) VALUES ('Александр', 'Веселов', '1990-01-22', '123456789');
INSERT INTO student (first_name, last_name, birth_date, phone) VALUES ('Василий', 'Пупкин', '1968-11-22', '12345678958');
INSERT INTO student (first_name, last_name, birth_date, phone) VALUES ('Иван', 'Петров', '1988-10-27', '12345678958')

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние

TRUNCATE TABLE student RESTART IDENTITY
