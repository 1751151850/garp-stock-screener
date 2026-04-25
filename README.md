# GARP Stock Screener

A universal AI prompt for **Growth-At-Reasonable-Price (GARP)** stock screening. Works with any AI coding assistant or chat tool.

## What It Does

Instructs an AI to act as an equity research analyst and screen 8-10 stocks using a 9-criterion framework:

1. **High Growth Inflection** — 30%+ YoY revenue/EPS acceleration in recent quarters
2. **High-Value Sector** — AI, semiconductors, robotics, quantum computing, EVs, etc.
3. **Reasonable Valuation** — TTM PE &le; 20x, Forward PE &le; 10x, PEG &lt; 1
4. **Market Cap Sweet Spot** — $5B - $100B
5. **Earnings Trajectory** — At or near all-time highs
6. **Market Priority** — US &gt; HK &gt; A-shares
7. **Competitive Moat** — Technology, scale, network effects, or switching costs
8. **Ownership Concentration** — Institutional + top 10 holders &ge; 70%
9. **Future Growth Visibility** — Clear 1-2 year growth catalysts

Output includes a ranked summary table and detailed per-stock analysis with sourced data.

## Quick Start

The core prompt is in **[`prompt.md`](prompt.md)**. Pick your tool and follow the setup below.

### Codewiz

```bash
# Copy with frontmatter
mkdir -p ~/.config/codewiz/skills/stock-screener
cp examples/codewiz/SKILL.md ~/.config/codewiz/skills/stock-screener/SKILL.md
# Then append the prompt content
cat prompt.md >> ~/.config/codewiz/skills/stock-screener/SKILL.md
```

Then say: **"帮我筛选股票"**

### Cursor

```bash
# Copy with frontmatter to your project
mkdir -p .cursor/rules
cp examples/cursor/stock-screener.mdc .cursor/rules/stock-screener.mdc
# Then append the prompt content
cat prompt.md >> .cursor/rules/stock-screener.mdc
```

Then say: **"帮我筛选股票"** or reference `@rules stock-screener`

### Claude Code

```bash
# Copy to project root
cp examples/claude-code/CLAUDE.md ./CLAUDE.md
# Then append the prompt content
cat prompt.md >> ./CLAUDE.md
```

### Codex (OpenAI)

```bash
# Copy to project root
cp examples/codex/AGENTS.md ./AGENTS.md
# Then append the prompt content
cat prompt.md >> ./AGENTS.md
```

### ChatGPT / Claude.ai / Any Chat UI

Just paste the contents of `prompt.md` into the conversation, then ask it to screen stocks.

## PDF Report Generation

After the AI generates an HTML report, convert it to PDF:

```bash
# Install dependencies (one-time)
pip install playwright
python -m playwright install chromium

# Generate PDF
python scripts/generate_pdf.py report.html report.pdf
```

## Project Structure

```
garp-stock-screener/
├── README.md              # This file
├── LICENSE                # MIT License
├── prompt.md              # The universal prompt (core content)
├── examples/
│   ├── codewiz/
│   │   └── SKILL.md       # Codewiz skill template (add prompt.md content)
│   ├── cursor/
│   │   └── stock-screener.mdc  # Cursor rules template
│   ├── claude-code/
│   │   └── CLAUDE.md      # Claude Code template
│   └── codex/
│       └── AGENTS.md      # Codex template
└── scripts/
    └── generate_pdf.py    # HTML → PDF converter (Playwright)
```

## Customization

The prompt is designed to be modified. Common customizations:

- **Sector focus**: Edit Criterion 2 to limit to specific sectors
- **Valuation thresholds**: Adjust PE/PEG limits in Criterion 3
- **Market cap range**: Change the $5B-$100B range in Criterion 4
- **Market scope**: Remove HK/A-shares if you only want US stocks
- **Output language**: Change Guideline 7 to output in English instead of Chinese

## Disclaimer

This tool generates AI-assisted stock analysis for **educational and research purposes only**. It is NOT financial advice. Always do your own due diligence before making investment decisions. The AI may produce inaccurate data — verify all figures independently.

## License

MIT
