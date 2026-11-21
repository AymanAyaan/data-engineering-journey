import my_tools


def main():
    file_path = "../ostad-de-bootcamp-main/module-02/data/raw_sales.txt"
    lines = my_tools.read_lines(file_path)

    bkash_total, bkash_count = 0.0, 0
    nagad_total, nagad_count = 0.0, 0
    card_total, card_count = 0.0, 0
    rocket_total, rocket_count = 0.0, 0
    cod_total, cod_count = 0.0, 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split(";")
        status = parts[7].strip().lower()

        if status == "cancelled":
            continue

        payment = parts[6].strip().lower()
        amount = my_tools.clean_amount(parts[5])

        if payment == "bkash":
            bkash_total += amount
            bkash_count += 1
        elif payment == "nagad":
            nagad_total += amount
            nagad_count += 1
        elif payment == "card":
            card_total += amount
            card_count += 1
        elif payment == "rocket":
            rocket_total += amount
            rocket_count += 1
        elif payment == "cash on delivery":
            cod_total += amount
            cod_count += 1

    grand_total = bkash_total + nagad_total + card_total + rocket_total + cod_total

    print("payment ধরে হিসাব (বাতিল বাদে)\n")
    print(f"{'bkash':<17} {bkash_count}টা   {my_tools.taka(bkash_total)}")
    print(f"{'nagad':<17} {nagad_count}টা   {my_tools.taka(nagad_total)}")
    print(f"{'card':<17} {card_count}টা   {my_tools.taka(card_total)}")
    print(f"{'rocket':<17} {rocket_count}টা   {my_tools.taka(rocket_total)}")
    print(f"{'cash on delivery':<17} {cod_count}টা   {my_tools.taka(cod_total)}")
    print(f"\nসব মিলিয়ে: {my_tools.taka(grand_total)}")


if __name__ == "__main__":
    main()
