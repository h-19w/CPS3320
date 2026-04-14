
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
    # with open("text.txt", "r") as infile:
    #     sentences = infile.readlines()
    
    #     num_sentences = len(sentences) # number
    #     for item in sentences:
    #         words = item.split()
    #         total_words = len(words)
    #     average_words = float(total_words/num_sentences)
    #     print(f"The average number of words per sentence is: {average_words}")

    with open("text.txt", "r") as infile:
        text = infile.read()
        space_count = 0
        upper_count = 0
        lower_count = 0
        digit_count = 0

        for char  in text:
            if char.isspace():
                space_count += 1
            elif char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
            elif char.isdigit():
                digit_count += 1
    print(f"Number of spaces: {space_count}")
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")
    print(f"Number of digits: {digit_count}")    

if __name__ == "__main__":
    main()

