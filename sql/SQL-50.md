# SQL 50

1. ## 1757. Recyclable and Low Fat Products

   ```sql
   SELECT product_id FROM Products
   WHERE low_fats = 'Y' and recyclable = 'Y';
   ```

2. ## 584. Find Customer Referee

   ```sql
   SELECT name FROM Customer
   WHERE referee_id is null or referee_id != 2;
   ```

3. ## 595. Big Countries

   ```sql
   SELECT name, population, area FROM World
   WHERE area >= 3000000 or population >= 25000000;
   ```

4. ## 1148. Article Views I

   ```sql
   SELECT DISTINCT author_id as id FROM Views
   WHERE author_id = viewer_id
   ORDER BY author_id ASC;
   ```

5. ## 1683. Invalid Tweets

   ```sql
   SELECT tweet_id FROM Tweets
   WHERE LENGTH(content) > 15;
   ```

6. ## 1378. Replace Employee ID With The Unique Identifier

   ```sql
   SELECT u.unique_id, e.name FROM Employees e
   LEFT JOIN EmployeeUNI u ON u.id = e.id;
   ```

7. ## 1068. Product Sales Analysis I

   ```sql
   SELECT p.product_name, s.year, s.price FROM Product p
   RIGHT JOIN Sales s ON s.product_id = p.product_id;
   ```

8. ## 1581. Customer Who Visited but Did Not Make Any Transactions

   ```sql
   SELECT v.customer_id,
      COUNT(*) AS count_no_trans
   FROM Visits v
   LEFT JOIN Transactions t ON v.visit_id = t.visit_id
   WHERE t.visit_id IS NULL
   GROUP BY v.customer_id;
   ```

9. ## 197. Rising Temperature

   ```sql
   SELECT w2.id FROM Weather w1
   RIGHT JOIN Weather w2 ON TIMESTAMPDIFF(DAY, w1.recordDate, w2.recordDate) = 1
   WHERE w1.temperature < w2.temperature;
   ```

10. ## 1661. Average Time of Process per Machine

    ```sql
    SELECT
    a1.machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) as processing_time
    FROM Activity a1
    INNER JOIN Activity a2
    ON a1.machine_id = a2.machine_id
    and a1.process_id = a2.process_id
    and a1.activity_type = 'start'
    and a2.activity_type = 'end'
    GROUP BY a1.machine_id;
    ```

11. ## 577. Employee Bonus

    ```sql
    SELECT e.name, b.bonus FROM Employee e
    LEFT JOIN Bonus b ON e.empId = b.empId
    WHERE b.bonus < 1000 or b.bonus is NULL;
    ```
