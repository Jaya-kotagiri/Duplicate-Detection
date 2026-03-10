def find_duplicate_emails(file_path):
    seen = set()
    duplicates = set()

    with open(file_path, "r") as f:
        for line in f:
            email = line.strip()

            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)

    return duplicates, seen


if __name__ == "__main__":
    duplicates, seen = find_duplicate_emails("emails.txt")
    print(f"Total duplicates found: {len(duplicates)}")
    print(f"Total unique id's found: {len(seen)}")