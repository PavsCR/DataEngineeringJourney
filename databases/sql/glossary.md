# Glossary

## SQL

Structured Query Language

## Table

A collection of related data entries in rows and columns.

| **ID** | **Name** | **Age** |
| ------ | -------- | ------- |
| 1      | Alice    | 30      |
| 2      | Bob      | 25      |
| 3      | Charlie  | 28      |

## Column

A vertical section in a table representing a specific attribute.

| **Name** |
| -------- |
| Alice    |
| Bob      |
| Charlie  |

## Row

A horizontal entry in a table containing data for a single record.

| **ID** | **Name** | **Age** |
| ------ | -------- | ------- |
| 1      | Alice    | 30      |

## Statement

An SQL command that performs an action in the database.
**INSERT, DROP, CREATE, etc.**

## Stored Procedure

A precompiled set of SQL statements executed as a single unit.

```sql
CREATE PROCEDURE AddUser (@Name VARCHAR(100), @Age INT)
AS
BEGIN
    INSERT INTO Users (Name, Age) VALUES (@Name, @Age);
END;
```

## Query

A request for data from a database, usually using **SELECT**.

```sql
SELECT * FROM Users WHERE Age > 25;
```

## View

A virtual table based on a SQL query result.

```sql
CREATE VIEW AdultUsers AS
SELECT * FROM Users WHERE Age >= 18;
```

## Constraint

A rule that restricts the data that can be entered into a table, ensuring data integrity. Common types of constraints include:

- **NOT NULL**: Ensures that a column cannot have a NULL value.
- **UNIQUE**: Ensures that all values in a column are different.
- **PRIMARY KEY**: Uniquely identifies each record in a table and cannot contain NULL values.
- **FOREIGN KEY**: Ensures referential integrity between two tables.
- **CHECK**: Ensures that all values in a column satisfy a specific condition.

```sql
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT CHECK (Age >= 18),
    Email VARCHAR(100) UNIQUE
);
```

## Primary Key

A unique identifier for a record in a table.

```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    UserID INT,
    Product VARCHAR(100),
);
```

## Foreign Key

A column that links one table to another, ensuring referential integrity.

```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    UserID INT,
    Product VARCHAR(100),
    CONSTRAINT fk_user
        FOREIGN KEY (UserID)
        REFERENCES Users(UserID)
);
```

## Index

A structure that improves data retrieval speed.

```sql
CREATE INDEX idx_name ON TableName (ColumnName);
```
