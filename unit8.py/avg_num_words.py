
# def read():
#     with open("text.txt", "r") as file:
#         text = file.read()
#     return text

# def avg_num_words(text):
#     sentences = text.split(".") # breaks the sentences at the period character 
#     total_sentences = len(sentences) # counte total number of sentences 
#     total_words = sum(len(sentence.split()) for sentence in sentences) # counts the total number of words in the whole doc
#     average = total_words / total_sentences if total_sentences > 0 else 0 # total no. of words / total no. of sentences. 
#     return average

# def main():
#     text = read()
#     average = avg_num_words(text)
#     print(f"The average number of words per sentence is: {average:.2f}")

def main():
    with open("text.txt", "r") as infile:
        sentences = infile.readlines()
    
        num_sentences = len(sentences) # number
        for item in sentences:
            words = item.split()
            total_words = len(words)
        average_words = float(total_words/num_sentences)
        print(f"The average number of words per sentence is: {average_words}")

if __name__ == "__main__":
    main()

