
from feature_flags import is_feature_active

def get_predictions(request):
    if is_feature_active('new_model'):
        predictions = new_model.predict(request.data)
    else:
        predictions = old_model.predict(request.data)

    return predictions
