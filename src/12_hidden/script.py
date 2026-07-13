#!/usr/bin/env python3

import hashlib
import json
import os
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# Root directory to crawl
BASE_URL = "http://localhost:8080/.hidden/"

# Output file
OUTPUT_FILE = "readmes.json"

session = requests.Session()
visited = set()

# Maps SHA256 -> README content
contents = {}

# Maps README path -> SHA256
paths = {}


def save_readme(url):
    """Download a README and store it only once."""
    try:
        r = session.get(url, timeout=10)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"[-] Failed to fetch {url}: {e}")
        return

    text = r.text
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()

    parsed = urlparse(url)

    # Save mapping from path -> content hash
    paths[parsed.path] = digest

    # Save unique content only once
    if digest not in contents:
        contents[digest] = text
        print(f"[+] New README ({digest[:8]})")
    else:
        print(f"[=] Duplicate README ({digest[:8]})")


def crawl(url):
    """Recursively crawl directory listings."""
    if url in visited:
        return

    visited.add(url)
    print(f"[*] Crawling {url}")

    try:
        r = session.get(url, timeout=10)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"[-] Failed to crawl {url}: {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")

    for a in soup.find_all("a"):
        href = a.get("href")

        if not href or href == "../":
            continue

        full_url = urljoin(url, href)

        if href.endswith("/"):
            crawl(full_url)
        elif href.upper() == "README":
            save_readme(full_url)


def main():
    crawl(BASE_URL)

    data = {
        "stats": {
            "directories_visited": len(visited),
            "readmes_found": len(paths),
            "unique_readmes": len(contents),
        },
        "paths": paths,
        "contents": contents,
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("\nDone!")
    print(f"Directories visited : {len(visited)}")
    print(f"README files found  : {len(paths)}")
    print(f"Unique README files : {len(contents)}")
    print(f"Saved to            : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()