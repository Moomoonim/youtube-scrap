# Searching Messy Documents for Contextual Meaning | Mistral OCR and Qdrant Vector Search

- 영상 링크: https://www.youtube.com/watch?v=bA9FrWqOoZo
- 채널: Qdrant
- 업로드일: 2025-08-27
- 자막 언어: en
- 단어 수: 약 381개

---

## 스크립트

Have you ever lost your notes? Or maybe you lost a presentation? You've got some kind of corpus of data that you need to sift through to find your specific item, but you don't remember exactly what the title was or how to find it. That's where Quadrant Quill comes in. Mistro just released a new OCR model that does surprisingly well with handwriting. Combining it with semantic search allows you to upload a document. And here I'm going to be uploading a document which is actually notes on a Apple M4 sustainability report. So if we take a look at the document, you'll see Apple M4 report and then I have some notes there in handwriting. And this is the image that we'll be uploading. So we're going to upload that image because let's say we've got a thousand different reports and we're not exactly sure what the title was of this sustainability report and we want to just find it with the click of a button. We'd click that button and you see there we get the M4 report. But you might be thinking to yourself, well, of course we found the report. You've got the title in the search. So, let's make things a little harder for Quadrant. We're going to take the title out and we're also going to add a random sentence. I like turtles. And then later on, I'll say chocolate smells. And you see there's some typos in there, some misformatting. Let's see how Quadrant handles this one. And you'll see we had 84, it went down to 78, but due to Quadrant being able to capture the semantic meaning of the document, we still were able to retrieve that report. And this works the other way as well. So, for example, if you wanted to upload a source document, we could go the other way and say, "Hey, I have this source document and I want to find the notes that are relevant to that source document. and we run that search and we pull up our notes because that is the most relevant document. So this is a great way for you to be able to build a system that allows you to semantically search through your documents combining Mistral and Quadrant.
