# serverless-aws-python-with-deps

Extending the [`serverless-aws-python` template](https://www.pulumi.com/templates/serverless-application/aws/) to show how to bundle Lambda dependencies.

[![](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new?template=https://github.com/cnunciato/serverless-aws-python-with-deps)

## Create a new project

```bash
mkdir serverless-aws-python-with-deps && cd $_
pulumi new https://github.com/cnunciato/serverless-aws-python-with-deps
```

## Deploy to AWS

```bash
pulumi up
```

## Browse to the endpoint

```bash
open $(pulumi stack output url)/date
```

# Observe

![](https://private-user-images.githubusercontent.com/274700/339875758-942b96a2-78e8-4553-a7c2-b4c9edd83176.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTgzOTE4ODAsIm5iZiI6MTcxODM5MTU4MCwicGF0aCI6Ii8yNzQ3MDAvMzM5ODc1NzU4LTk0MmI5NmEyLTc4ZTgtNDU1My1hN2MyLWI0YzllZGQ4MzE3Ni5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNjE0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDYxNFQxODU5NDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hYmI0MGI3NGZjN2ZhN2JmN2Q0OGU1YTU5MTBmYTljZmQ2MDk4Mjc4NjAwOGIzMzNmYWUyMGY0YWU3ZmMzZTAwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.jdWA4sLjrNR7z7g2EaDBdHidtliwixgrb-1bmY2BTk0)
