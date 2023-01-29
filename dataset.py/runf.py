import pickle
import re
with open("/workspaces/codespaces-blank/data_main.dat", "rb") as f:
    dataset = pickle.load(f)
def clean_text(text):
    text = text.lower()
    #remove text in brackets
    text = re.sub(r'\([^)]*\)', '', text)
    #remove text in curly brackets
    text = re.sub(r'\{[^)]*\}', '', text)
    #remove text in (...) brackets
    text = re.sub(r'\[[^)]*\]', '', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text
def complete_sentence(data):
    set = dataset
    for i in data:
        for j in set:
            if i == j:
                return set[set.index(j)+1]
                
    return None
    #is the word is there in the data of user then we will jump to next index of the word in the dataset
    """print("cnt",set[set.index(j)+[k for k, n in enumerate(wordlist) if n == i][cnt]] )
    return set[set.index(j)+[k for k, n in enumerate(wordlist) if n == i][cnt]]"""
def encode_user_data(user_data):
    user_data = clean_text(user_data)
    user_data = user_data.split()
    user_data = [text2int[word] for word in user_data]
    return user_data

text2int = dataset['t2i']
int2text = dataset['i2t']
dataset = dataset['dataset']
data = input("Enter your data: ")
user_data = encode_user_data(data)
revals = []
revals.extend(user_data)
for i in range(0,256):
    revals.append(complete_sentence(user_data))
    user_data = [complete_sentence(user_data)]
print("\n")
nlst = []     
for i in revals:
    if i not in nlst:
        nlst.append(i)
        print(int2text[i],end=" ")


print("\n")