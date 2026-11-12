from extra
ct_data import (
    extract_emails,
    extract_urls,
    extract_phone_numbers,
    extract_credit_cards,
    extract_times,
    extract_html_tags,
    extract_hashtags,
    extract_currency
)


def display_results(title, results):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

    if results:
        for result in results:
            print(result)
    else:
        print("No matches found.")


def get_manual_data():
    print("\nEnter your data below.")
    print("Press ENTER twice when you are finished:\n")

    lines = []

    while True:
        line = input()

        if line == "":
            break

        lines.append(line)

    return "\n".join(lines)


def get_source_data():
    source = input("\nEnter the path to your data source: ")

    try:
        with open(source, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("\nError: The specified file was not found.")
        return None

    except PermissionError:
        print("\nError: You do not have permission to read this file.")
        return None


def main():
    print("=" * 50)
    print("       REGEX DATA EXTRACTION TOOL")
    print("=" * 50)

    print("\nHow would you like to provide your data?")
    print("1. Enter the data manually")
    print("2. Provide a source file")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        text = get_manual_data()

    elif choice == "2":
        text = get_source_data()

    else:
        print("\nInvalid choice.")
        return

    if text is None:
        return

    if not text.strip():
        print("\nNo data was provided.")
        return

    # Run all extractors
    emails = extract_emails(text)
    urls = extract_urls(text)
    phone_numbers = extract_phone_numbers(text)
    credit_cards = extract_credit_cards(text)
    times = extract_times(text)
    html_tags = extract_html_tags(text)
    hashtags = extract_hashtags(text)
    currencies = extract_currency(text)

    # Display results
    display_results("EMAIL ADDRESSES", emails)
    display_results("URLs", urls)
    display_results("PHONE NUMBERS", phone_numbers)
    display_results("CREDIT CARD NUMBERS", credit_cards)
    display_results("TIME", times)
    display_results("HTML TAGS", html_tags)
    display_results("HASHTAGS", hashtags)
    display_results("CURRENCY AMOUNTS", currencies)

    print("\n" + "=" * 50)
    print("Extraction complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
