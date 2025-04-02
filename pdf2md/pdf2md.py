import onnxruntime as ort

print(
    ort.get_available_providers()
)  # 应输出 ['CPUExecutionProvider'] 或 ['CUDAExecutionProvider', 'CPUExecutionProvider']
