# 📊 Decision Tree Models – README


## 🔹 Overview

This project demonstrates the creation of **rule-based (deterministic) decision trees** for solving real-world business problems. Unlike machine learning models, these decision trees follow **fixed logic (if–else conditions)** and always produce the same output for the same input.

Two use cases are covered:

1. **Employee Attrition Risk Prediction**
2. **Customer Purchase Decision Classification**

---

## 🔹 1. Employee Attrition Risk

### 📌 Objective

To classify employees based on the likelihood of leaving the company.

### 📥 Input Features

* Job Satisfaction (High / Medium / Low)
* Salary (High / Low)
* Years at Company
* Overtime (Yes / No)

### ⚙️ Logic

* Employees with **low satisfaction and overtime** are at **high risk**
* Low satisfaction + low salary → **high risk**
* New employees (<2 years) → **medium risk**
* High salary + stable tenure → **low risk**

### 📤 Output

* High Risk
* Medium Risk
* Low Risk

---

## 🔹 2. Customer Purchase Decision

### 📌 Objective

To identify whether a customer should be targeted for marketing.

### 📥 Input Features

* Previous Purchase (Yes / No)
* Income Level
* Age

### ⚙️ Logic

* Customers with **previous purchases** → Target
* High income → Target
* Low income + young age → Not Target
* Others → Maybe Target

### 📤 Output

* Target Customer
* Maybe Target
* Not Target

---

## 🔹 Implementation

### 🐍 Python

* Implemented using **nested if–else conditions**
* Functions simulate decision tree logic

### 🗄️ SQL

* Implemented using **CASE WHEN statements**
* Suitable for database-level decision making

---

## 🔹 Key Features

* Deterministic (no randomness or learning)
* Easy to interpret and explain
* Business-focused logic
* Lightweight and fast execution

