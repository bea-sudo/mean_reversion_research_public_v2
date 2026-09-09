from pathlib import Path
import pandas as pd
import numpy as np

COST_PER_TRADE = 0.0

def season(m):
    if m in (12, 1, 2): return "Winter"
    if m in (3, 4, 5): return "Spring"
    if m in (6, 7, 8): return "Summer"
    return "Autumn"

def load(path):
    path = Path(path)
    df = pd.read_excel(path, sheet_name="Trades") if path.suffix.lower() in {".xlsx",".xlsm"} else pd.read_csv(path)
    x = df[df["Type"].astype(str).str.lower().str.startswith("exit")].copy()
    x["Date and time"] = pd.to_datetime(x["Date and time"], errors="coerce")
    x["Net PnL USD"] = pd.to_numeric(x["Net PnL USD"], errors="coerce")
    x = x.dropna(subset=["Date and time","Net PnL USD"])
    x["PnL"] = x["Net PnL USD"] - COST_PER_TRADE
    x["Year"] = x["Date and time"].dt.year
    x["Month"] = x["Date and time"].dt.month_name()
    x["Season"] = x["Date and time"].dt.month.apply(season)
    x["Weekday"] = x["Date and time"].dt.day_name()
    x["Hour"] = x["Date and time"].dt.hour
    return x

def summarize(df, col):
    rows = []
    for value, g in df.groupby(col):
        pnl = g["PnL"]
        wins = int((pnl > 0).sum())
        losses = int((pnl < 0).sum())
        n = wins + losses
        wr = wins / n * 100 if n else 0
        gp = pnl[pnl > 0].sum()
        gl = -pnl[pnl < 0].sum()
        pf = gp / gl if gl > 0 else np.inf
        rows.append({
            col: value,
            "Trades": len(g),
            "Win_Rate_Pct": round(wr, 3),
            "Net_PnL": round(pnl.sum(), 2),
            "Avg_PnL": round(pnl.mean(), 4),
            "Profit_Factor": round(pf, 4),
        })
    return pd.DataFrame(rows).sort_values(["Avg_PnL","Profit_Factor"], ascending=False)

def main():
    path = input("Trade XLSX/CSV path: ").strip().strip('"')
    df = load(path)
    for col in ["Season","Month","Weekday","Hour","Year"]:
        print(f"\n=== {col.upper()} ===")
        print(summarize(df, col).to_string(index=False))

if __name__ == "__main__":
    main()
