def get_num_words(file_path): 
    with open(file_path) as f:
        file_contents = f.read()
    num_words = file_contents.split()
    return len(num_words)

def print_count_chars(char_dict):
    sort_vals = sorted(char_dict.items(), key = lambda item: item[1], reverse=True)
    for key, value in sort_vals: 
        print(f"{key}: {value}")
    return None
    

def count_chars(file_path): 
    with open(file_path) as f:
        file_contents = f.read()
    num_words = file_contents.split()
    char_dict = {}
    for word in num_words: 
        word = word.lower()
        for char in word: 
            if char in char_dict: 
                char_dict[char]+=1
            else:
                char_dict[char]=1
    return print_count_chars(char_dict)