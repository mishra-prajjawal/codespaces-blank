# We are going to make an AI that can complete sentences for us.
import re
import pickle 
with open("/workspace/codespaces-blank/codespaces-blank/data_main.txt", "r") as f:
    example_data = f.read()


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
def create_encodes(input):
    input = input.split()
    word2int = {}
    int2word = {}
    for i, word in enumerate(input):
        word2int[word] = i
        int2word[i] = word
    return word2int, int2word
text = clean_text(example_data)


text2int,int2text = create_encodes(text)
dataset = []
for i in text.split():
    dataset.append(text2int[i])
#now we will take user data and enocde it
def encode_user_data(user_data):
    user_data = clean_text(user_data)
    user_data = user_data.split()
    user_data = [text2int[word] for word in user_data]
    return user_data
with open("data_main.dat", "wb") as f:
    pickle.dump({'t2i':text2int,'i2t':int2text,'dataset':dataset}, f)
data = input("Enter your data: ")
user_data = encode_user_data(data)
revals = []
revals.extend(user_data)
print(revals)
def complete_sentence(data):
    set = dataset
    #comparing the user data to find matches 
    # like [164,165] => [139,175....] basically finding the user pattern in the dataset and then finding the next word
    # checking user data list woth dataset list
    """
    for i in range(len(set)):
        if set[i:i+len(data)] == data:
            return set[i+len(data)]"""
    for i in data:
        for j in set:
            if i == j:
                return set[set.index(j)+1]
            


    return None

for i in range(0,256):
    revals.append(complete_sentence(user_data))
    user_data = [complete_sentence(user_data)]

nlst = []     
for i in revals:
    if i not in nlst:
        nlst.append(i)
        print(int2text[i],end=" ")


print("\n")
# clean data 
"""
a voivodeship polish wojewdztwo vjvutstf plural wojewdztwa is the highestlevel administrative division of poland corresponding to a province in many other countries the term has been in use since the 14th century and is commonly translated into english as provincethe polish local government reforms adopted in 1998 which went into effect on 1 january 1999 created sixteen new voivodeships these replaced the 49 former voivodeships that had existed from 1 july 1975 and bear a greater resemblance in territory but not in name to the voivodeships that existed between 1950 and 1975 todays voivodeships are mostly named after historical and geographical regions while those prior to 1998 generally took their names from the cities on which they were centered the new units range in area from under 10000 km2 3900 sq mi opole voivodeship to over 35000 km2 14000 sq mi masovian voivodeship and in population from nearly one million opole voivodeship to over five million masovian voivodeship administrative authority at the voivodeship level is shared between a governmentappointed governor called a voivode wojewoda an elected assembly called a sejmik and an executive board zarzd wojewdztwa chosen by that assembly headed by a voivodeship marshal marszaek wojewdztwa voivodeships are further divided into powiats counties and gminas communes or municipalities the smallest administrative divisions of poland
"""
