# GARP Stock Screener

一个通用的 AI Prompt，用于 **GARP（Growth-At-Reasonable-Price，合理价格成长股）** 选股策略。适用于任何 AI 编程助手或对话工具。

## 功能概述

指导 AI 扮演权益研究分析师，通过多维框架筛选 8-10 只股票：

### 筛选维度

1. **增长拐点** — 最近 1-3 个季度营收/EPS 同比加速 30%+，需标明拐点起始时间和拐点前后状态对比
2. **高价值赛道** — AI、半导体、机器人、量子计算、电动车等结构性增长行业
3. **合理估值** — 同时列出静态 PE、TTM PE、Forward PE 三种市盈率，每个标注计算基础
4. **市值区间** — $5B - $100B 最佳
5. **业绩轨迹** — 营收/EPS 处于或接近历史最高
6. **市场优先级** — 美股 > 港股 > A 股
7. **竞争壁垒** — 技术、规模、网络效应、转换成本或监管壁垒
8. **筹码集中度** — 机构 + 前十大股东持股 >= 70%
9. **未来增长可见性** — 基于在手订单、产能扩张、公司指引等硬数据推算 1-2 年增长

### 新增分析板块

- **行业分析** — 每个涉及行业的规模、驱动力、竞争格局、估值水平、风险
- **同行业对比** — 横向对比表格，找出"同样增速谁更便宜"
- **安全边际** — 最大预期回撤、下行逻辑推导（估值底/盈利下修/历史回撤/系统性风险）、买入区间
- **收益空间** — 12/24 个月目标价推导、风险收益比、敏感性分析

### 输出质量保障

- 每个财务指标必须标注来源财报和时间
- 每只股票按统一完整模板输出，后面排名的不允许缩水
- 所有数据附带来源 URL 和日期

## 快速开始

核心 prompt 在 **[`prompt.md`](prompt.md)** 中。选择你的工具并按照下面的方式配置。

### Codewiz

```bash
# 复制带 frontmatter 的模板
mkdir -p ~/.config/codewiz/skills/stock-screener
cp examples/codewiz/SKILL.md ~/.config/codewiz/skills/stock-screener/SKILL.md
# 追加 prompt 内容
cat prompt.md >> ~/.config/codewiz/skills/stock-screener/SKILL.md
```

然后说：**"帮我筛选股票"**

### Cursor

```bash
# 复制带 frontmatter 的模板到项目中
mkdir -p .cursor/rules
cp examples/cursor/stock-screener.mdc .cursor/rules/stock-screener.mdc
# 追加 prompt 内容
cat prompt.md >> .cursor/rules/stock-screener.mdc
```

然后说：**"帮我筛选股票"** 或引用 `@rules stock-screener`

### Claude Code

```bash
# 复制到项目根目录
cp examples/claude-code/CLAUDE.md ./CLAUDE.md
# 追加 prompt 内容
cat prompt.md >> ./CLAUDE.md
```

### Codex (OpenAI)

```bash
# 复制到项目根目录
cp examples/codex/AGENTS.md ./AGENTS.md
# 追加 prompt 内容
cat prompt.md >> ./AGENTS.md
```

### ChatGPT / Claude.ai / 任何对话界面

直接将 `prompt.md` 的内容粘贴到对话中，然后要求它筛选股票即可。

## PDF 报告生成

AI 生成 HTML 报告后，可以转换为 PDF：

```bash
# 安装依赖（一次性）
pip install playwright
python -m playwright install chromium

# 生成 PDF
python scripts/generate_pdf.py report.html report.pdf
```

## 项目结构

```
garp-stock-screener/
├── README.md              # 本文件
├── LICENSE                # MIT 许可证
├── prompt.md              # 通用 prompt（核心内容）
├── examples/
│   ├── codewiz/
│   │   └── SKILL.md       # Codewiz skill 模板（需追加 prompt.md 内容）
│   ├── cursor/
│   │   └── stock-screener.mdc  # Cursor rules 模板
│   ├── claude-code/
│   │   └── CLAUDE.md      # Claude Code 模板
│   └── codex/
│       └── AGENTS.md      # Codex 模板
└── scripts/
    └── generate_pdf.py    # HTML → PDF 转换器（Playwright）
```

## 自定义

prompt 设计为可修改。常见自定义方式：

- **赛道聚焦**：编辑维度二，限制为特定赛道
- **估值阈值**：调整维度三中的 PE/PEG 限制
- **市值范围**：修改维度四中 $5B-$100B 的范围
- **市场范围**：如果只需要美股，移除港股/A 股
- **输出语言**：修改准则第 9 条，改为英文输出

## 免责声明

本工具生成的 AI 辅助股票分析仅用于 **教育和研究目的**。这不构成投资建议。在做出投资决策前，请始终进行独立的尽职调查。AI 可能生成不准确的数据 — 请独立验证所有数据。

## License

MIT
