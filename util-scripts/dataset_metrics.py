import os


def find_python_files(folder_path):
    """
    Recursively find and print all Python (.py) files in the specified folder.

    :param folder_path: Path to the folder to search in.
    """
    counts = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py') and not file.startswith("test") and "_cwe" in file:
                source, cwe_id, prompt_id = file.split("_")
                if source not in counts:
                    counts[source] = {}
                if cwe_id not in counts[source]:
                    counts[source][cwe_id] = 0
                counts[source][cwe_id] += 1

                print(os.path.join(root, file))

    return counts


if __name__ == "__main__":
    folder_path = "../Dataset"
    counts = find_python_files(folder_path)
    cwe_counts = {}
    for source, cwes in counts.items():
        for cwe_id, cwe_count in cwes.items():
            # print(f"\t{source}+{cwe_id}: {cwe_count}")
            if cwe_id not in cwe_counts:
                cwe_counts[cwe_id] = 0
            cwe_counts[cwe_id] += cwe_count

    headers = ["CWE"] + [source for source in counts.keys()]
    print("\t".join(headers))

    for cwe_id, cwe_count in cwe_counts.items():
        formatted_cwe_id = f"CWE-{int(cwe_id.replace('cwe', ''))}"
        row = [formatted_cwe_id]
        for source in headers[1:]:
            if cwe_id in counts[source]:
                row.append(counts[source][cwe_id])
            else:
                row.append(0)
        print("\t".join([str(x) for x in row]))
