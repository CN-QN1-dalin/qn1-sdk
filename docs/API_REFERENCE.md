# API 参考

## `qn1.auto()`

自动检测模型、后端、最优引擎配置。

```python
from qn1 import auto

engine = auto(
    model: str = None,          # 模型名称或路径，None=自动检测
    backend: str = None,        # mlx | gguf | torch，None=自动
    preset: str = "balanced",   # lite | balanced | performance
) -> Engine
```

**返回**: `Engine` 对象，包含 `generate()` 方法。

---

## `qn1.monkey_patch()`

零训练替换模型注意力机制（MLX 后端）。

```python
from qn1 import monkey_patch

monkey_patch(
    model,              # MLX 模型对象
    preset="balanced",  # lite | balanced | performance
    config: dict = None # 自定义配置（覆盖 preset）
)
```

**Preset 说明**:

| Preset | 内存节省 | 适用场景 |
|--------|---------|---------|
| lite | 最大 | 端侧部署、长上下文 |
| balanced | 均衡 | 通用推理 |
| performance | 最小 | 追求最高速度 |

---

## `qn1.create_llama_engine()`

创建 GGUF 后端引擎（跨平台 CPU）。

```python
from qn1 import create_llama_engine

engine = create_llama_engine(
    model_path: str,          # .gguf 文件路径
    n_ctx: int = 2048,        # 上下文长度
    use_ring: bool = True,    # 启用 RingBuffer
) -> Engine
```

---

## `qn1.create_torch_engine()`

创建 PyTorch 后端引擎（GPU 推理）。

```python
from qn1 import create_torch_engine

engine = create_torch_engine(
    model_name: str,          # HuggingFace 模型名
    device: str = "auto",     # cuda | mps | cpu
    use_hetero: bool = True,  # 启用异构引擎
) -> Engine
```

---

## `Engine.generate()`

执行文本生成。

```python
engine.generate(
    prompt: str,                     # 输入提示词
    max_tokens: int = 512,           # 最大生成 token 数
    temperature: float = 0.7,        # 采样温度
    top_p: float = 0.9,              # nucleus 采样
    stream: bool = False,            # 流式输出
) -> str | Generator[str]
```

---

## 许可证管理

```python
from qn1 import activate, LicenseStatus

# 激活
activate("QN1-XXXX-XXXX-XXXX")

# 查询状态
status = LicenseStatus()
print(status.trial_remaining)  # 试用剩余次数
print(status.is_expired)       # 是否过期
```

### CLI

```bash
# 查看状态
qn1-trial --status

# 激活许可证
qn1-license --activate QN1-XXXX-XXXX-XXXX
```
