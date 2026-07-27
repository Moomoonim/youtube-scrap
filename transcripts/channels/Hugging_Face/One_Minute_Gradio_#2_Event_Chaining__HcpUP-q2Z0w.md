# One Minute Gradio #2: Event Chaining

- 영상 링크: https://www.youtube.com/watch?v=HcpUP-q2Z0w
- 채널: Hugging Face
- 업로드일: 2024-07-15
- 자막 언어: en
- 단어 수: 약 360개

---

## 스크립트

hi everyone welcome to one minute gradio where I discuss some concept in gradio in just about one minute so today I'd like to talk about how do you chain events in gradio so gradio has this concept of events that get triggered in different situations what if you want to do something after one event completes so let's as an example let's take a look at this very simple uh gradio application so it has just two text boxes and when you click on this button underneath the text boxes the first one gets evaluated and the result gets piped to the second text box so I can make it think of it as a little maybe calculator I can go ahead and run this now maybe after this gets run I want to clear the first text box after this is complete well what I can do is I can just add another event so that says something like this def clear doesn't take an any inputs it just returns uh an empty string and then what I can do is I can take this event and I can say hey after this event is done then run clear and assign the result to this first text box so let me run this again I've saved this now if I run this you can see after the result came this first one is clear and maybe you only want to do this if the first one is successful so maybe if it's something like you know uh plus a this should not work but you can see here it ran an error but the first one still got cleared so if you only want to run the subsequent event when the first event completes successfully just change then to success and let's try running this again so now if I do something that's invalid valid it'll give me a chance to you know uh to edit that but if I do something that is valid then it still gets run successfully so that's it today we introduced the then and success event thanks so much for tuning in
