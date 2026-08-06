# How to Share TensorBoard Metrics on the 🤗 Hub

- 영상 링크: https://www.youtube.com/watch?v=7eaBs2BAdPI
- 채널: Hugging Face
- 업로드일: 2022-01-26
- 자막 언어: en
- 단어 수: 약 357개

---

## 스크립트

hey everyone i'm nate from hugging face and today i'm going to show you how you can share tensorboard training metrics on the hug and face hub if you find this video helpful give it a like and consider subscribing to our youtube channel for more content like this to get tensorboard running remotely with your hug and face model repo you just need to upload the tf events files used by tensorboard to a directory named logs in your repo let's see how this works with keras here i'll quickly run through the denoising autoencoder example from the kerastocks that we covered it in the hug and face hub keras integration video which i'll include a link to the difference here is that i'll initialize a tensorboard callback to track the training metrics and include it when we call autoencoder.fit once the model is finished training we'll push it up to the hub after that we can see the repo we created but notice it does not have the tensorboard training metrics yet that's because we didn't upload them let's go back and add them when we pushed the model a directory named after the model id we specified was created we'll just copy our logs directory from the tensorboard callback into that directory now we'll use git add git commit and get push to upload that new directory to our repo now that's finished let's take a look at our model repo again and after loads we'll see that a remote version of tensorboard is in our repo when you click the training metrics tab these links are shareable which means that you can send your results publicly or privately to your teammates so you always have access to both your training metrics and the associated model so that's how you add tensorboard training metrics to the hug and face hub if you found this video helpful give it a like and consider subscribing to our youtube channel you can also join our discord server to connect with over 3000 other people interested in machine learning thanks for watching until next time bye [Music] you
