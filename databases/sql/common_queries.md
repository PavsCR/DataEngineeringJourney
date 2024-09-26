# SQL Common Queries Reference

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
