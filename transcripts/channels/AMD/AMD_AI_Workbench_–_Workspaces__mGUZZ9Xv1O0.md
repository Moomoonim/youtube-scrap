# AMD AI Workbench – Workspaces

- 영상 링크: https://www.youtube.com/watch?v=mGUZZ9Xv1O0
- 채널: AMD
- 업로드일: 2026-07-27
- 자막 언어: en
- 단어 수: 약 375개

---

## 스크립트

In this video, we will walk you through the workspaces feature of the AMD AI Workbench. The workspaces provide various interactive environments designed to support AMD compute. For example, JupyterLab and Visual Studio Code workspaces enable users to harness the power of the cluster with zero configuration on their local machines. In this demo, we will show you how to create and access a Visual Studio Code workspace. Let's take a look at how it works. The first step is to navigate to the workspaces page where you can view all available workspaces. In this case, we are interested in creating a Visual Studio Code workspace. To deploy a workspace, click deploy. This will open the workload deployment drawer. From here, you can change the name of the workspace, choose the container image, assign secrets, and customize the resource allocation. As you can see, you can change the number of GPUs, the amount of memory, and the number of CPU cores per GPU. Once you have set the desired configuration, you can deploy the workspace by clicking deploy. While it's loading, you can track the deployment progress in the dashboard page. Here you can see that the status is currently marked as pending while it is being prepared. Back on the workspaces page, we can see that once the workspace has launched, the deployment overlay will display a launch button which you can click to access the workspace. Once inside, you can use the workspace just like a regular Visual Studio Code project. For example, you can open a terminal, create, upload and run your files, and more. Note that you have persistent storage in the workload folder visible on the left. In this case, let's create a notebook and you can run this notebook as you normally would. So let's for example import Torch and create a random tensor and then run it. If this is the first time you are running the notebook, you need to select and possibly install your environment, but once selected and installed, the notebook will run and you will see the results. And that is how you use the workspace feature in the AMD AI Workbench to access the GPU cluster with zero configuration on your local machine.
