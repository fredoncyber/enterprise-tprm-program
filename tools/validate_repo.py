#!/usr/bin/env python3
"""Validate the public TPRM repository without accessing confidential vendor evidence."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "SECURITY.md", "LICENSE", "policies/tprm-policy.md",
    "docs/risk-methodology.md", "assessments/endpoint-security/assessment-standard.md",
    "data/vendor-register.csv", "tools/risk_score.py",
]


def validate() -> None:
    for name in REQUIRED:
        assert (ROOT / name).is_file(), f"Missing required file: {name}"
    for p in ROOT.rglob("*.json"):
        with p.open(encoding="utf-8") as handle:
            json.load(handle)
    for p in ROOT.rglob("*.csv"):
        with p.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        assert rows and len(rows[0]) > 0, f"Empty CSV: {p}"
        assert all(len(row) == len(rows[0]) for row in rows), f"Malformed CSV: {p}"
    link_pattern = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
    for p in ROOT.rglob("*.md"):
        for link in link_pattern.findall(p.read_text(encoding="utf-8")):
            destination = link.strip().split("#", 1)[0].strip()
            if not destination or ":" in destination or destination.startswith("/"):
                continue
            target = (p.parent / destination).resolve()
            assert target.is_relative_to(ROOT) and target.exists(), f"Broken link: {p}: {link}"


if __name__ == "__main__":
    validate()
    print("Repository validation passed")
