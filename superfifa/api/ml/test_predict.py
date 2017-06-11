import os

from django.core.cache import cache
from sklearn.externals import joblib


def get_prediction():
    model_cache_key = 'model_cache'
    model_rel_path = "/home/akshay/kevin/superfifa/api/ml/model_cache/cache.pkl"

    model = cache.get(model_cache_key)

    if model is None:
        model_path = os.path.realpath(model_rel_path)
        model = joblib.load(model_path)
        # save in django memory cache
        cache.set(model_cache_key, model, None)
    print "loaded model"
    prediction = model.predict([2, 106, 56, 27, 165, 29.0, 0.426, 22])
    print prediction
