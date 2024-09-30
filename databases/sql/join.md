# Types of JOIN in SQL

| **Join Type**  | **Description**                                                                                                                           | **Example**                                                                                   |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **INNER JOIN** | Returns only rows that have matches in both tables.                                                                                       | `sql<br>SELECT *<br>FROM table1<br>INNER JOIN table2<br>ON table1.id = table2.table1_id;<br>` |
| **LEFT JOIN**  | Returns all rows from the left table and the matching rows from the right table. Non-matching rows from the right are filled with `NULL`. | `sql<br>SELECT *<br>FROM table1<br>LEFT JOIN table2<br>ON table1.id = table2.table1_id;<br>`  |
| **FULL JOIN**  | Returns all rows from both tables. Non-matching rows from either table are filled with `NULL`.                                            | `sql<br>SELECT *<br>FROM table1<br>FULL JOIN table2<br>ON table1.id = table2.table1_id;<br>`  |
| **CROSS JOIN** | Returns the **Cartesian product** of the tables. All possible combinations of rows between the two tables.                                | `sql<br>SELECT *<br>FROM table1<br>CROSS JOIN table2;<br>`                                    |
