# Customer-Shopping-Behaviour-Analysis

## Project Overview
This project analyzes customer shopping behavior by performing data cleaning, transformation, SQL analysis, and visualization using Power BI. The workflow involves:

1. Reading raw CSV data.
2. Cleaning and transforming the data using Python (pandas).
3. Uploading the cleaned data to a MySQL database.
4. Running SQL queries to extract insights.
5. Creating interactive dashboards in Power BI for business recommendations.

---

## Data Source
- File: `customer_shopping_behavior.csv`
- Contains customer details, purchase behavior, review ratings, age, category, frequency of purchase, discounts, and promo code usage.

---

## Workflow

### 1️⃣ Data Cleaning & Transformation (Python)
- Libraries used: `pandas`, `pymysql`, `sqlalchemy`
- Steps:
  - Read CSV file.
  - Check for missing values.
  - Fill missing `Review Rating` values using median per category.
  - Standardize column names (lowercase, replace spaces with underscores).
  - Rename columns for clarity (e.g., `purchase_amount_(usd)` → `purchase_amount`).
  - Create new columns:
    - `age_group` based on age quartiles: Young Adult, Adult, Middle-age, Senior.
    - `purchase_frequency_days` mapped from `frequency_of_purchases`.
  - Drop redundant columns (`promo_code_used`).

```python
# Example snippet
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median()))
df['age_group'] = pd.qcut(df['age'], 4, labels=['Young Adult','Adult','Middle-age','Senior'])
```

---

## 2️⃣ Upload to MySQL

 - Connect to MySQL using SQLAlchemy.
 - Create database table customer.
 - Upload cleaned DataFrame.

```python
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
df.to_sql('customer', con=engine, if_exists='replace', index=False)
```

---

## 3️⃣ SQL Analysis

• Sample queries for customer behavior insights:

• Total revenue by gender.

• Customers using discounts but spending above average.

• Customers with multiple purchases.

• Products never sold.

• Average purchase amount per customer.

---

## 4️⃣ Power BI Dashboard

Connect Power BI to MySQL database.

Visualizations created:

• Total revenue and sales trends.

• Customer segmentation by age and purchase frequency.

• Discount and promo code usage analysis.

• Category-wise purchase insights.

• Dashboard supports business recommendations based on customer behavior.

---

## Business Recommendations

• Focus on High‑Value Customer Segments
Young Adults and Middle‑Age groups generate the highest spending. Introduce age‑specific product bundles, targeted email campaigns, and personalized recommendations.

• Strengthen Category‑Wise Strategy
Clothing and Accessories drive most revenue. Increase inventory depth, highlight these categories in seasonal campaigns, and negotiate better supplier terms to increase margin.

• Reduce Unnecessary Discount Usage
Many discount users still spend above the average amount. Shift to conditional discounts (e.g., spend threshold, loyalty-based coupons) instead of blanket offers.

• Improve Subscription Program Value
Subscribers show higher average spend. Promote subscription benefits through onboarding journeys, exclusive deals, and free shipping to increase sign‑ups.

• Improve Shipping Experience
Express shipping customers spend slightly more. Offer dynamic shipping upgrades based on cart value or membership status.

• Enhance Customer Loyalty Tracking
Returning and loyal customers provide steady revenue. Introduce tiers (Silver/Gold/Platinum), reward points, and anniversary discounts.

• Optimize Underperforming Products
Identify items with low purchase frequency and high discount dependence. Apply product redesign, price adjustments, or phase‑out strategy.

• Use Review Rating Insights to Improve Quality
Items with lower average ratings should be flagged for quality checks. Follow up with dissatisfied customers to improve retention.

---

## Tools & Libraries

• Python: pandas, pymysql, sqlalchemy

• Database: MySQL

• Visualization: Power BI

