<div align="center">

<img src="assets/icon.png" width="112" alt="auto-newmedia-agents">

# auto-newmedia-agents

### 汽车新媒体每日选题监控，交给 Agent 每天跑。

**每天盯新车、竞品、政策、用户声音、爆款内容五类线索，三次分级播报；刷到好内容丢一个链接，自动拆解归档进知识库。**<br>
这些活每天都要做、步骤固定，最适合固化成 SOP 交给 Agent。<br>
新建一个 Bot，发一句话，它会读这个仓库、问你几个问题，然后把自己装好。

[![Stars](https://img.shields.io/github/stars/mingginwan/auto-newmedia-agents?style=flat&color=111111&cacheSeconds=3600)](https://github.com/mingginwan/auto-newmedia-agents/stargazers) [![License](https://img.shields.io/badge/license-MIT-111111)](LICENSE) [![Python](https://img.shields.io/badge/python_3-stdlib_only-111111?logo=python&logoColor=white)](lib/aisa/client.py)<br>
[![Grok Bot](https://img.shields.io/badge/Grok_Bot-推荐-000000?logo=x&logoColor=white)](https://grok.com/refer/bot?code=NASHTX8NMYH3) ![Muse](https://img.shields.io/badge/Muse-333333) ![Dot](https://img.shields.io/badge/Dot-333333) ![Hermes](https://img.shields.io/badge/Hermes-333333) ![OpenClaw](https://img.shields.io/badge/OpenClaw-333333) ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?logo=claude&logoColor=white) ![Codex](https://img.shields.io/badge/Codex-111111)

**[三分钟上手](#三分钟上手)** &nbsp;·&nbsp; **[Bot 列表](#bot-列表)** &nbsp;·&nbsp; **[发给 Bot 的一句话](bootstrap.md)** &nbsp;·&nbsp; **[AGENTS.md](AGENTS.md)** &nbsp;·&nbsp; **[Grok Bot 免费 14 天](https://grok.com/refer/bot?code=NASHTX8NMYH3)** &nbsp;·&nbsp; [English](README.md) · **简体中文**

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/flow-dark.zh-CN.svg">
  <img alt="数据流：数据源进入汽车选题监控流水线（新车、竞品、政策、用户声音、爆款内容五类线索），脚本只做采集、去重、记账这些确定的事；Agent 负责分析、提取、核实、写播报，再推送给你做决定。状态写进文件和账本，每次开工先读；花钱、发送、删除都要你点头。" src="assets/flow-light.zh-CN.svg" width="900">
</picture>

</div>

<br>

这个 Fork 面向汽车新媒体团队：主推汽车选题监控，把每日选题会前的线索收集、分级播报和爆款拆解归档交给 Agent。原版出海增长 Bot 保留在下面，供参考。任何能跑终端命令、能存长期指令的 Agent 都能用。

> **从 douyin-comments 来的？** 抖音评论区 skill 现在放在社媒分析包里的 [`bots/social-kb/douyin-comments/`](bots/social-kb/douyin-comments/SKILL.md)，用法和以前一样。重新安装方法见[社媒分析包](bots/social-kb/README.zh-CN.md#以前装过-douyin-comments)。

**这套系统只有三条原则：**

1. **脚本做确定的事**：采集、去重、打分、记台账，结果可复现、可回放，不靠模型「感觉」。
2. **Agent 做判断**：读脚本给的材料去分析、提取、核实、写播报。拿不到数据就直说，不编。
3. **你做决定**：Agent 只推结论；花钱、对外发送、删除都要你点头。你每次纠正它，都变成一条新规矩写回技能里。

## Bot 列表

### 主推：汽车选题监控

| Bot | 你做什么 | 它做什么 |
|---|---|---|
| [汽车选题监控](bots/auto-topic-monitor/README.md) | 什么都不用做（可选：给品牌和价位带） | 每天早中晚三次播报汽车行业值得拍的新鲜事：新车、竞品动作、政策、用户声音、爆款内容。按 A/B/C 分级，维护选题台账，把对标内容拆解归档进知识库。**用公开网页和你已登录的浏览器，不要求 AIsa Key。** |

### 原版出海 Bot（保留参考）

| Bot | 你做什么 | 它做什么 |
|---|---|---|
| [新词监控](bots/newterm/job.md) | 什么都不用做 | 每天早中晚三次播报新出现、可被搜索的词：AI 新产品、新模型、新梗、新模板。词源包括 Google Trends、竞品 sitemap、导航站新上架、Product Hunt、GitHub Trending、Reddit、TikTok |
| [出海站点运营](bots/site-ops/job.md) | 给词、给产品 | 按词找出所有在抢这个词的站，查它们的 DR 和外链，每天盯自有站指标，按规则提交免费导航站，全部记台账 |
| [社媒分析包](bots/social-kb/README.zh-CN.md) | 刷到好内容，丢一个链接 | 取原文（X、抖音、小红书、YouTube、公众号、网页）→ 整理 → 对照你的工作流提取「能改进你 SOP 的部分」→ 按主题存进知识库；抖音还能抓完整评论区，看用户都在问什么 |

另外附带一个和出海无关的 [交易雷达](extras/trade-radar/job.md)：盯价格异动和突发事件，分析后推送，**只分析、不下单**。

## 在哪个 Agent 里用

**Grok Bot、Muse、Dot、Hermes、OpenClaw** 都可以，Claude Code、Codex 也行。[AGENTS.md](AGENTS.md) 里写的是通用步骤，各家只是把「例程（定时任务）」「保险库」叫法不同。

**作者推荐 Grok Bot。** 它自带云电脑、保险库、技能和例程，这几套 SOP 最早就是在 Grok Bot 上跑出来的，装好后可以 7×24 小时按例程工作。

> 还没有 Grok Bot？用作者的邀请链接注册可以免费用 14 天：**https://grok.com/refer/bot?code=NASHTX8NMYH3**
> （这是推荐链接，作者会因此获得奖励；活动规则以 Grok 官方页面为准。）

## 三分钟上手

1. 在你的 Agent 里新建一个 Bot。
2. 把 [bootstrap.md](bootstrap.md) 里对应的那句话发给它，比如：

   ```text
   读 https://github.com/mingginwan/auto-newmedia-agents 的 AGENTS.md，按它把你自己装成 auto-topic-monitor（汽车选题监控）Bot。一次只问我一个问题。
   ```

3. 汽车选题监控默认用公开网页和你已登录的浏览器，不用 AIsa Key 就能开跑。它会先手动跑一遍给你看，你满意了再设成例程。原版出海 Bot 仍使用 [AIsa](https://go.aisa.one/rain)，见下方说明。

整个过程就是「**做一次 → 改到满意 → 存成技能 → 设成例程**」。

## 数据从哪来

### 汽车选题监控（本 Fork 主推）

公开网页 + 你已登录的浏览器：品牌官网、汽车之家、懂车帝、车质网、工信部等公开页面，抖音/小红书用你自己的登录态读取。**不要求 AIsa Key，可以先零 API 成本跑起来。**

### 原版出海 Bot（保留参考）

所有外部数据走 [AIsa](https://go.aisa.one/rain)：一个 Key 调几千个接口，按次计费，支持 MCP。这里用到的有：

- **SEO**：DataForSEO 的 SERP 和 Google Trends，Ahrefs
- **社交**：Twitter，TikHub（抖音、小红书），DataForSEO YouTube（字幕、视频信息）
- **网页**：Firecrawl、Tavily
- **交易雷达**：CoinGecko、Financial（美股）、Polymarket、FRED、Perplexity

每个接口对应 [lib/aisa/sources.py](lib/aisa/sources.py) 里的一个函数，路径和参数按 AIsa 官方 OpenAPI 核对过。
每次请求都带最高价，超价直接拒绝；不确定价格就先加 `--quote` 问价，问价不花钱。

> AIsa 链接是作者的邀请链接。抖音评论区模块不走 AIsa，在你自己已登录的浏览器里运行，不花钱。

## 可选：运行日志

想让系统更稳，出了问题能查到原因，可以加装 [运行日志](lib/runlog/README.md)。它会记下每次例程跑了没有、成没成、花了多少，你批准过什么，规则什么时候、为什么被改过。每晚体检时，会把失败、卡住、漏跑和花费异常列出来。

> ⚠️ **开了会多消耗 Bot 的额度，所以默认不开，装机时 Bot 会问你要不要开。** 分三档：轻量（只记审批和规则变更，几乎不耗额度）、标准（再加每次例程的运行记录）、完整（再加每晚体检、每周归档）。日志只在本地写文件，AIsa 不会多花钱。

## 仓库结构

```
auto-newmedia-agents/
├── AGENTS.md               给 Agent 的安装步骤
├── bootstrap.md            发给 Bot 的一句话
├── lib/aisa/               AIsa 调用层：client.py（标准库）、sources.py（各数据源）、aisa_cli.py（命令行）
├── lib/runlog/             可选：运行日志、审批记录、规则变更、每晚体检（会多耗 Bot 额度）
├── bots/
│   ├── newterm/            新词监控：job.md · routines.md · check.md · pipeline/ · skills/ · install.sh
│   ├── site-ops/           出海站点运营：job.md · routines.md · check.md · scripts/ · skills/
│   ├── social-kb/          社媒分析包：README.zh-CN.md · job.md · routines.md · check.md · scripts/ · douyin-comments/
│   └── auto-topic-monitor/ 汽车选题监控：README.md · job.md · routines.md · check.md · skills/ · templates/
├── extras/trade-radar/     交易雷达（附带）
├── skills/agent-setup/     给 Claude Code / Codex 用：问清需求，生成发给 Bot 的定制安装消息
├── templates/              账本格式
└── tests/                  不需要 Key 的演练测试（样例数据都是虚构的）
```

每个 Bot 目录都一样：`job.md` 是岗位说明，`routines.md` 是例程，`check.md` 是装好后的验收清单。

## 不用 Key 先试一下

```bash
git clone https://github.com/mingginwan/auto-newmedia-agents.git && cd auto-newmedia-agents
python3 tests/test_dry_run.py                                        # 全部演练
AISA_DRY_RUN=1 python3 bots/site-ops/scripts/serp_sites.py "ai video generator"
```

## 边界

- **不绕过验证码，不代填账号密码，不替你注册账号。** 遇到就停下交给你。
- **导航站提交只走免费、不要求互链的站**，付费和互链的一律跳过并记原因。
- **这几类做法不在本仓库范围内**：
  - 浏览器插件批处理：许可证不明
  - 共享账号抓取：违反平台条款
  - 博客评论外链批量发布：属于垃圾外链
  - 真实的站点池、提交记录和词库：属于个人数据
- 别人的内容只做学习记录，不搬运发布。抓取请控制频率，遵守各平台的用户协议。
- 交易雷达仓库里没有任何下单代码，账本拒收仓位和订单字段。它的输出只是信息整理，不构成投资建议。

## 许可证

[MIT](LICENSE)。第三方服务和致谢见 [NOTICE.md](NOTICE.md)。
