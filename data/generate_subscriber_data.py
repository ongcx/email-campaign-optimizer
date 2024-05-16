import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate random subscriber data
num_subscribers = 1000
subscriber_ids = range(1, num_subscribers + 1)
emails = [f"subscriber{i}@example.com" for i in subscriber_ids]
age = np.random.randint(18, 65, num_subscribers)
gender = np.random.choice(['Male', 'Female'], num_subscribers)
location = np.random.choice(['Selangor', 'Kuala Lumpur', 'Penang'], num_subscribers)

# Create a DataFrame
subscribers_data = pd.DataFrame({
    'subscriber_id': subscriber_ids,
    'email': emails,
    'age': age,
    'gender': gender,
    'location': location
})

# Save the data to a CSV file
subscribers_data.to_csv('subscribers.csv', index=False)
