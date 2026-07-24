# How to Go from Product Shot to Social Ad in Minutes | Runway

- 영상 링크: https://www.youtube.com/watch?v=OHowmVSSqLQ
- 채널: Runway
- 업로드일: 2026-02-05
- 자막 언어: en
- 단어 수: 약 407개

---

## 스크립트

This workflow creates complete social ads from a single product shot. Let's build it from scratch. Head to the workflows page and create a new workflow. We'll start with our product shot. Hit the plus button and create a new image node. Grab your product shot from the file browser. Next, add a text node. You can right-click in the empty canvas space to open the node create dialogue and select text. Last way to create a node is to drag from the output handles of any existing node and let go in the empty canvas. Select a Nano Banana Pro node from the dialogue. Hit the settings button in the top right of the node and set your aspect ratio to 9 by 16. Let's write a prompt to design our ad. This image will be the foundation for our ad. Looking closer, we can see the details of our product have been preserved. Now, let's add text. Create a new image node, find a reference for the typeface you like to use. Using this reference, we can generate text in a similar style. Create a text node and hook these inputs up to a new Nano Banana Pro node. For this prompt, we'll add instructions to render the slogan of our choice over a white background. Now, we can wire our ad image and text reference into a Nano Banana Pro node to create a modified frame that includes our slogan. Pro tip, you can drag out from a node's input handle to automatically open the node create dialogue and get a list of nodes compatible with that input. With this prompt, we'll define an end frame for our ad that includes our text. Here, I'll adjust the pose of the subject to create some implied motion and prepare for the video generation phase coming next. Now, we have everything we need to complete our ad. Create a VO image to video node and connect the first image we generated to the start frame input. Connect the image that includes the text to the end frame input. Create a text node. Dial in your settings on the VO node and let's write our final prompt. Here, I'll include instructions to add subtle movement to the character and a motion graphics animation to the text. Add an upscale video node to render the ad in 4K. Discover more featured workflows or create your own at runwayml.com/workflows.
