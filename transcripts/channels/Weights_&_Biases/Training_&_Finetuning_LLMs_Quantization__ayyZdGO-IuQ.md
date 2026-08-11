# Training & Finetuning LLMs: Quantization

- 영상 링크: https://www.youtube.com/watch?v=ayyZdGO-IuQ
- 채널: Weights & Biases
- 업로드일: 2024-02-06
- 자막 언어: en
- 단어 수: 약 232개

---

## 스크립트

[Music] we are putting a large language model into one GPU simply most large language model you download today will have trouble fitting that why if you think about it um if you have one parameters and you represent as a 32bit float or like four bytes um if you have a a billion of those parameters that's for gigabytes and that's just for weights alone now you if you need to find tune you or training you have other things so at 8 bit per parameter for example for your atom Optimizer four bits for like gradient and up to eight bits for like activations and temporary memories it really adds up so how do you actually make this fit so this is like a technique called the quantization and uh the simplest way you can approach is just LP up some of the positions so you can go like instead of 32 you can do 16 bit or you can go even further to 8 bit or use some like interesting like uh more nuanced floating Point representation so for example Google's like be float 16 which like changes the number of bits for mantisa and exponent as opposed to the standard iple e so these are some of the ways and there's many many other ways that you could explore and this is just kind of teaser on quantization
