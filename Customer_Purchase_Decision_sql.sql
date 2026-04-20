SELECT 
    CASE 
        WHEN previous_purchase = 'Yes' THEN 'Target Customer'
        WHEN income > 50000 THEN 'Target Customer'
        WHEN age < 25 THEN 'Not Target'
        ELSE 'Maybe Target'
    END AS customer_category
FROM customers;