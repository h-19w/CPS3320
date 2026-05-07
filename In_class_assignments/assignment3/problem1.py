
def main():
    filename = input("Enter filename: ")
    freq = {}

    with open(filename) as f:
        for line in f:
            for word in line.split():
                word = word.strip('.,!?;:\'"').lower()
                if word:
                    freq[word] = freq.get(word, 0) + 1

    with open("frequency.txt", "w") as out:
        out.write(f"{'Word':<20} {'Count':>5}\n")
        out.write("-" * 27 + "\n")
        for word in sorted(freq):
            out.write(f"{word:<20} {freq[word]:>5}\n")

    print("Saved to frequency.txt")
if __name__ == "__main__":
    main()