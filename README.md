````markdown
# Enterprise E-Commerce ETL Pipeline
### End-to-End Data Engineering Project using Apache Airflow, AWS, Databricks, PySpark, Athena, and Power BI

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Apache Airflow](https://img.shields.io/badge/Apache-Airflow-red)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20Glue%20%7C%20Athena-orange)
![Databricks](https://img.shields.io/badge/Databricks-PySpark-red)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Architecture](https://img.shields.io/badge/Architecture-Medallion%20Architecture-green)
![Data Model](https://img.shields.io/badge/Data%20Model-Star%20Schema-success)

---

# 📖 Project Overview

This project demonstrates an end-to-end Data Engineering pipeline that processes raw e-commerce transaction data using the **Medallion Architecture (Bronze/Raw → Silver/Processed → Gold/Presentation)**.

The pipeline ingests raw Excel files through a REST API, stores them in Amazon S3, cleans and standardizes the data using Databricks and PySpark, builds a dimensional data warehouse using a Star Schema, catalogs datasets with AWS Glue, queries them with Amazon Athena, and visualizes business insights in Power BI.

The entire workflow is orchestrated using **Apache Airflow**.

---

# 🏗️ Solution Architecture

```text
                                  REST API
                                      │
                                      ▼
                        Apache Airflow (Orchestration)
                                      │
                                      ▼
                    AWS S3 - Bronze Layer (Raw Files)
                                      │
                                      ▼
                    Databricks (PySpark - Silver Layer)

                     • Remove duplicate records
                     • Handle NULL values
                     • Standardize text casing
                     • Trim whitespace
                     • Validate dates
                     • Validate numeric values
                     • Standardize payment methods
                     • Data quality validation

                                      │
                                      ▼
                AWS S3 - Silver Layer (Processed Data)
                         │                       │
                         ▼                       ▼
               AWS Glue Crawler        AWS Glue Data Catalog
                         │                       │
                         └──────────────┬────────┘
                                        ▼
                                  Amazon Athena
                                        │
                                        ▼
                  Databricks (Gold Layer - Star Schema)

        ┌──────────────────────────────────────────────────┐
        │                 Dimension Tables                 │
        │                                                  │
        │  • dim_customer                                  │
        │  • dim_product                                   │
        │  • dim_store                                     │
        │  • dim_supplier                                  │
        │  • dim_sales_rep                                 │
        │  • dim_payment                                   │
        │  • dim_date                                      │
        └──────────────────────┬───────────────────────────┘
                               │
                               ▼
                           fact_sales
                               │
                               ▼
                        AWS S3 - Gold Layer
                         │                │
                         ▼                ▼
               AWS Glue Crawler    AWS Glue Data Catalog
                         │                │
                         └───────┬────────┘
                                 ▼
                            Amazon Athena
                                 │
                                 ▼
                             Power BI
```

---

# 🛠️ Technology Stack

| Category | Technology |
|-----------|------------|
| Workflow Orchestration | Apache Airflow |
| Programming | Python |
| Query Language | SQL |
| Big Data | PySpark, Spark SQL |
| Cloud Storage | Amazon S3 |
| Data Processing | Databricks |
| Metadata | AWS Glue Crawler |
| Catalog | AWS Glue Data Catalog |
| Query Engine | Amazon Athena |
| Integration | REST API |
| Data Modeling | Star Schema |
| Architecture | Medallion Architecture |
| Business Intelligence | Power BI |
| Source Data | Microsoft Excel |

---

# 📂 Project Workflow

## Bronze/Raw Layer

Raw Excel files are received through a REST API.

Apache Airflow orchestrates the ingestion process and stores the files in an Amazon S3 Bronze bucket without modifying the data.

The Bronze layer serves as the immutable source of truth.

---

## Silver/Processed Layer

Databricks processes the raw data using PySpark.

### Data Cleaning

- Remove duplicate rows
- Remove duplicate Order IDs
- Handle NULL values
- Replace blank strings
- Trim leading and trailing spaces
- Remove extra whitespace
- Standardize text casing
- Validate dates
- Validate numeric fields

The cleaned datasets are written back to Amazon S3 as the silver/processed layer.

---

## Metadata Management

After the Silver layer is created:

- AWS Glue Crawler scans the processed datasets.
- AWS Glue Data Catalog registers the metadata.
- Amazon Athena enables SQL queries against the Silver datasets.

---

## Gold Layer

The Gold layer contains business-ready datasets modeled using a Star Schema.

### Dimension Tables

#### dim_customer

- customer_key
- customer_id
- customer_name
- customer_type

#### dim_product

- product_key
- product_id
- product_name
- category
- sub_category
- brand

#### dim_store

- store_key
- store
- city
- state
- country

#### dim_supplier

- supplier_key
- supplier

#### dim_sales_rep

- sales_rep_key
- sales_rep_name

#### dim_payment

- payment_key
- payment_method

#### dim_date

- date_key
- order_date

---

## Fact Table

### fact_sales

The `fact_sales` table stores transactional measures and references all dimension tables using surrogate keys.

| Column | Description |
|----------|-------------|
| order_id | Business Order ID |
| customer_key | Foreign Key |
| product_key | Foreign Key |
| store_key | Foreign Key |
| supplier_key | Foreign Key |
| sales_rep_key | Foreign Key |
| payment_key | Foreign Key |
| date_key | Foreign Key |
| gross_sales | Quantity × Unit Price |
| discount_amount | Discount Applied |
| net_sales | Gross Sales − Discount |
| tax_amount | Calculated Tax |
| final_amount | Net Sales + Tax |
| order_age | Number of Days Since Order |
| delivery_sla | Delivery SLA Status |
| returned_flag | Indicates Returned Order |

---

## Gold Metadata

Once the Star Schema tables are generated:

- AWS Glue Crawler scans the Gold datasets.
- AWS Glue Data Catalog updates the metadata.
- Amazon Athena provides SQL access to the curated warehouse.

---

# ⭐ Star Schema

```text
                     dim_customer
                           │
                           │
dim_product ─────── fact_sales ─────── dim_store
                           │
                           │
                     dim_supplier
                           │
                           │
                    dim_sales_rep
                           │
                           │
                     dim_payment
                           │
                           │
                       dim_date
```

---

# 📊 Business Metrics

The pipeline calculates the following measures:

- Gross Sales
- Discount Amount
- Net Sales
- Tax Amount
- Final Amount
- Profit Margin
- Quantity Sold
- Order Age
- Delivery SLA
- Returned Orders

---

# 📈 Reporting

Power BI connects to Amazon Athena to visualize curated Gold datasets.

---

# 🚀 Skills Demonstrated

- End-to-End ETL Pipeline Development
- Apache Airflow Workflow Orchestration
- REST API Integration
- Amazon S3 Data Lake
- Medallion Architecture
- PySpark Data Processing
- Spark SQL
- SQL Development
- Data Cleansing
- Data Validation
- Data Standardization
- Star Schema Modeling
- Fact and Dimension Table Design
- AWS Glue Crawler
- AWS Glue Data Catalog
- Amazon Athena
- Power BI Dashboard Development


---

# 👤 Author

**Jasmin In-naka**

This project was built as part of my Data Engineering portfolio to demonstrate practical experience designing and implementing scalable ETL pipelines, cloud-based data processing, dimensional modeling, and business intelligence solutions using modern data engineering technologies.
````
