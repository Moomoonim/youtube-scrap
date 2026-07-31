# The Top 10 Lambda Functions in the Console

- 영상 링크: https://www.youtube.com/watch?v=HZrLOoFIcpM
- 채널: AWS Developers
- 업로드일: 2024-12-10
- 자막 언어: en
- 단어 수: 약 365개

---

## 스크립트

How can you quickly identify the top 10 Lambda functions that are throwing errors in your AWS account? Hey, I'm Eric Johnson, Principal Developer Advocate at AWS, and this is a Serverless DX Answer. Developers tell us they struggle to find metrics around the top 10 Lambda functions in their account. From identifying functions with the most invocations to illuminating functions with the highest error account, they wanna have this information at their fingertips. Previously, developers needed to go to the Amazon CloudWatch console and manually build out this report. However, as of today, the Lambda dashboard now has three new metrics called the Top 10 Functions. Let's take a look. First, I'm gonna go to the Lambda console inside the AWS console. And over on the left side, I see a navigation to the dashboard. I'm gonna click that. And here at the top is what we're looking for, the top 10 functions. First, I have the errors, and this is the top 10 functions with the highest errors, then I have invocations, the top 10 functions with the highest invocations, and finally, the concurrent executions, which are the top 10 Lambda functions with the highest count of executions. I can then go and I can scroll through these and see which Lambdas they are. So I can see all 10 right here. And finally, that I can hover over and I can see the individual metrics for each one. And with that, that gives you access to the top 10 metrics for your Lambda functions inside the AWS console. With these metrics in place, I can quickly identify the top 10 Lambda functions in my account without having to change context to a different service. And that's a quick look at the new top 10 metrics in the Lambda console. Now I know the developers are not usually building directly in the console. However, this is one of the many changes coming to improve console to desktop uniformity and portability. Keep an eye on this space for more DX improvements. Be sure to subscribe to this channel for more videos like this. Again, I'm Eric Johnson, and this is a Serverless DX Answer.
