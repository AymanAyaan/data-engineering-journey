import my_tools


def main():
    file_path = "../ostad-de-bootcamp-main/module-02/data/raw_sales.txt"
    lines = my_tools.read_lines(file_path)

    d07_total = 0.0
    d08_total = 0.0
    d09_total = 0.0
    d10_total = 0.0
    d11_total = 0.0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(";")
        status = parts[7].strip().lower()

        if status == "cancelled":
            continue

        date = parts[1].strip()
        amount = my_tools.clean_amount(parts[5])

        if date == "2026-10-07":
            d07_total += amount
        elif date == "2026-10-08":
            d08_total += amount
        elif date == "2026-10-09":
            d09_total += amount
        elif date == "2026-10-10":
            d10_total += amount
        elif date == "2026-10-11":
            d11_total += amount

    print("তারিখ ধরে হিসাব (বাতিল বাদে)\n")
    print(f"2026-10-07 : {my_tools.taka(d07_total)}")
    print(f"2026-10-08 : {my_tools.taka(d08_total)}")
    print(f"2026-10-09 : {my_tools.taka(d09_total)}")
    print(f"2026-10-10 : {my_tools.taka(d10_total)}")
    print(f"2026-10-11 : {my_tools.taka(d11_total)}")

    best_date = "2026-10-07"
    best_total = d07_total

    if d08_total > best_total:
        best_date, best_total = "2026-10-08", d08_total
    if d09_total > best_total:
        best_date, best_total = "2026-10-09", d09_total
    if d10_total > best_total:
        best_date, best_total = "2026-10-10", d10_total
    if d11_total > best_total:
        best_date, best_total = "2026-10-11", d11_total

    print(f"\nসবচেয়ে বেশি অর্ডার: {best_date} ({my_tools.taka(best_total)})")


if __name__ == "__main__":
    main()
