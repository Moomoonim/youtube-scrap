# 🤗 Tasks: Image Segmentation

- 영상 링크: https://www.youtube.com/watch?v=dKE8SIt9C-w
- 채널: Hugging Face
- 업로드일: 2022-05-10
- 자막 언어: en
- 단어 수: 약 176개

---

## 스크립트

welcome to the hugging face task series in this video we'll take a look at the image segmentation task the image segmentation test divides an image into segments where every pixel in the image is assigned a label this test has multiple variants instant segmentation panoptix segmentation and semantic segmentation semantic segmentation is the task of segmenting parts of an image together which belong to the same class semantic segmentation models assign a probability of a class to each pixel instant segmentation is the variant of image segmentation where every distinct object in the image is segmented instead of one segment per class panoptix segmentation segments the image both instance wise and class wise it assigns every pixel a distinct instance of the class segmentation models are evaluated on the overlap between the predicted mask and the ground truth mask the overlap is called the intersection over union and metrics such as mean average precision are calculated on the intersection over union for more information about the segmentation tasks check out the hugging face task pages
