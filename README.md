# serverlessSlacktoEC2

Slack(1) <-> Amazon API Gateway(2) <-> AWS Lambda(3) <-> AWS Lambda(4) <-> Amazon EC2(5)
1. you enter a slash command(/hoge huga), and it will be sent to the API Gateway.
2. it will be sent to the Lambda.
3. The back Lambda is called asynchronously and it returns 200 status code.
4. This Lambda gets the EC2 instance lists(/hoge list command) or start/stop the EC2 instances(/hoge start i-xxxx or /hoge stop i-xxxx).
5. It is called the EC2 instance start or stop command.

This repo works on AWS Lambda(3).

## usage

```
$ cd <clone directory>
$ pip install boto3 -t .
$ zip -r lambda_function.zip *
```
You upload lambda_function.zip to AWS Lambda and save.
