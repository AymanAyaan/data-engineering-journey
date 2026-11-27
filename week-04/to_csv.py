#!/usr/bin/env python3
import csv
import os
import sales_tools
from item_report import get_valid_records, totals_by

OUTDIR = os.path.join("week-04", "output")


def main():
    _, records, _ = get_valid_records()
    totals, counts = totals_by(records, "item_name")

    os.makedirs(OUTDIR, exist_ok=True)
    clean = os.path.join(OUTDIR, "sales_week2_clean.csv")
    summary = os.path.join(OUTDIR, "item_summary.csv")

    columns = [
        "order_id", "order_date", "customer_name", "item_name",
        "quantity", "amount", "payment", "status"
    ]

    with open(clean, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)

    print(f"লেখা হলো: {clean}  ({len(records)}টা সারি + হেডার)")

    summary_rows = [
        {
            "item_name": name,
            "orders": counts[name],
            "total_amount": round(totals[name], 2)
        }
        for name in sorted(totals)
    ]

    with open(summary, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["item_name", "orders", "total_amount"])
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"লেখা হলো: {summary}       ({len(summary_rows)}টা সারি + হেডার)")
    print()

    back = []
    with open(clean, "r", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            row["amount"] = float(row["amount"])
            row["quantity"] = int(row["quantity"])
            back.append(row)

    print(f"CSV থেকে ফেরত পড়লাম: {len(back)}টা record")
    if back:
        total = 0.0
        for rec in back:
            total = total + rec["amount"]
        print(f"সব মিলিয়ে: {sales_tools.taka(total)}   ← মিলে গেছে")


if __name__ == "__main__":
    main()
