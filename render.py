"""Render poster.html to entry.png at exactly 1024x1024 with headless Chromium.

Local regeneration helper only; it is NOT run by the grader (main.py only
copies the bundled entry.png). Finds a Chromium binary: headless_shell from
Playwright's cache, a system chromium/chrome, or google-chrome.
"""
import glob
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def find_chromium():
    for name in ("chromium", "chromium-browser", "google-chrome",
                 "google-chrome-stable", "headless_shell"):
        path = shutil.which(name)
        if path:
            return path
    patterns = [
        os.path.expanduser("~/.cache/ms-playwright/chromium_headless_shell-*/chrome-linux/headless_shell"),
        os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux/chrome"),
    ]
    for pattern in patterns:
        for path in sorted(glob.glob(pattern)):
            if os.path.isfile(path) and os.access(path, os.X_OK):
                return path
    return None


def main() -> int:
    chrome = find_chromium()
    if not chrome:
        print("no Chromium binary found", file=sys.stderr)
        return 1
    src = os.path.join(HERE, "poster.html")
    dst = os.path.join(HERE, "entry.png")
    cmd = [
        chrome, "--headless", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars", "--force-device-scale-factor=1",
        "--window-size=1024,1024",
        "--screenshot=" + dst,
        "file://" + src,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        return result.returncode
    print("wrote", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
