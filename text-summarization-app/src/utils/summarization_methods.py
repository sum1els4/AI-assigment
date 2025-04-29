from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

def extractive_summary(text, num_sentences=3):
    sentences = text.split('. ')
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    
    kmeans = KMeans(n_clusters=num_sentences)
    kmeans.fit(tfidf_matrix)
    
    avg = []
    for i in range(num_sentences):
        avg.append(np.mean(tfidf_matrix[kmeans.labels_ == i].toarray(), axis=0))
    
    avg = np.array(avg)
    summary_indices = np.argsort(-avg.sum(axis=1))[:num_sentences]
    
    summary = ' '.join([sentences[i] for i in sorted(summary_indices)])
    return summary

def abstractive_summary(text):
    # Placeholder for an abstractive summarization method
    # This could be implemented using a pre-trained transformer model like BART or T5
    return "Abstractive summary generation is not implemented yet."