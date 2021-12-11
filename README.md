# trakr

### Database Configuration

```
CREATE TABLE 2021_expense (
    expense_date date not null,
    transaction_id binary(16) primary key,
    entity varchar(255),
    category varchar(255) not null,
    expense int not null
);

CREATE TABLE income_category (
    category_id int not null primary key,
    category varchar(255)
);

CREATE TABLE expense_category (
    category_id int not null primary key,
    category varchar(255)
);

create table trakr_config (
	year int not null,
	year_expense_table varchar(255),
	year_income_table varchar(255),
	status varchar(255)
);

CREATE USER 'trakr'@'localhost' IDENTIFIED BY '';

grant create, alter, insert, update, delete, select, references, reload on *.* 
to 'trakr'@l'ocalhost' with grant option;

```