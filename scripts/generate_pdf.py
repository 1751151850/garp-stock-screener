#!/usr/bin/env python3
"""
Convert a stock screener HTML report to PDF using Playwright (Chromium headless).

Usage:
    python generate_pdf.py input.html output.pdf

Requirements:
    pip install playwright
    python -m playwright install chromium
"""

import sys
import asyncio
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: playwright is not installed.")
    print("Run: pip install playwright && python -m playwright install chromium")
    sys.exit(1)


async def html_to_pdf(html_path: str, pdf_path: str) -> None:
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        print(f"Error: {html_file} not found")
        sys.exit(1)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"file://{html_file}", wait_until="networkidle")
        await page.pdf(
            path=pdf_path,
            format="A4",
            margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"},
            print_background=True,
        )
        await browser.close()

    print(f"PDF generated: {pdf_path}")


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.html> <output.pdf>")
        sys.exit(1)

    asyncio.run(html_to_pdf(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
