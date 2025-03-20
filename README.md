# AWS Lambda Function for Scheduling EC2 Start and Stop

## Overview
This project provides a solution to schedule EC2 instances to start and stop automatically using AWS Lambda and Amazon EventBridge.

## Prerequisites
Before deploying this solution, ensure you have the following:
- An AWS account
- EC2 instances running in AWS
- IAM role with necessary permissions for Lambda to manage EC2 instances
- AWS CLI or AWS Console access

## Setup Instructions

### Step 1: Create an IAM Role for Lambda (Role Name: `EC2SchedulerRole`)
1. Go to the **AWS IAM Console**.
2. Create a new role with **AWS Lambda** as the trusted entity.
3. Attach the following policy to the role:
   - **AmazonEC2FullAccess**
4. Attach the **AWSLambdaBasicExecutionRole** policy.
5. Save the role and note the **ARN**.

### Step 2: Create Two Lambda Functions
#### Lambda Function 1: EC2 Start
1. Go to the **AWS Lambda Console**.
2. Click **Create function** > Choose **Author from scratch**.
3. Set the function name (e.g., `EC2StartFunction`).
4. Select **Python 3.x** as the runtime.
5. Assign the IAM role created in Step 1.
6. Click **Create Function**.
7. Upload the code file `ec2_start.py` to the function.

#### Lambda Function 2: EC2 Stop
1. Repeat steps 1-6 above, but name the function `EC2StopFunction`.
2. Upload the code file `ec2_stop.py` to the function.

### Step 3: Create Amazon EventBridge Schedules
#### Schedule 1: EC2 Start
1. Go to the **Amazon EventBridge Console**.
2. Click **Create Rule**.
3. Set the rule name (e.g., `EC2StartSchedule`).
4. Select **Schedule** and define the cron expression (e.g., `cron(0 9 * * ? *)` for 9 AM UTC daily).
5. Set the target to your **EC2StartFunction** Lambda function.
6. Save the rule.

#### Schedule 2: EC2 Stop
1. Repeat steps 1-5 above, but name the rule `EC2StopSchedule`.
2. Use a different cron expression (e.g., `cron(0 18 * * ? *)` for 6 PM UTC daily).
3. Set the target to your **EC2StopFunction** Lambda function.
4. Save the rule.

### Step 4: Test the Lambda Functions
1. Manually trigger the **EC2StartFunction** in the AWS Lambda console and verify that your EC2 instance starts.
2. Manually trigger the **EC2StopFunction** in the AWS Lambda console and verify that your EC2 instance stops.
3. Check the **Amazon CloudWatch Logs** for logs.

## Conclusion
This setup automates EC2 instance scheduling using AWS Lambda and EventBridge. You can modify the cron expressions and instance IDs to fit your requirements.

## References
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon EventBridge Documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
