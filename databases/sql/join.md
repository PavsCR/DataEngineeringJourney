# Types of JOIN in SQL

| **Join Type**     | **Description**                                                                                                                           | **Example**                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **INNER JOIN**    | Returns only rows that have matches in both tables.                                                                                       | `SELECT * FROM table1 INNER JOIN table2 ON table1.id = table2.table1_id;` |
| **LEFT JOIN**     | Returns all rows from the left table and the matching rows from the right table. Non-matching rows from the right are filled with `NULL`. | `SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.table1_id;`  |
| **FULL JOIN**     | Returns all rows from both tables. Non-matching rows from either table are filled with `NULL`.                                            | `SELECT * FROM table1 FULL JOIN table2 ON table1.id = table2.table1_id;`  |
| **CROSS JOIN**    | Returns the **Cartesian product** of the tables. All possible combinations of rows between the two tables.                                | `SELECT * FROM table1 CROSS JOIN table2;`                                 |
| **Implicit JOIN** | Combines tables without the `JOIN` keyword by separating tables with a comma. A `WHERE` condition makes it equivalent to an `INNER JOIN`. | `SELECT * FROM table1, table2 WHERE table1.id = table2.table1_id;`        |
