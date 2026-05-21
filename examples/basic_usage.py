"""
QN1 SDK — 基础使用示例

运行方式（需先安装 qn1）：
    pip install qn1
    python examples/basic_usage.py
"""


def demo_auto():
    """自动模式 — 一行代码完成"""
    from qn1 import auto

    engine = auto()
    output = engine.generate("用三句话解释什么是 Transformer")
    print(f"【自动模式】\n{output}\n")


def demo_monkey_patch_mlx():
    """MLX 猴补模式（macOS）— 零训练替换注意力机制"""
    from mlx_lm import load
    from qn1 import monkey_patch

    model, tokenizer = load("Qwen2.5-7B-Instruct-4bit")
    monkey_patch(model, preset="balanced")

    output = model.generate(
        "用三句话解释什么是量子计算",
        tokenizer=tokenizer,
        max_tokens=500,
    )
    print(f"【MLX 猴补】\n{output}\n")


def demo_gguf():
    """GGUF 后端 — 跨平台 CPU 推理"""
    from qn1 import create_llama_engine

    engine = create_llama_engine("/path/to/your/model.gguf")
    output = engine.generate("写一个 Python 快速排序")
    print(f"【GGUF 后端】\n{output}\n")


def demo_pytorch():
    """PyTorch 后端 — GPU 推理"""
    from qn1 import create_torch_engine

    engine = create_torch_engine("Qwen/Qwen2.5-7B-Instruct")
    output = engine.generate("解释一下光速不变原理")
    print(f"【PyTorch 后端】\n{output}\n")


if __name__ == "__main__":
    print("=" * 50)
    print("QN1 SDK 使用示例")
    print("=" * 50)
    demo_auto()
