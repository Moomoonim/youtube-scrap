# The user experience problem plaguing AI (and the eval fix)

- 영상 링크: https://www.youtube.com/watch?v=tsAVPDuE7i8
- 채널: Cerebras
- 업로드일: 2025-12-11
- 자막 언어: en
- 단어 수: 약 307개

---

## 스크립트

Today we're going to be talking about the horrors of not having evals. &gt;&gt; Everyone knows about like the airplane incidents or the banking incidents. You know, maybe a model hallucinates financial advice or something. I think those are kind of obvious cuz some of them are so horrendous that the model labs pick up on um these very glaring issues and solve them. But I'll give you an example. There's a very popular uh coding tool and I actually stopped using it for this reason cuz [music] I just couldn't take it after a certain point. If you edit something in the editor [music] and then you ask the agent to help you, it will go and like edit stuff in the editor for you. But then if you go and edit it again yourself and then you ask the agent for help um there's some kind of modelbased thing in this product that tell that tries to determine whether the agent should put in the extra [music] compute cycles of reading the stuff that you edited and updating its context with it. What uh I personally experienced over and over again is that it just wouldn't [music] and so I would ask for help and it would just overwrite my changes. This is such a grading experience to someone who's using [music] this uh product constantly. Really good uh eval mean that when someone complains to you with an issue like this um it's very low friction for you to go and find the trace, add that example into some evals, reproduce it, and then make sure that at least for the person who is hitting it, it doesn't happen again. And in general, you have a good representation of this type of issue um that you can prevent from happening in in the future.
