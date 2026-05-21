# 快速开始

## 安装

### macOS（推荐 MLX）

```bash
pip install qn1
```

安装完成后通过 `qn1-trial` 获取试用：

```bash
pn1-trial --request
```

### Linux CPU（GGUF）

```bash
pip install qn1[gguf]
```

### GPU（PyTorch）

```bash
pip install qn1[torch]
```

## 基础使用

### 自动模式

```python
from qn1 import auto

engine = auto()
output = engine.generate("你好，请介绍一下自己")
print(output)
```

### 指定模型

```python
from qn1 import auto

engine = auto(
    model="Qwen2.5-7B-Instruct-4bit",
    backend="mlx",       # mlx | gguf | torch
    preset="performance" # lite | balanced | performance
)

output = engine.generate("写一个快速排序算法")
print(output)
```

### 许可证激活

```python
from qn1 import activate

activate("QN1-XXXX-XXXX-XXXX")  # 输入激活码
```

## 试用

```bash
# 查看试用剩余次数
qn1-trial --status

# 激活许可证
qn1-license --activate QN1-XXXX-XXXX-XXXX
```

## 更多

- [API 参考](API_REFERENCE.md)
- [性能数据](PERFORMANCE.md)
