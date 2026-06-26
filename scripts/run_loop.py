import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/run_loop.py <path-to-loop.md>")
        return 1

    loop_path = Path(sys.argv[1])
    if not loop_path.exists():
        print(f"Loop file not found: {loop_path}")
        return 1

    print("GitStar AI Loop Runner")
    print("======================")
    print(loop_path.read_text(encoding="utf-8"))
    print("\nNext: paste this loop into your AI coding agent with current STATE.md context.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
