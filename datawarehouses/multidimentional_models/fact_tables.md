# Foreign Keys and Composite Key in Fact Tables in a Data Warehouse

In a **data warehouse**, **fact tables** store quantitative data and typically have **foreign keys** that connect to the **primary keys** of **dimension tables**. These foreign keys combine to form a **composite key** that uniquely identifies each transaction or event.

## Example

### Fact Table: Sales

| date_id  | product_id | customer_id | amount |
| -------- | ---------- | ----------- | ------ |
| 20240101 | 101        | 1001        | 150    |
| 20240102 | 102        | 1002        | 200    |
| 20240103 | 101        | 1001        | 100    |

- **Composite Key**: `(date_id, product_id, customer_id)`

### Dimension Table: Products

| product_id | product_name | category |
| ---------- | ------------ | -------- |
| 101        | Widget A     | Widgets  |
| 102        | Gadget A     | Gadgets  |

### Dimension Table: Customers

| customer_id | customer_name | customer_segment |
| ----------- | ------------- | ---------------- |
| 1001        | Alice         | Retail           |
| 1002        | Bob           | Wholesale        |

### Dimension Table: Time

| date_id  | date       | month   | year |
| -------- | ---------- | ------- | ---- |
| 20240101 | 2024-01-01 | January | 2024 |
| 20240102 | 2024-01-02 | January | 2024 |
| 20240103 | 2024-01-03 | January | 2024 |

## Relationship Between Tables

- `date_id` in **Sales** connects to `date_id` in **Time**.
- `product_id` in **Sales** connects to `product_id` in **Products**.
- `customer_id` in **Sales** connects to `customer_id` in **Customers**.

### Benefits

1. **Efficient Analysis**: Facilitates complex queries.
2. **Descriptive Context**: Numeric data is accompanied by meaningful descriptions.
3. **Flexibility**: Allows for the addition of new dimensions or facts without affecting the existing design.
