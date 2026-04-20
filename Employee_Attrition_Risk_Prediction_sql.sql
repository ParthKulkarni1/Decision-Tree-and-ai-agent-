SELECT 
    CASE 
        WHEN job_satisfaction = 'Low' AND overtime = 'Yes' THEN 'High Risk'
        WHEN job_satisfaction = 'Low' AND salary = 'Low' THEN 'High Risk'
        WHEN job_satisfaction = 'Low' THEN 'Medium Risk'
        WHEN years_at_company < 2 THEN 'Medium Risk'
        WHEN salary = 'High' THEN 'Low Risk'
        ELSE 'Medium Risk'
    END AS attrition_risk
FROM employees;