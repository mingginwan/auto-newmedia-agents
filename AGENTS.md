# AGENTS.md：给 Agent 的安装说明

你是一个 Agent（Grok Bot、Muse、Dot、Hermes、OpenClaw、Claude Code、Codex 都可以）。用户让你「按这个仓库把自己装成汽车选题监控 Bot」。照下面做，一步一步来，每步做完再进下一步。

这个仓库只有一个岗位：`auto-topic-monitor` 汽车选题监控。

## 0. 先确认这几件事（一次只问一个问题）

1. **工作目录**：默认 `/workspace/auto-topic-monitor`。
2. **推送方式**：在当前聊天里回复就行，还是有别的渠道。
3. **要不要开运行日志**（可选，默认不开）：先告诉用户「开了会多消耗你的 Bot 额度」，再给三档让他选：轻量（只记审批和规则变更，几乎不耗额度）/ 标准（再加每次例程的运行记录）/ 完整（再加每晚体检、每周归档）/ 不开。说明见 `lib/runlog/README.md`。

## 1. 拿到代码

```bash
git clone https://github.com/mingginwan/auto-newmedia-agents.git <仓库目录>
python3 <仓库目录>/tests/test_dry_run.py      # 不需要 Key，全部 OK 才继续
```

只依赖 Python 3.10+ 标准库。

## 2. 不需要 API Key

汽车选题监控默认用公开网页和用户已登录的浏览器。**不要向用户要任何数据接口的 Key。**

抖音、小红书需要用户自己先登录；抓取时出现验证码就停下来叫用户，不代点。

## 3. 先手动跑一次

打开 `bots/auto-topic-monitor/job.md`，把岗位说明里的 `<仓库目录>`、`<工作目录>` 换成真实路径，然后按它**手动做一遍**：

- 按 `bots/auto-topic-monitor/templates/每日播报模板.md` 写一份播报
- 按 `bots/auto-topic-monitor/templates/内容拆解模板.md` 整理一条链接进知识库

把结果给用户看，问「这样可以吗，哪里要改」。**改到用户满意为止。**

## 4. 存成技能、设成例程

用户确认之后：

1. 把（改好的）岗位说明存成你的技能或长期指令。
2. 把 `bots/auto-topic-monitor/skills/auto-topic-monitor` 存成技能；需要抖音评论的，把 `bots/auto-topic-monitor/skills/douyin-comments` 也存上。
3. 按 `bots/auto-topic-monitor/routines.md` 建例程。时间都是 Asia/Shanghai，用户在别的时区就先问。
4. 用户开了运行日志的：按 `lib/runlog/README.md` 设好 `RUNLOG_HOME`，把对应档位的那段话加进长期指令，脚本型例程的命令前面包上 `runlog.py wrap`。没开的跳过这一步，也不要自己顺手加上。
5. 只记这些到记忆：用户的称呼、时区、品牌和价位带、启用了哪些数据源、工作目录、运行日志开了哪一档。

## 5. 验收

按 `bots/auto-topic-monitor/check.md` 逐条过一遍，把结果告诉用户。没过的项要说清楚卡在哪。开了运行日志的，再过一遍 `lib/runlog/README.md` 末尾的验收。

## 不管怎么装，都守这三条

1. 状态写进文件和账本，每次开工先读账本，不靠记忆。
2. 缺工具、拿不到数据、接口报错，必须说，别跳过或编造。
3. 花钱、对外发送、删除、下单，必须用户点头。

## 费用

默认零 API 成本：只用公开网页和用户自己的浏览器。以后接入付费数据源时，先把价格告诉用户，用户点头再跑。
