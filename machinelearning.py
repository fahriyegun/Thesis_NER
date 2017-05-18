from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer()

measurements = [
    {'city': 'Dubai', 'temperature': 33.},
    {'city': 'London', 'temperature': 12.},
    {'city': 'San Fransisco', 'temperature': 18.},
]
vec.fit_transform(measurements).toarray()
vec.get_feature_names()