
import pandas as pd
df = pd.DataFrame({
    'user_id': [1, 2, 3],
    'song_id': ['song1', 'song2', 'song3'],
    'interaction_type': ['play', 'like', 'dislike']
})
df.to_parquet('interactions.parquet', index=False)
