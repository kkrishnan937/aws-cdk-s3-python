# AWS CDK – Secure S3 Bucket (Python)

This repository demonstrates how to provision a **secure Amazon S3 bucket** using **AWS Cloud Development Kit (CDK)** with **Python**.  
The infrastructure is defined as code and deployed via **AWS CloudFormation**, following AWS security best practices.

This project was built as part of hands-on learning for the **AWS Solutions Architect Associate (SAA-C03)** certification and reflects real-world DevOps workflows.

---

## 🧰 Tech Stack
- AWS CDK (Python)
- Amazon S3
- AWS KMS
- AWS CloudFormation
- Python 3.x
- Node.js & npm

---

## 🏗️ Architecture Overview
- Infrastructure defined using **AWS CDK (Python)**
- CDK synthesizes into **CloudFormation templates**
- **Amazon S3 bucket** provisioned with:
  - Server-side encryption using **AWS KMS**
  - Managed lifecycle via CloudFormation
- Deployment and teardown handled through **CDK CLI**

---

## 📌 Prerequisites
Before deploying, ensure the following are installed and configured:

- Node.js (LTS recommended)
- AWS CDK CLI  
  ```bash
  npm install -g aws-cdk


## 📸 Screenshots

### CDK Deploy Output
![CDK Deploy Output](images/cdk-deploy.png)

### S3 Bucket in AWS Console
![S3 Bucket](images/s3-bucket.png)


## ✅ What I learned
- How to initialize and structure an AWS CDK project in Python.
- How `cdk synth`, `cdk bootstrap`, and `cdk deploy` work together with CloudFormation.
- How to provision an S3 bucket with KMS encryption using Infrastructure as Code.


## 🚀 How to Deploy
```bash
# Install dependencies
pip install -r requirements.txt

# Synthesize CloudFormation
cdk synth

# Bootstrap (first time only)
cdk bootstrap

# Deploy stack
cdk deploy

#Cleanup
cdk destroy


