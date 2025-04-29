def clean_text(text):
    import re
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer

    # Initialize the stemmer
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenization
    tokens = text.split()

    # Remove stop words and apply stemming
    cleaned_tokens = [stemmer.stem(token) for token in tokens if token.lower() not in stop_words]

    # Join tokens back to string
    cleaned_text = ' '.join(cleaned_tokens)

    return cleaned_text


def preprocess_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    cleaned_text = clean_text(text)

    # Save cleaned data to processed directory
    with open('data/processed/cleaned_data.txt', 'w', encoding='utf-8') as cleaned_file:
        cleaned_file.write(cleaned_text)

    return cleaned_text


def tokenize_text(text):
    return text.split()


def stem_text(tokens):
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]


def lemmatize_text(tokens):
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]