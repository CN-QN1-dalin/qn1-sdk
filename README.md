<p align="center">
  <img src="https://raw.githubusercontent.com/CN-QN1-dalin/qn1-sdk/main/docs/assets/qn1_logo.svg" alt="QN1 Logo" width="200"/>
</p>

# QN1 — 念动幻化 · 全域核心引擎

> **一行替换，零训练无损，三端统一 API**

[![PyPI](https://img.shields.io/badge/pypi-qn1-blue)](https://pypi.org/project/qn1/)
[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20|%20Linux%20|%20Windows-lightgrey)]()

---

## 📦 安装

```bash
# MLX 后端（推荐 macOS）
pip install qn1

# GGUF 后端（CPU 推理）
pip install qn1[gguf]

# PyTorch 后端（GPU 推理）
pip install qn1[torch]

# 全部后端
pip install qn1[all]
```

> 详细安装指引 → [docs/QUICKSTART.md](docs/QUICKSTART.md)

---

## 🚀 一行替换

```python
from qn1 import auto

# 自动检测模型、后端、最优引擎
engine = auto("Qwen2.5-7B-Instruct-4bit")

output = engine.generate("用三句话解释量子计算")
print(output)
```

### MLX（macOS）

```python
from mlx_lm import load
from qn1 import monkey_patch

model, tokenizer = load("Qwen2.5-7B-Instruct-4bit")
monkey_patch(model, preset="lite")

output = model.generate("解释 Transformer 工作原理", tokenizer=tokenizer)
```

### GGUF（跨平台 CPU）

```python
from qn1 import create_llama_engine

engine = create_llama_engine("/path/to/model.gguf")
output = engine.generate("写一个快速排序")
```

---

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| **零训练替换** | 无需重新训练，一行代码替换原注意力机制 |
| **三端统一 API** | MLX · GGUF · PyTorch 同一套接口 |
| **RingBuffer™** | O(1) KV 缓存，上下文越长优势越大 |
| **Hetero 异构** | GPU 近场 + CPU 锚点池 + α 自适应融合 |
| **归元锁™** | 四层道家加密体系，保护核心 IP |

---

## 📊 效果数据

> macOS M1 Pro 16GB + Qwen2.5-7B-Instruct-Q4_K_M

| 上下文 | 标准内存 | QN1 RingBuffer | 节省 |
|--------|---------|----------------|:----:|
| 1K     | 14 MB   | 14 MB          | 1.0× |
| 8K     | 112 MB  | **0.5 MB**     | **224×** |
| 16K    | 224 MB  | **0.5 MB**     | **462×** |
| 32K+   | → OOM   | **→ 继续运行** | **∞** |

> 更多数据 → [docs/PERFORMANCE.md](docs/PERFORMANCE.md)

---

## 🛡️ 归元锁（独立产品）

四层防御体系：

```
无形  →  C 扩展编译 (.so / .dylib)
散气  →  五路种子推演（混淆调用链）
渐退  →  质量腐朽（反调试反破解）
归元  →  破解静默降级
```

```bash
pip install guiyuan-lock
```

| 方案 | 价格 | 内容 |
|------|------|------|
| Free | ¥0 | Python 混淆 + 五路推演 |
| Pro 月付 | ¥9.9/月 | C 扩展 + 质量腐朽 + 哨兵 |
| Pro 年付 | ¥49.9/年 | 省 ¥69 |

---

## 💰 定价

| 方案 | 价格 | 说明 |
|------|------|:----:|
| **QN1 Free** | ¥0 | MLX RingBuffer · 4bit · 7B · 32K |
| **QN1 Pro 月付** | ¥9.9/月 | 全量化 · 全模型 · 128K · PyTorch hetero |
| **QN1 Pro 年付** | ¥49.9/年 | Pro × 12 → 省 ¥69 |

> 购买 → [ClawHub](https://clawhub.com) · 搜索 `qn1`

---

## 🔧 开发环境

| 环境 | 要求 |
|------|------|
| Python | ≥ 3.10 |
| MLX   | ≥ 0.31（macOS Apple Silicon） |
| PyTorch | ≥ 2.0（GPU 后端） |
| llama-cpp-python | ≥ 0.3（GGUF 后端） |

```bash
git clone https://github.com/CN-QN1-dalin/qn1-sdk.git
cd qn1-sdk
pip install -e .
```

> 完整开发指引 → [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🌐 兼容性

| 环境 | 状态 |
|------|:----:|
| macOS Apple Silicon + MLX | ✅ |
| Linux x86_64 + CPU（GGUF） | ✅ |
| Linux x86_64 + NVIDIA（PyTorch） | ✅ |
| Windows x86_64 + CPU（GGUF） | ✅ 待测 |
| macOS Intel | 🔄 开发中 |

---

## 📄 许可

专有软件 © 念动幻化 QN1 · CN_SJZ-QN1-大林

未经授权不得复制、分发、反编译核心引擎源码。

---

<p align="center">
  <sub>QN1 — 一念凝核，幻化全域引擎</sub>
</p>
