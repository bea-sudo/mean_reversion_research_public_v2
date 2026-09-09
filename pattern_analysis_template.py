from pathlib import Path
from collections import defaultdict
import pandas as pd

PATTERN_LENGTH = 5
MIN_OCCURRENCES = 100

def main():
    path = Path(input("Trade XLSX/CSV path: ").strip().strip('"'))
    df = pd.read_excel(path, sheet_name="Trades") if path.suffix.lower() in {".xlsx",".xlsm"} else pd.read_csv(path)
    x = df[df["Type"].astype(str).str.lower().str.startswith("exit")].copy()
    pnl = pd.to_numeric(x["Net PnL USD"], errors="coerce").dropna()
    seq = [1 if p > 0 else 0 if p < 0 else None for p in pnl]

    patterns = defaultdict(list)

    for i in range(PATTERN_LENGTH, len(seq)):
        previous = seq[i-PATTERN_LENGTH:i]
        nxt = seq[i]

        if nxt is None or any(v is None for v in previous):
            continue

        patterns["".join(map(str, previous))].append(nxt)

    rows = []

    for pattern, results in patterns.items():
        if len(results) < MIN_OCCURRENCES:
            continue

        rows.append({
            "Pattern": pattern,
            "Occurrences": len(results),
            "Next_Win_Rate_Pct": round(sum(results) / len(results) * 100, 3),
        })

    result = pd.DataFrame(rows).sort_values(
        ["Next_Win_Rate_Pct","Occurrences"],
        ascending=False
    )

    print(result.to_string(index=False))

if __name__ == "__main__":
    main()
