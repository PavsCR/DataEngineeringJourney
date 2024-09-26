# SQL Common Queries Reference

## Queries with conditions

```sql
SELECT column, another_column, …
FROM mytable
WHERE condition
    AND/OR another_condition
    AND/OR …;
```

## Table of conditions

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
| \_           | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE)                    | col*name **LIKE** "AN*" (matches "AND", but not "AN")                  |
| IN (…)       | String exists in a list                                                                               | col_name **IN** ("A", "B", "C")                                        |
| NOT IN (…)   | String does not exist in a list                                                                       | col_name **NOT IN** ("D", "E", "F")                                    |

## WHERE

```sql
SELECT * FROM table_name WHERE condition; -- Filter records
```

## JOIN

```sql
SELECT columns FROM table1 INNER JOIN table2 ON table1.common_column = table2.common_column; -- Inner Join

SELECT columns FROM table1 LEFT JOIN table2 ON table1.common_column = table2.common_column; -- Left Join
```

## GROUP BY

```sql
SELECT column1, COUNT(*) FROM table_name GROUP BY column1; -- Group records
```

## ORDER BY

```sql
SELECT _ FROM table_name ORDER BY column1 ASC; -- Sort records ascending

SELECT _ FROM table_name ORDER BY column1 DESC; -- Sort records descending
```

### Where to practice?

[SQLBolt](https://sqlbolt.com/)
