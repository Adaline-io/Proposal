"""
Build every proposal + the team-facing root index.

Run from anywhere:  python3 _build/build_all.py
Discovers each build_<client>.py, renders its proposal, then rebuilds index.html
from clients.json. Pure stdlib, no external deps.
"""

import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import template as T  # noqa: E402

# Per-client proposal builders. Add new clients here (and to clients.json).
CLIENT_MODULES = [
    "build_rocafuel",
    "build_bzfitness",
    "build_vertex",
    "build_rocaapp",
    "build_ktone",
]


def main():
    for name in CLIENT_MODULES:
        mod = importlib.import_module(name)
        path = T.build(mod.DATA)
        print("  proposal:", os.path.relpath(path, os.path.dirname(HERE)))
    import build_index
    idx = build_index.build()
    print("  index:   ", os.path.relpath(idx, os.path.dirname(HERE)))
    print("Done.")


if __name__ == "__main__":
    main()
