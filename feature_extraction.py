import requests
from urllib.parse import urlparse

def extract_features(url):
    features = {}

    # Basic text-based features
    features['url_length'] = len(url)
    features['at_symbol'] = url.count('@')
    features['nb_dots'] = url.count('.')
    features['nb_hyphens'] = url.count('-')
    features['nb_and'] = url.lower().count('and')
    features['nb_or'] = url.lower().count('or')
    features['nb_www'] = url.lower().count('www')
    features['nb_com'] = url.lower().count('com')
    features['nb_underscore'] = url.count('_')

    # Sensitive words count
    sensitive_words = ['confirm', 'account', 'secure', 'webscr', 'banking', 'login', 'signin']
    features['sensitive_words_count'] = sum(url.lower().count(word) for word in sensitive_words)

    # Path length (everything after the domain)
    parsed = urlparse(url)
    features['path_length'] = len(parsed.path)

    # isHttps - check the URL scheme
    features['isHttps'] = 1 if parsed.scheme == 'https' else 0

    # valid_url - actually try to visit it
    try:
        response = requests.get(url, timeout=5)
        features['valid_url'] = 1 if response.status_code == 200 else 0
    except requests.exceptions.RequestException:
        features['valid_url'] = 0

    return features


if __name__ == "__main__":
    test_url = "http://example.com"
    print(extract_features(test_url))