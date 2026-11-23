import os

TEXT = (
    "Day 1: enter every free make.fun bounty (6/day max, $2-50 each, $0 cost) "
    "and list agent-built gigs on Fiverr at $30 (pages, scrapers, docs), 2/day. "
    "Reinvest first $50 only into paid contests with <40 entrants. Keep $50 "
    "untouched. No leverage, no tokens. Day-30 target: $450-900."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
