import nltk
import math
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')


filename = "./requirements.txt"

do_stop_words = True
do_stemming = True
do_lemmatization = False
do_parts_of_speech = False

do_thresholding = False
similarity_threshold = 0.2

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def preprocess_tokens(tokens):
    if do_stop_words:
        tokens = [w for w in tokens if w.lower() not in stop_words]
    
    if do_lemmatization:
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
        
    if do_stemming:
        tokens = [stemmer.stem(t) for t in tokens]
        
    return tokens


def similarity(nfrs, frs):
    count = 0
    with open("output.txt", "w") as output_file:
        for fr_tokens in frs:
            count += 1
            fr_set = set(fr_tokens)
            similarities = []

            for nfr_tokens in nfrs:
                nfr_set = set(nfr_tokens)

                intersection = fr_set.intersection(nfr_set)

                dot_product = len(intersection)

                magnitude_fr = math.sqrt(len(fr_set))
                magnitude_nfr = math.sqrt(len(nfr_set))

                if magnitude_fr * magnitude_nfr == 0:
                    cosine = 0.0
                else:
                    cosine = dot_product / (magnitude_fr * magnitude_nfr)
                
                if do_thresholding:
                    if cosine >= similarity_threshold:
                        cosine = 1
                    else:
                        cosine = 0

                similarities.append(round(cosine, 3))
            
            similarities_string: str = f"FR {count} Similarities to NFRs: {similarities}"
            
            print(similarities_string)
            output_file.write(similarities_string + "\n")
        


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [line for line in f if line.strip()]
    processed_lines = []

    for line in lines:
        tokens = word_tokenize(line)
        processed_tokens = preprocess_tokens(tokens)
        processed_lines.append(processed_tokens)

    processed_lines = [line[2:] for line in processed_lines]
    processed_lines = [[token for token in tokens if token not in string.punctuation] for tokens in processed_lines]

    nfrs = processed_lines[0:3]
    frs = processed_lines[3:]

    # print(frs)
    similarity(nfrs, frs)
