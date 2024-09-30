# SQL Common Queries Reference

## Queries with conditions

```sql
SELECT column, another_column, …
FROM mytable
WHERE condition
    AND/OR another_condition
    AND/OR …;
```

### Numeric Data

| **Operator**        | **Condition**                                        | **SQL Example**                       |
| ------------------- | ---------------------------------------------------- | ------------------------------------- |
| =, !=, <, <=, >, >= | Standard numerical operators                         | col_name **!=** 4                     |
| BETWEEN … AND …     | Number is within range of two values (inclusive)     | col_name **BETWEEN** 1.5 **AND** 10.5 |
| NOT BETWEEN … AND … | Number is not within range of two values (inclusive) | col_name **NOT BETWEEN** 1 **AND** 10 |
| IN (…)              | Number exists in a list                              | col_name **IN** (2, 4, 6)             |
| NOT IN (…)          | Number does not exist in a list                      | col_name **NOT IN** (1, 3, 5)         |

### Text Data

| **Operator** | **Condition**                                                                                         | **SQL Example**                                                        |
| ------------ | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| =            | Case sensitive exact string comparison                                                                | col_name **=** "abc"                                                   |
| !=           | Case sensitive exact string inequality comparison                                                     | col_name **!=** "abc"                                                  |
| LIKE         | Case insensitive exact string comparison                                                              | col_name **LIKE** "ABC"                                                |
| NOT LIKE     | Case insensitive exact string inequality comparison                                                   | col_name **NOT LIKE** "ABCD"                                           |
| %            | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | col_name **LIKE** "%AT%" (matches "AT", "ATTIC", "CAT" or even "BATS") |
| \_           | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE)                    | col_name **LIKE** "AN\_" (matches "AND", but not "AN")                 |
| IN (…)       | String exists in a list                                                                               | col_name **IN** ("A", "B", "C")                                        |
| NOT IN (…)   | String does not exist in a list                                                                       | col_name **NOT IN** ("D", "E", "F")                                    |

### Filtering and Sorting Query Results

| **Operator**  | **Function**                                                | **SQL Example**                                                                                                                                                                                                                                |
| ------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| DISTINCT      | Discard rows that have a duplicate column value             | SELECT **DISTINCT** column, another_column, … FROM table_name;                                                                                                                                                                                 |
| GROUP BY      | GROUP BY                                                    | Groups rows that have the same values in specified columns, typically used with aggregate functions (such as `SUM()`, `COUNT()`, `AVG()`, etc.) to perform calculations on each group, allowing for summarized results based on shared values. | SELECT column, **COUNT**(\*) FROM table_name **GROUP BY** column; |
| ORDER BY      | Sort the result set by one or more columns                  | SELECT column1, column2 FROM table_name **ORDER BY** column1 **ASC**;                                                                                                                                                                          |
| HAVING        | Filter groups based on a condition (used with **GROUP BY**) | SELECT column, SUM(amount) AS total_amount FROM table_name GROUP BY column **HAVING** SUM(amount) > 1000;                                                                                                                                      |
| LIMIT(MySQL)  | Limit the number of rows returned                           | SELECT \* FROM table_name **LIMIT** 10;                                                                                                                                                                                                        |
| OFFSET(MySQL) | Skip a specified number of rows before returning results    | SELECT \* FROM table_name LIMIT 10 **OFFSET** 5 ;                                                                                                                                                                                              |

## EXIST

```sql
SELECT c.CustomerName
FROM Customers c
WHERE EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.CustomerID = c.CustomerID
);
```

### Where to practice?

[SQLBolt](https://sqlbolt.com/)
