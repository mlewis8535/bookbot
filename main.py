def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        dicktionary = {}
        lowered_words = file_contents.lower()
        for char in lowered_words:
            if char.isalpha():
            
                if char in dicktionary:
                    dicktionary[char] += 1
                else:
                    dicktionary[char] = 1
        # sorted() with a key function can sort dictionary items
        # First get your sorted items
    sorted_items = sorted(dicktionary.items(), key=lambda x: x[1], reverse=True)

# Then loop through them and print each one
    for char, count in sorted_items:
        print(f"The '{char}' character was found {count} times") 



    
main()