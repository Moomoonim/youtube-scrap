# Why are fast tokenizers called fast?

- 영상 링크: https://www.youtube.com/watch?v=g8quOxoqhHQ
- 채널: Hugging Face
- 업로드일: 2021-11-15
- 자막 언어: en
- 단어 수: 약 284개

---

## 스크립트

Why are fast tokenizers called fast? In this video&nbsp; we will see exactly how much faster the so-called&nbsp;&nbsp; fast tokenizers are compared to their&nbsp; slow counterparts. For this benchmark,&nbsp;&nbsp; we will use the GLUE MNLI dataset, which&nbsp; contains 432 thousands pairs of texts.&nbsp;&nbsp; We will see how long it takes for the&nbsp; fast and slow versions of a BERT tokenizer&nbsp;&nbsp; to process them all. We define our fast and slow&nbsp; tokenizer using the AutoTokenizer API. The fast&nbsp;&nbsp; tokenizer is the default (when available), so we&nbsp; pass along use_fast=False to define the slow one.&nbsp;&nbsp; In a notebook, we can time the execution of a&nbsp; cell with the time magic command, like this.&nbsp;&nbsp; Processing the whole dataset is four&nbsp; times faster with a fast tokenizer.&nbsp;&nbsp; That's quicker indeed, but not very impressive&nbsp; however. That's because we passed along the&nbsp;&nbsp; texts to the tokenizer one at a time. This is&nbsp; a common mistake to do with fast tokenizers,&nbsp;&nbsp; which are backed by Rust and thus able to&nbsp; parallelize the tokenization of multiple texts.&nbsp;&nbsp; Passing them only one text at a time is like&nbsp; sending a cargo ship between two continents&nbsp;&nbsp; with just one container, it's very inefficient.&nbsp; To unleash the full speed of our fast tokenizers,&nbsp;&nbsp; we need to send them batches of texts, which&nbsp; we can do with the batched=True argument&nbsp;&nbsp; of the map method. Now those results are&nbsp; impressive! The fast tokenizer takes 12 seconds to&nbsp;&nbsp; process a dataset that takes 4 minutes to the slow&nbsp; tokenizer. Summarizing the results in this table,&nbsp;&nbsp; you can see why we have called those&nbsp; tokenizers fast. And this is only for&nbsp;&nbsp; tokenizing texts. If you ever need to train a&nbsp; new tokenizer, they do this very quickly too!
