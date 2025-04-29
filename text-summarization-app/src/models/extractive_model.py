from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np

class ExtractiveSummarizer:
    def __init__(self, n_clusters=5):
        self.n_clusters = n_clusters
        self.vectorizer = TfidfVectorizer()
        self.kmeans = KMeans(n_clusters=self.n_clusters)

    def fit(self, documents):
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        self.kmeans.fit(tfidf_matrix)

    def summarize(self, document, num_sentences=3):
        sentences = document.split('. ')
        tfidf_matrix = self.vectorizer.transform(sentences)
        cluster_labels = self.kmeans.predict(tfidf_matrix)

        # Select the top sentences from each cluster
        summarized_sentences = []
        for i in range(self.n_clusters):
            cluster_sentences = np.array(sentences)[cluster_labels == i]
            if len(cluster_sentences) > 0:
                summarized_sentences.append(cluster_sentences[0])  # Select the first sentence from each cluster

        # Return the top 'num_sentences' sentences
        return '. '.join(summarized_sentences[:num_sentences]) + '.' if summarized_sentences else ''