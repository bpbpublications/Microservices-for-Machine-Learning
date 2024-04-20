
if recommendation_accepted:
    increment_recommendation_acceptance_metric()
log_time_taken_to_generate_recommendation(time_taken)

log.info(f"Logic used: {recommendation_logic}")
log.info(f"Recommendation output: {recommended_song}")
