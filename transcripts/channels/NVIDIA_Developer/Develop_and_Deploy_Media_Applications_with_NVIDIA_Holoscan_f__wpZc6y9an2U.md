# Develop and Deploy Media Applications with NVIDIA Holoscan for Media

- 영상 링크: https://www.youtube.com/watch?v=wpZc6y9an2U
- 채널: NVIDIA Developer
- 업로드일: 2023-11-15
- 자막 언어: en
- 단어 수: 약 239개

---

## 스크립트

This is NVIDIA Holoscan for media&nbsp; which delivers on the EBU vision for&nbsp;&nbsp; the dynamic media facility making software media&nbsp; functions that mean we can repurpose hardware,&nbsp;&nbsp; commercial off-the-shelf hardware, to deliver&nbsp; functionality for broadcasters from multiple&nbsp;&nbsp; vendors all running on the same platform. The&nbsp; platform architecture starts with servers with&nbsp;&nbsp; NVIDIA GPUs and networking. It has open-source&nbsp; kubernetes with the NVIDIA GPU operator and&nbsp;&nbsp; network operator which expose the networking and&nbsp; GPU into kubernetes and mean that applications can&nbsp;&nbsp; be written that rely on those in a containerized&nbsp; environment. The platform is built around Open&nbsp;&nbsp; Standards and specifications so that we&nbsp; have SDKs that support ST2110 and NMOS,&nbsp;&nbsp; PTP, and the other broadcast specifications. But&nbsp; you're not locked into a particular control plane&nbsp;&nbsp; or a particular transport because of the way the&nbsp; platform is built, you can rely on any of your&nbsp;&nbsp; SDKs that you would use on bare metal and shift&nbsp; your application to a containerized deployment.&nbsp;&nbsp; And kubernetes takes care of scheduling your&nbsp; applications on a node in your server cluster&nbsp;&nbsp; that has the facilities that you need for your&nbsp; application. So this has advantages both for&nbsp;&nbsp; the broadcaster who can repurpose their their&nbsp; hardware platform with the applications that&nbsp;&nbsp; they need in the current hour the current day the&nbsp; current minute, but it also has advantages for&nbsp;&nbsp; the vendors who can rely on a platform while&nbsp; still being deployed in an in an open way.
