---
name: agent-setup
description: >-
  帮用户在自己的 Agent（Grok Bot、Muse、Dot、Hermes、OpenClaw 等）里装好汽车选题监控 Bot：
  先问清品牌和价位带、常看平台、播报时间，再生成一段定制好的安装消息让用户发给 Bot。
  用户说「帮我配一个汽车选题 Bot」「帮我装汽车选题监控」「生成发给 Bot 的安装话术」时使用。
---
# 汽车选题监控装机助手

你在用户的电脑上（Claude Code、Codex 等），产出是一段消息，用户复制给 Bot，Bot 照 `AGENTS.md` 自己装。

## 1. 问清楚（一次一个问题）

1. 用在哪个 Agent：Grok Bot / Muse / Dot / Hermes / OpenClaw / 其他
2. 品牌和价位带：主要盯哪些品牌、什么价位区间（决定竞品名单和线索范围）
3. 常看平台：抖音 / 小红书 / 视频号 / 公众号 / 汽车之家 / 懂车帝，哪几个是重点
4. 播报时间：默认早报 08:30、午报 12:30、晚报 17:00，要不要改
5. 要不要开运行日志（可选）：轻量 / 标准 / 完整 / 不开，拿不准就建议先开轻量

## 2. 本地验证（不花钱）

```bash
git clone https://github.com/mingginwan/auto-newmedia-agents.git /tmp/auto-newmedia-agents
python3 /tmp/auto-newmedia-agents/tests/test_dry_run.py
```

全部 OK 再继续。汽车选题监控不需要 API Key。

## 3. 生成安装消息

模板：

```text
读 https://github.com/mingginwan/auto-newmedia-agents 的 AGENTS.md，按它把你自己装成 auto-topic-monitor（汽车选题监控）Bot。
一次只问我一个问题。下面这些我已经想好了，直接用，不用再问：
- 工作目录：/workspace/auto-topic-monitor
- 品牌和价位带：<...>
- 常看平台：<...>
- 播报时间：<...>
- 运行日志：<不开 / 轻量 / 标准 / 完整>
不需要 API Key；抖音、小红书用我自己已登录的浏览器。
```

## 4. 交付

- 给用户：安装消息（可直接复制）+ `bots/auto-topic-monitor/check.md` 验收清单
- 提醒用户：第一次先手动跑一遍，满意后再设成例程；发布、投放、删除这些动作始终由用户决定
