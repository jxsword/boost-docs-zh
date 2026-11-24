# -*- coding: utf-8 -*-
"""pilot_qa.py - run the four QA gates restricted to pilot pages.

Reads work/pilot_files.tsv (lib <TAB> relpath) and invokes each qa_*.py
with --lib and exact-file --prefix args.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WS = Path(__file__).resolve().parent.parent

GATES = ["qa_dom_parity.py", "qa_terms.py", "qa_links.py", "qa_coverage.py"]


def main():
    libs = {}
    for line in (WS / "work" / "pilot_files.tsv").read_text(
            encoding="utf-8").splitlines():
        if not line.strip():
            continue
        lib, f = line.split("\t")
        libs.setdefault(lib, []).append(f)
    failures = 0
    for gate in GATES:
        print(f"===== {gate} =====")
        for lib, fs in libs.items():
            args = [sys.executable, "-I", f"pipeline/{gate}",
                    "--lib", lib]
            for f in fs:
                args += ["--prefix", f]
            r = subprocess.run(args, capture_output=True, text=True,
                               encoding="utf-8", errors="replace",
                               cwd=str(WS))
            tail = (r.stdout or r.stderr).strip().splitlines()
            summary = tail[-1] if tail else "(no output)"
            print(f"[{lib}] rc={r.returncode} {summary}")
            if r.returncode != 0:
                failures += 1
                for line in tail[:-1][:12]:
                    print("   ", line)
    print("=====", "ALL GREEN" if failures == 0 else f"{failures} gate-lib runs failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
