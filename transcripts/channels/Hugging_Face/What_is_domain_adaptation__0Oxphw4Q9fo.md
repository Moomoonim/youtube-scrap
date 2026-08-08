# What is domain adaptation?

- 영상 링크: https://www.youtube.com/watch?v=0Oxphw4Q9fo
- 채널: Hugging Face
- 업로드일: 2021-11-15
- 자막 언어: en
- 단어 수: 약 265개

---

## 스크립트

What is domain adaptation? When fine-tuning&nbsp; a pretrained model on a new dataset,&nbsp;&nbsp; the fine-tuned model we obtain will make&nbsp; predictions that are attuned to this new dataset.&nbsp;&nbsp; When the two models are trained with the same&nbsp; task, we can then compare their predictions&nbsp;&nbsp; on the same input. The predictions&nbsp; of the two models will be different,&nbsp;&nbsp; in a way that reflects the differences&nbsp; between the two datasets, a phenomenon we call&nbsp;&nbsp; domain adaptation. Let's look at an example with&nbsp; mask language modeling, by comparing the outputs&nbsp;&nbsp; of the pretrained distilBERT model with the&nbsp; version fine-tuned in chapter 7 of the course&nbsp;&nbsp; (linked below). The pretrained model makes generic&nbsp; predictions, whereas the fine-tuned model has its&nbsp;&nbsp; first two predictions linked to cinema. Since&nbsp; it was fine-tuned on a movie reviews dataset,&nbsp;&nbsp; it's perfectly normal to see it&nbsp; adapted its suggestions like this.&nbsp;&nbsp; Notice how it keeps the same predictions as&nbsp; the pretrained model afterward. Even if the&nbsp;&nbsp; fine-tuned model adapts to the new dataset,&nbsp; it's not forgetting what it was pretrained on.&nbsp;&nbsp; This is another example on a translation task.&nbsp; On top we use a pretrained French/English model&nbsp;&nbsp; and at the bottom, the version we fine-tuned in&nbsp; chapter 7. The top model is pretrained on lots of&nbsp;&nbsp; texts, and leaves technical English terms like&nbsp; plugin and email unchanged in the translation&nbsp;&nbsp; (both are perfectly understood by French people).&nbsp; The dataset picked for the fine-tuning is a&nbsp;&nbsp; dataset of technical texts where special attention&nbsp; was picked to translate everything in French.&nbsp;&nbsp; As a result, the fine-tuned model picked that&nbsp; habit and translated both plugin and email.
