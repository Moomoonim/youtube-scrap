# Mapless Driving: AI Powered Autonomy at Urban Scale - DRIVE Labs Ep.38

- 영상 링크: https://www.youtube.com/watch?v=u_eZoOS5bFc
- 채널: NVIDIA
- 업로드일: 2025-05-15
- 자막 언어: en
- 단어 수: 약 351개

---

## 스크립트

[Music] High definition or HD maps are detailed digital model of the world, including elements like road geometry, signs, and traffic signals. While they've been widely used for autonomous driving, they're costly to create and maintain. This has led to the growing demand for matless driving. In this episode of Drive Labs, we'll explore NVIDIA innovations that enhance Mattless driving by removing information bottlenecks, improving task accuracy and accelerating model training and inference times. One solution is NVIDIA Roadet, a single bird's eye view or BEV transformer network. It predicts road geometry in real time, detecting lanes, paths, road boundaries, and other road surface elements. RoadNet's outputs can be further refined through topology aware context fusion, integrating perception signals to enhance lane geometry. In a finalist for the CVPR 2024 best paper award, NVIDIA researchers introduced a general uncertainty formulation for maps that can be integrated into any online mapping model. Here we see typical online mapping outputs with road boundaries in green and lane dividing lines in yellow. In contrast, our approach models uncertainty shown as shaded ellipses producing probabilistic maps. This method can be applied to many existing models reducing training time by up to 50%. While enhancing accuracy in downstream models like motion prediction by up to 15%. We can enhance MATLAS driving further by exposing internal features from online mapping models instead of their usual polyline outputs. In our ECCV 2024 work, we introduced techniques to connect transformers and graph neural networks to mapping, allowing downstream models access to their rich BEV features. By skipping HDM decoding, we reduce overall inference time by up to 73%. While improving task accuracy by up to 29%. This provides a direct path from existing MATLA driving architectures to end toend AV stacks by removing information bottlenecks while more tightly integrating existing models such as online mapping and planning. NVIDIA is leading the way in advancing matless driving solutions. With RoadNet, online mapping, and the shift toward end-to-end architectures, we're reducing reliance on HD maps and advancing scalable, adaptable autonomous driving. For more information, please read our papers on Mattless Driving.
