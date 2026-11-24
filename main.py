"""Write the competition's one-line entry to /output/entry.txt."""

import os
from pathlib import Path

LINE = "ERROR: Slot 2 contains a fork. We need to talk about your choices."

assert 1 <= len(LINE) <= 120
assert "\n" not in LINE

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_path = output_dir / "entry.txt"
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(LINE, encoding="utf-8")
os.chmod(output_path, 0o644)

# Verification: output is deterministic and contains no trailing newline.
