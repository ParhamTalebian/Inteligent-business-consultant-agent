from sklearn.neighbors import NearestNeighbors
import numpy as np
import pickle

class RetrievalEngine:
    def __init__(self, n_neighbors=5, algorithm='ball_tree'):
        self.n_neighbors = n_neighbors
        self.algorithm = algorithm
        self.model = None
        self.data = None
    
    def fit(self, data):
        self.data = np.array(data)
        self.model = NearestNeighbors(n_neighbors=self.n_neighbors, algorithm=self.algorithm)
        self.model.fit(self.data)
    
    def retrieve(self, query_vector):
        query_vector = np.array(query_vector).reshape(1, -1)
        distances, indices = self.model.kneighbors(query_vector)
        return indices[0], distances[0]
    
    def save(self, filename="retrieval_model.pkl"):
        with open(filename, "wb") as f:
            pickle.dump((self.model, self.data), f)
    
    def load(self, filename="retrieval_model.pkl"):
        with open(filename, "rb") as f:
            self.model, self.data = pickle.load(f)

    def search(self, query):
        
        relevant_data = "این داده‌های مرتبط با پرسش شما هستند."
        return relevant_data


