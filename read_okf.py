#!/usr/bin/env python3
"""
Simple OKF Bundle Reader
Reads an OKF knowledge bundle and displays its concepts.
"""

import os
import yaml
import frontmatter
from pathlib import Path


def read_okf_bundle(bundle_path: str):
    """Read all concept documents from an OKF bundle."""
    concepts = []
    
    for md_file in Path(bundle_path).rglob("*.md"):
        # Skip index and log files for concept listing
        if md_file.name in ("index.md", "log.md"):
            continue
            
        with open(md_file, 'r') as f:
            post = frontmatter.load(f)
            
        concepts.append({
            "path": str(md_file.relative_to(bundle_path)),
            "type": post.metadata.get("type", "Unknown"),
            "title": post.metadata.get("title", md_file.stem),
            "description": post.metadata.get("description", ""),
            "status": post.metadata.get("status", "unknown"),
            "tags": post.metadata.get("tags", []),
            "resource": post.metadata.get("resource", ""),
        })
    
    return concepts


def display_bundle(bundle_path: str):
    """Display OKF bundle contents."""
    print(f"📦 OKF Bundle: {bundle_path}\n")
    
    # Read index if exists
    index_path = Path(bundle_path) / "index.md"
    if index_path.exists():
        with open(index_path, 'r') as f:
            print(f.read())
        print("\n" + "="*60 + "\n")
    
    # Read concepts
    concepts = read_okf_bundle(bundle_path)
    
    print(f"Found {len(concepts)} concept(s):\n")
    
    for c in concepts:
        status_icon = {"stable": "✅", "draft": "📝", "deprecated": "⚠️"}.get(c["status"], "❓")
        print(f"{status_icon} [{c['type']}] {c['title']}")
        print(f"   Path: {c['path']}")
        if c['description']:
            print(f"   Description: {c['description']}")
        if c['resource']:
            print(f"   Resource: {c['resource']}")
        if c['tags']:
            print(f"   Tags: {', '.join(c['tags'])}")
        print(f"   Status: {c['status']}")
        print()


if __name__ == "__main__":
    import sys
    bundle_path = sys.argv[1] if len(sys.argv) > 1 else "example_bundle"
    display_bundle(bundle_path)