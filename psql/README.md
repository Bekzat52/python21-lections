# Slash commands
*`\c` - показывает в какой БД мы находимся и через какого юзера зашли
*`\c name_of_db` - переклюяаемся к этой БД
*`\l` - показывает все БД
*`\dt` - показывает все таблицы в БД, к которой мы подключились
*`\du` - показывает всех юзеров
*`\q` - выход

# Создание БД и таблиц
```sql
CREATE DATABASE name_of_db;
-- создает базу данных
```

```sql
CREATE TABLE name_of_table(
    name_of_column1 data_type constraint,
    name_of_column2 data_type constraint,
    ...
);
-- создает таблицу
```
# Заполнение таблиц
```sql
INSERT INTO name_of_table(name_of_column1, name_of_column2)
VALUES(val_for_column1, val_for_column2);
-- добавляет запись в таблицу
```

# Вывод данных из таблицы
```sql
SELECT * FROM name_of_table;
-- достает все поля и все записи из таблицы
```

```sql
SELECT name_of_column1, name_of_column2 FROM name_of_table;
--достает только указанные столбцы из таблицы со всеми записями
```

```sql
SELECT * FROM name_of_table WHERE name_of_column2
= 'hello';
-- достает все записи из таблицы у которых name_of_column2 со значением 'hello'
```

# Связи 
## pk fk
> primary key(pk) - первичный ключ
> это ограничение, которое мы указываем на те поля, которые должны быть уникальными, чтобы потом их использовать в связях (создает btree)

> foreign key(fk) - внешний ключ
> это ограничение, которое мы указываем на те поля, которые будут ссылаться 


```sql

CREATE TABLE author(
    id serial primary key,
    first_name varchar(50)
    last_name varchar(50)
);

CREATE TABLE book (
    id serial,
    title varchar(100),
    published year ,
    author_id int,
    CONSTRAINT fk_author_book
    FOREIGN KEY(author_id)
    REFERENCES author (id)
);
```

## Виды связей (теория)
> One to one - (один к одному)
Например:

* Один флаг - одна страна
* Один человек - одно сердце
* Один автор - одна автобиография

> One to many - (один ко многим)
Например:

* Один Оомат - много поздравлений
* Одна страна - много городов
* Один пост - много комментариев
* Один диктатор - много подчененных

> Many to many - (многие ко многим)
Например:

* У студента много менторов - и у ментора много студентов
* У пользователя много соц.сетей и у одной соц.сети много пользователей

## Виды связей (практика)
### One to one 
```sql 
CREATE TABLE flag (
    id serial primary key,
    photo text
);

CREATE TABLE country (
    id serial primary key,
    title varchar(50),
    flag_id int unique,
    CONSTRAINT fk_country_flag
    FOREIGN KEY (flag_id)
    REFERENCES flag(id)
);
```

### One to many
```sql
CREATE TABLE post(
    id serial primary key,
    title varchar (100),
    body text
);

CREATE TABLE comment (
    id serial primary key,
    body text,
    created_at datetime,
    post_id int,

    CONSTRAINT fk_post_comment
    FOREIGN KEY post_id
    REFERENCES post(id)
);
```

### Many to many
```sql
CREATE TABLE student (
    id serial primary key,
    first_name varchar(50),
    age int
);

CREATE TABLE mentor (
    id serial primary key,
    first_name varchar(50),
    age int
);

CREATE TABLE student_mentor(
    student_id int,
    mentor_id int,

    CONSTRAINT fk_student
    FOREIGN KEY (student_id)
    REFERENCES student(id),

    CONSTRAINT fk_mentor
    FOREIGN KEY (mentor_id)
    REFERENCES mentor(id)
);
```
## Join (теория)
> JOIN - инструкция, которая позволяет в запросах SELECT брать данные из нескольких связанных таблиц

> INNER JOIN (JOIN) - когда достаются только те записи, у которых есть полная связь

> FULL JOIN - когда достаются абсолютно все записи со всех таблиц (не важно есть ли связь у записи)

> LEFT JOIN - когда достаются все записи с "левой" таблицы и также записи с полной связью

> RIGHT JOIN - когда достаются все записи с "правой" таблицы и также записи с полной связью

## JOIN (практика)
### one to one 

```sql
SELECT country.title, flag.photo
FROM country 
JOIN flag
ON country.flag_id = flag.id;
```

### one to many
```sql
SELECT post.title, comment.body, comment.created_at 
FROM post
JOIN comment
ON post.id = comment.post_id;
```

### many to many
```sql
SELECT mentor.first_name as mentor_name, student.first_name as student_name
FROM mentor
JOIN student_mentor
ON mentor.id = student_mentor.mentor_id

JOIN student
ON student.id = student_mentor.student_id;
```

# Import / Export данных
write from file to db
```bash
psql db_name < file.sql
```

write from db to file
```bash
pg_dump db_name > file.sql
```