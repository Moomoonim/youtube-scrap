# 🤗 Tasks: Text Classification

- 영상 링크: https://www.youtube.com/watch?v=leNG9fN9FQU
- 채널: Hugging Face
- 업로드일: 2022-05-17
- 자막 언어: en
- 단어 수: 약 312개

---

## 스크립트

welcome to the hugging face task series in this video we'll take a look at text classification in text classification models receive a text as input and return class labels and their associated probabilities there are many variants of this task that lets you analyze sentiment assess grammatical correctness determine if one question is a paraphrase of another or determine if a statement is correct according to a given text we will not cover all of them in this video you can take a look at the text classification task page for more details sentiment analysis is the task of determining sentiment of a given text these models receive a text and return either polarity or emotion in it another variant is natural language inference and line models take a premise and a hypothesis and return a label if the hypothesis is true and the line model returns entailment if the hypothesis is false it returns contradiction or if there is no relation it returns neutral question and a line models take a text and the question and return entailment if the answer to the question can be found in a text and not entailment otherwise this model can be used in modeling information retrieval problems glue is a benchmark that is used to measure the performance of nlp models across 10 different tanks classification tasks these data sets are useful for fine-tuning the text classification models as well text classification models are evaluated on accuracy and the fund score the metrics are calculated for each of the class labels predicted for texts and take the average to measure the overall performance of the model as an example use case you can classify your customers reviews from the product reviews or tweets using sentiment analysis models to make better business decisions for more information about text classification check out the task pages
