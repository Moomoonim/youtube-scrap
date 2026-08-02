# What Is a Model?

- 영상 링크: https://www.youtube.com/watch?v=-hazM31Nys4
- 채널: SambaNova
- 업로드일: 2026-06-30
- 자막 언어: en
- 단어 수: 약 361개

---

## 스크립트

A model is a system that learns patterns from data and uses those patterns to produce an output. You give it an input and it predicts a result, just like you might be familiar with using chat GPT. The most widely used model today is the large language model or LLM. It might read a sentence and continue it. It might look at an image and describe what's in it. Or it might even write code that you can execute. There are other types of models that handle images, audio, and more. But in this series, we're focused on LLMs. The key idea is that a model does not memorize one exact answer for every situation. Instead, it learns patterns from many examples, then applies those patterns to something new. But how does it actually learn? During training, the model makes a prediction, checks whether it was right or wrong, and adjusts itself next time. It does this billions of times across massive amounts of data. Over time, those tiny adjustments add up and the model gets remarkably good at recognizing patterns it's never explicitly been told about. The output of training a model is the model weights, billions of numbers that represent everything the model has learned. You might have heard these called parameters, like when someone says a model has 70 billion parameters. That's literally 70 billion numbers. Each one a tiny adjustment the model made during training. Together, they are the model. When you actually use the model, that's called inference. It takes your input and gives you an output. But to do that, it has to run calculations across all 70 billion of those parameters. No single chip can hold all of them, so you split them across many chips. And now the hard part isn't just doing the calculations, it's getting the right data to the right chip at the right time. That's what inference speed actually comes down to. Get it right, and it feels instant. So, if you remember one thing from this lesson, remember this. A model is billions of learned numbers through training, and inference is the challenge of running the model.
