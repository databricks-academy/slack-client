# Slack-Client
Owner: Jacob Parr | A Slack client that is capable of maintaining slack-threads

# Purpose
This client is used by various apps including AWS Lambdas and Spark Listeners to post messages back to Slack.

It's key feature is its ability to maintain a slack-thread and post updates to that one thread and thus avoiding spamming of the named channel.

# Getting Started

```
conda create -n slack-client python=3.8
conda activate slack-client
pip install -r requirements.txt
```
