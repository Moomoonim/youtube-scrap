# Migration from Vertiv™ Avocent® DSView™ 4.5 to Vertiv™ Avocent® DSView™ MP1000

- 영상 링크: https://www.youtube.com/watch?v=RjviyUqjjuI
- 채널: Vertiv
- 업로드일: 2025-11-06
- 자막 언어: en
- 단어 수: 약 367개

---

## 스크립트

[music] This video will cover the Verdive DSV 4.5 migration to the DSV solution platform with the ACS appliance. To begin, I'm logged into my ACS that is currently managed by DSV 4.5. In the left hand sidebar under system security and DS view you should see that the ACS is currently managed. On the left hand sidebar again when you select authentication the appliance authentication should be set to DSV/local. Below that when you select authentication servers and DS view you should see the IP address of the DSV 4.5 server that is managing the ECS. Before we make any changes, we'll save the ACS configuration. From here, I'll log on to my DSV server. You should see the ACS appliance under the unit page. When you select the ACS, you will see a copy of the web overview. You can interact with this overview to manage the ACS as if you were in the ACS web interface itself. When you select the ACS target from the unit view page, you'll be met with an interface similar to the ACS web interface. From here, you can use this to manage the ACS. Before we've removed this target, we need to make sure it is in unsecure mode. You can check this under the [music] appliance page, selecting properties and network. If you'd like to customize the information shown on the DSV 4.5 server, on the right hand side, select customize fields and filters. Now the ACS is ready to be unenrolled from DSV 4.5. Select the ACS by checking the check box, then select delete. When the prompt pops up, select okay. You should now see the ACS is removed from the DSV software. Going back to my ACS, you can see that it's automatically been unenrolled from the DSV server. The ACS is now ready to be enrolled in DSV solutions MP1000. In the MP1000 web interface, I select add a device and input the parameters for the ACS. The ACS has now been successfully discovered by the MP1000 DSV solution platform. Going back to my ACS 8000, you can see that the new management platform is the IP address of the DSV solution MP1000.
