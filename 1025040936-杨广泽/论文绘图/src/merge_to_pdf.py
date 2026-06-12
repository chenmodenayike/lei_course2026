"""
将 output 目录下全部配图（含 HTML 交互图）整合为一份 PDF。
"""
import glob
import os
import re
import tempfile
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR.parent / "output"
PDF_PATH = OUTPUT_DIR / "全部论文配图合集.pdf"
TEMP_DIR = OUTPUT_DIR / "_html_snapshots"


def natural_sort_key(path: Path) -> tuple:
    """按 fig 编号排序"""
    m = re.search(r"fig(\d+)", path.name)
    num = int(m.group(1)) if m else 999
    sub = 0
    if "图4.1" in path.name:
        sub = 1
    elif "图4.2" in path.name:
        sub = 2
    elif "图4.3" in path.name:
        sub = 3
    return (num, sub, path.suffix != ".png", path.name)


def html_to_png(html_path: Path, png_path: Path) -> None:
    file_url = html_path.resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 960, "height": 560})
        page.goto(file_url, wait_until="networkidle", timeout=60000)
        page.wait_for_timeout(1500)
        container = page.locator(".chart-container")
        container.screenshot(path=str(png_path))
        browser.close()


def collect_image_paths() -> list[Path]:
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    # HTML 先转 PNG
    for html_file in sorted(OUTPUT_DIR.glob("*.html")):
        png_out = TEMP_DIR / (html_file.stem + ".png")
        print(f"HTML 截图: {html_file.name}")
        html_to_png(html_file, png_out)

    images: list[Path] = []
    for png in OUTPUT_DIR.glob("fig*.png"):
        images.append(png)
    for png in sorted(TEMP_DIR.glob("*.png")):
        images.append(png)

    # 排除重复：只用 fig10 的 PNG，不用 EPS
    images = [p for p in images if p.suffix.lower() == ".png"]
    images.sort(key=natural_sort_key)
    return images


def images_to_pdf(image_paths: list[Path], pdf_path: Path) -> None:
    if not image_paths:
        raise FileNotFoundError("未找到可合并的图片文件")

    rgb_images: list[Image.Image] = []
    for path in image_paths:
        print(f"加入 PDF: {path.name}")
        img = Image.open(path)
        if img.mode in ("RGBA", "P"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode == "P":
                img = img.convert("RGBA")
            bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = bg
        else:
            img = img.convert("RGB")
        rgb_images.append(img)

    first, *rest = rgb_images
    first.save(
        pdf_path,
        "PDF",
        resolution=150.0,
        save_all=True,
        append_images=rest,
    )
    for img in rgb_images:
        img.close()


def main():
    image_paths = collect_image_paths()
    images_to_pdf(image_paths, PDF_PATH)
    print(f"\n已生成: {PDF_PATH}")
    print(f"共 {len(image_paths)} 页")


if __name__ == "__main__":
    main()
