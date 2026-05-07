
def main():
    filename = input("Enter filename: ")
    index = {}

    with open(filename) as f:
        for line_num, line in enumerate(f, start=1):
            for word in line.split():
                word = word.strip('.,!?;:\'"').lower()
                if word:
                    if word not in index:
                        index[word] = []
                    if line_num not in index[word]:
                        index[word].append(line_num)

    with open("index.txt", "w") as out:
        out.write(f"{'Word':<20} {'Lines':>5}\n")
        out.write("-" * 27 + "\n")
        for word in sorted(index):
            lines = ", ".join(str(n) for n in index[word])
            out.write(f"{word:<20} {lines}\n")

    print("Saved to index.txt")
if __name__ == "__main__":
    main()