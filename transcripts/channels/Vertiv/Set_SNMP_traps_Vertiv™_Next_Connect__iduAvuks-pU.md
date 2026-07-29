# Set SNMP traps | Vertiv™ Next Connect

- 영상 링크: https://www.youtube.com/watch?v=iduAvuks-pU
- 채널: Vertiv
- 업로드일: 2026-04-22
- 자막 언어: en
- 단어 수: 약 369개

---

## 스크립트

Welcome to this how-to video on setting the Vertiv Geist r Connect Agent as an SNMP trap target. In this tutorial, we'll show you how to configure Vertiv Power IT IMD devices so the local agent can receive SNMP trap notifications. So, without further ado, let's get started. For Vertiv Power IT IMD devices, the easiest way to configure the trap target is by using the device's local web interface. First, manually the SNMP settings on one device. Then, go to the system menu. And while you're in the system menu, select SNMP. Scroll to the bottom of the SNMP page and click the add icon next to the trap target list. Enter the agent's IPv4 address. Now, select the appropriate SNMP version. Associate with the existing [music] SNMP credentials. And then, click save. Raven based devices support both V1, V2C, and V3 simultaneously, but maintain a single credential set per version. After adding the trap target, retrieve the updated host configuration JSON file. To do this in your browser, enter the device's IP followed by Then, right click the displayed configuration. Choose save as &gt;&gt; [music] &gt;&gt; and save the file with a .json extension. Open the file in a code editor like Visual Studio Code or Notepad++. Inside this SNMP section, confirm that the new trap target is listed. Make sure to only include the relevant SNMP section if you're reusing this file across multiple devices. This helps prevent accidental overwrites. Keep in mind that the exported JSON file won't contain any SNMP [music] credentials. If you import a file and credentials are blank, existing credentials will remain unchanged. Once the file is ready, upload it to the Vertiv Geist r Connect platform and push it to additional edge devices as needed. For full details on the format, refer to the Vertiv Power IT public API specification available at the link shown here. And that's it. You've now learned how to set the Vertiv Geist r Connect Agent as a trap target for Vertiv Power IT IMD devices, making sure the agent can receive real-time alerts across your environment. Thanks for watching. For more how-to videos and detailed walkthroughs, visit the Vertiv Geist r Connect support documentation.
