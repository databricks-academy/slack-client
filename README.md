# Slack-Client
Owner: Jacob Parr | A Slack client that is capable of maintaining and contributing to a slack-thread that this client creates.

# Purpose
This client is used by various apps including AWS Lambdas and Spark Listeners to post messages back to Slack.

It's key feature is its ability to maintain a slack-thread and post updates to that one thread and thus avoiding spamming of the named channel.

# Getting Started

```
conda create -n slack-client python=3.8
conda activate slack-client
pip install -r requirements.txt
```

Once setup, unit tests can by ran by executing
```pytest```

# Usage

Usage of this library will require an OAuth Token obtained from your custom [Slack Application](https://api.slack.com/apps). One such application (Training Engine) currently exists and is available by contacting Jacob D. Parr.

Once obtained, the token can be specified by setting the `SLACK_OAUTH_ACCESS_TOKEN` environment variable to the appropriate value.

