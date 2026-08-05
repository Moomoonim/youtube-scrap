# How to swap models safely (without breaking production)

- 영상 링크: https://www.youtube.com/watch?v=bGbgG5CmYn0
- 채널: Cerebras
- 업로드일: 2025-12-10
- 자막 언어: en
- 단어 수: 약 386개

---

## 스크립트

So maybe just to get a product out the door as quickly as possible, you picked the largest model you could and now people are using it, but they're complaining like, "Yeah, this is great, but it's too slow." One of the things that we've seen a lot of companies do recently is take those use cases, um, turn them into EVELs and then try to figure out how they can make smaller, more cost effective or faster models actually solve the same use cases. [music] &gt;&gt; Okay. What is the default model that you see people kind of gravitating towards like when they're starting out and then what do they how do they switch? &gt;&gt; Yeah, I think you know the frontier models that we see people start out on our GPT5, Claude 4 and above and Gemini 2.5. I was talking to one of our customers recently and they're actually still using Llama 3.1. And the reason is that they've been using it for a few years now and so they really understand all of the quirks of uh the model, where it performs well, where it doesn't perform well, how to get it to perform well for certain use cases. I think another thing that people uh often don't think about in the moment is getting stuck on particular models. We'll often talk to people that are still using models like GPT 3.5. [music] Really, I mean, you shouldn't be using GPT 3.5 in production at this point. The reason they do is that they have revenue driving use cases that depend on their application and they have no way of actually modernizing what they do without potentially breaking things like they have no idea. &gt;&gt; So you're saying like adding emails and logging is a really good way to migrate models while safely knowing that you're not going to break production basically. &gt;&gt; Absolutely. Yeah. I think the very best companies that we work with, they're able to make production model changes within 24 hours of new models coming out. they can go to your website, get an API key, push a button, and then get an email like right then and there that tells them whether that's even possible or not. We've seen those companies obviously move a lot faster. [music]
