# HPC Assistant: GPU Profiling

- 영상 링크: https://www.youtube.com/watch?v=eIog5T41x1k
- 채널: AMD
- 업로드일: 2026-06-05
- 자막 언어: en
- 단어 수: 약 161개

---

## 스크립트

In this scenario, we have a Python script that runs matrix multiplications, and we want to profile its GPU kernels. We can ask the assistant to create a SLARMBatchJob script for profiling. Submit the job and monitor it until it finishes. Sometimes the first run may fail because of a script or environment issue. In that case, the assistant can inspect the error, update the batch script, and submit the job again. We could ask the assistant that once the profiling job completes, to read the profiler output and return a summary of the results. In the summary, it identifies the kernel configuration from the kernel name, explains what each part means, and reports the dispatch durations. It also highlights the steady state run time and points out one slower outlier run. So instead of manually writing the profiling script, checking the job logs, fixing errors, and parsing the profiler output, we can delegate the full profiling workflow to the assistant.
