#!/usr/bin/env python3
import json
import os
from item_report import get_valid_records, totals_by

OUTDIR = os.path.join("week-04", "output")


def main():
    _, records, cancelled = get_valid_records()
    totals, counts = totals_by(records, "item_name")
    by_date_raw, _ = totals_by(records, "order_date")

    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, "report_week2.json")

    by_item = {name: round(totals[name], 2) for name in sorted(totals)}
    by_date = {date: round(by_date_raw[date], 2) for date in sorted(by_date_raw)}

    best_item = max(totals, key=totals.get)

    report = {
        "company": "ThelaGari",
        "week": "2026-10-12 → 2026-10-18",
        "counted": len(records),
        "cancelled": cancelled,
        "grand_total": round(sum(totals.values()), 2),
        "top_item": {
            "item_name": best_item,
            "orders": counts[best_item],
            "total_amount": round(totals[best_item], 2),
        },
        "by_item": by_item,
        "by_date": by_date,
    }

    with open(path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as fh:
        loaded = json.load(fh)

    print(type(loaded["grand_total"]))
    print(loaded["top_item"]["item_name"])


if __name__ == "__main__":
    main()
