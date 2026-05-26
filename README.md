# QN1 — 念动幻化

**AI inference without limits. Consumer hardware. Production speed.**

[![PR](https://img.shields.io/badge/llama.cpp-PR%20%2323743-blue)](https://github.com/ggml-org/llama.cpp/pull/23743)
[![License](https://img.shields.io/badge/license-MIT%20%2B%20Commercial-blue)](LICENSE)

---

## What We Do

QN1 optimizes LLM inference on consumer devices (MacBooks, phones, edge) through **attention architecture innovation** — not model compression, not cloud offload.

Our core insight: the bottleneck isn't compute, it's **memory architecture**. Standard attention is O(n) — every new token attends to all previous tokens. We make it O(1).

## Open Source Projects

| Repo | Description | Stars |
|------|-------------|-------|
| [ringbuffer](https://github.com/CN-QN1-dalin/ringbuffer) | O(1) KV Cache for llama.cpp — one-line API | ⭐ |
| [ultra-infer](https://github.com/CN-QN1-dalin/ultra-infer) | DeepSeek V4 Flash engine — 284B on 16GB | ⭐ |
| [benchmarks](https://github.com/CN-QN1-dalin/benchmarks) | Reproducible performance data | ⭐ |
| [llama.cpp fork](https://github.com/CN-QN1-dalin/llama.cpp) | Upstream PR with RingBuffer | ⭐ |

## RingBuffer: One Line, O(1)

```cpp
llama_memory_set_n_kv_max(mem, 16);  // That's it. O(1) from here.
```

| Context | Standard | RingBuffer | Speedup |
|---------|----------|------------|---------|
| 4K      | 8.3 t/s  | 10.5 t/s   | 1.27x   |
| 64K     | ~2 t/s   | ~10 t/s    | ~5x     |

→ [Full benchmarks](https://github.com/CN-QN1-dalin/benchmarks)  
→ [llama.cpp PR #23743](https://github.com/ggml-org/llama.cpp/pull/23743)

## QN1 Pro

The open-source RingBuffer gives you O(1) decode. QN1 Pro adds **semantic retrieval** so you don't lose context:

| Feature | RingBuffer (free) | QN1 Pro |
|---------|:---:|:---:|
| O(1) decode | ✅ | ✅ |
| Semantic retrieval | ❌ | ✅ SignalField |
| KV compression | ❌ | ✅ 归元SSM (99%) |
| Fast adaptation | ❌ | ✅ 灵芽 (36% < LoRA) |
| Multi-backend | llama.cpp | MLX + PyTorch + llama.cpp |

→ [qn1.ai](https://qn1.ai)

## Architecture

```
┌─────────────────────────────────────────┐
│              QN1 Engine                  │
├─────────────────────────────────────────┤
│  RingBuffer (free)     O(1) KV window   │
│  SignalField (Pro)     Semantic search  │
│  归元SSM (Pro)         KV compression   │
│  灵芽 (Pro)            Fast adaptation  │
└─────────────────────────────────────────┘
```

## Team

**CN_SJZ-QN1-大林** — Founder. Reverse-engineered DeepSeek V4 Flash (284B MoE). Built the first O(1) KV cache integration for llama.cpp. Located in Shijiazhuang, China.

→ [GitHub](https://github.com/CN-QN1-dalin)

## License

- Open source components: MIT
- QN1 Pro SDK: Commercial license
- Contact: contact@qn1.ai

---

> **一行代码，O(1)解码。**
