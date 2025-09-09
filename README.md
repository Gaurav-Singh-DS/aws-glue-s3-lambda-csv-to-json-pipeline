# 🚀 AWS Glue + Lambda ETL Pipeline – S3 CSV to JSON Conversion

## ✅ Business Requirement
- **Input Bucket (S3):** Receives incoming CSV files  
- **Output Bucket (S3):** Stores converted JSON files  

**Goal:** Whenever a CSV file arrives in the input S3 bucket, it should be **automatically converted to JSON** and saved in the output S3 bucket.  

---

## ✅ Architecture Overview
```bash
S3 Input Bucket
↓
Lambda Trigger (on S3 PUT event)
↓
AWS Glue Job
↓
Transforms CSV → JSON
↓
S3 Output Bucket
```

---

## 🔹 Lambda Function

**Purpose:** Trigger the AWS Glue Job whenever a new file is uploaded to the input S3 bucket.  

```bash
| Step | Description                                                 |
| ---- | ----------------------------------------------------------- |
| 1    | A new CSV file is placed in Input S3 Bucket                 |
| 2    | S3 triggers Lambda function                                 |
| 3    | Lambda starts the Glue ETL Job                              |
| 4    | Glue reads CSV, applies transformation & data quality check |
| 5    | Output JSON written to Output S3 Bucket                     |
```
## 📂 Folder Structure
```bash
aws-glue-s3-csv-to-json-pipeline/
│── README.md                     # Documentation
│── lambda_function.py             # Lambda trigger code
│── glue_job.py                    # Glue PySpark script
│── LICENSE                        
```

