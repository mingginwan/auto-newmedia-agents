<div align="center">

<img src="assets/icon.png" width="112" alt="auto-newmedia-agents">

# auto-newmedia-agents

### 汽车新媒体每日选题监控，交给 Agent 每天跑。

**每天盯新车、竞品、政策、用户声音、爆款内容五类线索，三次分级播报；刷到好内容丢一个链接，自动拆解归档进知识库。**<br>
这些活每天都要做、步骤固定，最适合固化成 SOP 交给 Agent。<br>
新建一个 Bot，发一句话，它会读这个仓库、问你几个问题，然后把自己装好。

[![Stars](https://img.shields.io/github/stars/mingginwan/auto-newmedia-agents?style=flat&color=111111&cacheSeconds=3600)](https://github.com/mingginwan/auto-newmedia-agents/stargazers) [![License](https://img.shields.io/badge/license-MIT-111111)](LICENSE)

**[三分钟上手](#三分钟上手)** &nbsp;·&nbsp; **[这个 Bot](#这个-bot)** &nbsp;·&nbsp; **[发给 Bot 的一句话](bootstrap.md)** &nbsp;·&nbsp; **[AGENTS.md](AGENTS.md)** &nbsp;·&nbsp; [English](README.md) · **简体中文**

</div>

<br>

这个仓库是给汽车新媒体团队用的一套岗位 SOP 和技能包。它把每天的选题会变成 Agent 例程：采集线索、按 A/B/C 分级、推一份手机能读的播报、维护选题台账，再把对标内容拆解归档进知识库。

**整套系统只守三条规矩：**

1. **脚本做确定的事**：采集、去重、打分、记台账，结果可复现、可回放，不靠模型「感觉」。
2. **Agent 做判断**：读采集结果去分析、提取、核实、写播报。拿不到数据就直说，不编。
3. **你做决定**：Agent 只推结论；花钱、对外发送、删除都要你点头。你每次纠正它，都变成一条新规矩写回技能里。

## 这个 Bot

| Bot | 你做什么 | 它做什么 |
|---|---|---|
| [汽车选题监控](bots/auto-topic-monitor/README.md) | 什么都不用做（可选：给品牌和价位带） | 每天早中晚三次播报汽车行业值得拍的新鲜事：新车、竞品动作、政策、用户声音、爆款内容。按 A/B/C 分级，维护选题台账，把对标内容拆解归档进知识库。用公开网页和你已登录的浏览器，不需要 API Key。 |

## 在哪个 Agent 里用

**Grok Bot、Muse、Dot、Hermes、OpenClaw** 都可以，Claude Code、Codex 也行。[AGENTS.md](AGENTS.md) 里写的是通用步骤，各家只是把「例程（定时任务）」「保险库」叫法不同。

## 三分钟上手

1. 在你的 Agent 里新建一个 Bot。
2. 把 [bootstrap.md](bootstrap.md) 里对应的那句话发给它，比如：

   ```text
   读 https://github.com/mingginwan/auto-newmedia-agents 的 AGENTS.md，按它把你自己装成 auto-topic-monitor（汽车选题监控）Bot。一次只问我一个问题。
   ```

3. 它会先手动跑一遍给你看，你满意了再设成例程。

整个过程就是「**做一次 → 改到满意 → 存成技能 → 设成例程**」。

## 仓库里有什么

```
auto-newmedia-agents/
├── AGENTS.md               给 Agent 的安装说明
├── bootstrap.md            发给 Bot 的一句话
├── assets/icon.png
├── bots/auto-topic-monitor/
│   ├── README.md           完整 SOP
│   ├── job.md              岗位说明
│   ├── routines.md         例程表
│   ├── check.md            验收清单
│   ├── skills/auto-topic-monitor/SKILL.md
│   ├── skills/douyin-comments/   可选：抓完整抖音评论区
│   └── templates/          播报、内容拆解、选题台账模板
├── lib/runlog/             可选：运行日志
├── templates/              通用台账格式
└── tests/                  不需要 Key 的演练测试
```

## 数据从哪来

汽车选题监控用公开网页 + 你已登录的浏览器：品牌官网、汽车之家、懂车帝、车质网、工信部等公开页面，抖音/小红书用你自己的登录态读取。**不需要 API Key，也不需要任何付费数据服务。** 可选的 `douyin-comments` 技能同样在你自己的浏览器里运行。

## 可选：运行日志

想让系统更稳、出了问题能查到原因，可以加装 [运行日志模块](lib/runlog/README.md)。它记录每个例程有没有跑、成没成功、你批准过什么、规则什么时候改过。默认关闭，只在本地写文件。

## 许可证

MIT。本项目改编自 Pluviobyte 的 [saas-growth-agents](https://github.com/Pluviobyte/saas-growth-agents)，原作者信息见 [NOTICE.md](NOTICE.md)。
