
from jaeger_client import Config

config = Config(
    config={
        'sampler': {
            'type': 'const',
            'param': 1,
        },
        'logging': True,
    },
    service_name='recommendation_service',
)
tracer = config.initialize_tracer()

def get_recommendations(user_id):
    with tracer.start_span('fetch_user_preferences') as span1:
        preferences = fetch_user_preferences(user_id)
    with tracer.start_span('generate_recommendations') as span2:
        recommendations = generate_based_on_preferences(preferences)
    return recommendations
