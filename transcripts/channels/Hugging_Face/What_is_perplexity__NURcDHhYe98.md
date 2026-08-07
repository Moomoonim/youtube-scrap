# What is perplexity?

- 영상 링크: https://www.youtube.com/watch?v=NURcDHhYe98
- 채널: Hugging Face
- 업로드일: 2021-11-15
- 자막 언어: en
- 단어 수: 약 295개

---

## 스크립트

In this video we take a look at the&nbsp; mysterious sounding metric called Perplexity.&nbsp;&nbsp; You might have encountered perplexity&nbsp; when reading about generative models.&nbsp;&nbsp; You can see two examples here from the original&nbsp; transformer paper “Attention is all you need”&nbsp;&nbsp; as well as the more recent GPT-2 paper. Perplexity&nbsp; is a common metric to measure the performance&nbsp;&nbsp; of language models. The smaller the value the&nbsp; better the performance. But what does it actually&nbsp;&nbsp; mean and how can we calculate it? A very common&nbsp; quantity in machine learning is the likelihood.&nbsp;&nbsp; We can calculate the likelihood as the&nbsp; product of each token’s probability&nbsp;&nbsp; What this means is that for each token we use&nbsp; the language model to predict its probability&nbsp;&nbsp; based on the previous tokens. In the end we&nbsp; multiply all probabilities to get the Likelihood.&nbsp;&nbsp; With the likelihood we can calculate&nbsp; another important quantity:&nbsp;&nbsp; the cross entropy. You might already have heard&nbsp; about cross-entropy when looking at loss function.&nbsp;&nbsp; Cross-entropy is often used as a&nbsp; loss function in classification.&nbsp;&nbsp; In language modeling we predict the next&nbsp; token which also is a classification task.&nbsp;&nbsp; Therefore, if we want to calculate the cross&nbsp; entropy of an example we can simply pass it to the&nbsp;&nbsp; model with the inputs as labels. The loss return&nbsp; by the model then corresponds the cross entropy.&nbsp;&nbsp; We are now only a single operation&nbsp; away from calculating the perplexity.&nbsp;&nbsp; By exponentiating the cross-entropy we get the&nbsp; perplexity. So you see that the perplexity is&nbsp;&nbsp; closely related to the loss. Keep in mind that&nbsp; the loss is only a weak proxy for a model’s&nbsp;&nbsp; ability to generate quality text and the same is&nbsp; true for perplexity. For this reason one usually&nbsp;&nbsp; also calculates more sophisticated metrics&nbsp; such as BLEU or ROUGE on generative tasks.
