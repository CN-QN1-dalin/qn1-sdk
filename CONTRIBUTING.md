# 贡献指南

## 架构说明

QN1 SDK 核心结构：

```
qn1/                   # 核心引擎（闭源）
├── taichi_lock/       # 归元锁加密层
├── hetero.py          # 异构引擎
├── ring.py            # RingBuffer
└── ...

docs/                  # 文档
examples/              # 使用示例
dist/                  # 发行包
```

## llama.cpp 集成

QN1 RingBuffer 和 AnchorPool 已集成至 llama.cpp：

- **RingBuffer** — O(1) KV Cache 滑动窗口
- **AnchorPool** — 智能锚点缓存管理器
- **Heterogeneous** — 混合推理调度

相关 PR 请提交至 [llama.cpp](https://github.com/ggerganov/llama.cpp) 官方仓库。

## 开发

```bash
# 克隆
git clone https://github.com/CN-QN1-dalin/qn1-sdk.git
cd qn1-sdk

# 安装开发环境
pip install -e ".[dev]"

# 运行测试
pytest tests/
```

## 许可

本项目为专有软件。贡献代码即代表您同意将代码授权给 QN1 项目。
未经许可不得将核心引擎源码用于其他项目。
