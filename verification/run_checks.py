"""Run the finite scientific checks from any working directory."""
from pathlib import Path
import subprocess
import sys

if sys.flags.optimize:
    raise SystemExit("Run without -O: the numerical scripts use Python assertions.")

here = Path(__file__).resolve().parent
for name in ("check_geometry.py", "check_ladders.py", "check_tradeoff.py",
             "check_prescribed_errors.py"):
    subprocess.run([sys.executable, str(here/name)], cwd=here, check=True)
print("PASS: all finite scientific checks completed.")
