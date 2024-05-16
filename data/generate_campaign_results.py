import pandas as pd
import numpy as np

def generate_campaign_results(subscribers_data, control_group, treatment_group):
    """
    Generate random campaign results data based on subscriber data and A/B test groups.

    Parameters:
    - subscribers_data: DataFrame containing subscriber data.
    - control_group: List of subscriber IDs in the control group.
    - treatment_group: List of subscriber IDs in the treatment group.

    Returns:
    - campaign_results_data: DataFrame containing campaign results data.
    """
    # Assign opened and converted values based on A/B test groups
    opened = np.random.choice([0, 1], size=len(subscribers_data), p=[0.3, 0.7])
    converted = np.random.choice([0, 1], size=len(subscribers_data), p=[0.1, 0.9])
    
    # Adjust open and conversion rates for treatment group
    opened[subscribers_data['subscriber_id'].isin(treatment_group)] = np.random.choice([0, 1], size=sum(subscribers_data['subscriber_id'].isin(treatment_group)), p=[0.2, 0.8])
    converted[subscribers_data['subscriber_id'].isin(treatment_group)] = np.random.choice([0, 1], size=sum(subscribers_data['subscriber_id'].isin(treatment_group)), p=[0.15, 0.85])

    # Create the campaign results DataFrame
    campaign_results_data = pd.DataFrame({
        'subscriber_id': subscribers_data['subscriber_id'],
        'opened': opened,
        'converted': converted
    })

    return campaign_results_data

# Example usage
subscribers_data = pd.read_csv('subscribers.csv')
control_group = subscribers_data.sample(frac=0.5).subscriber_id.tolist()
treatment_group = [sid for sid in subscribers_data.subscriber_id if sid not in control_group]

campaign_results_data = generate_campaign_results(subscribers_data, control_group, treatment_group)
campaign_results_data.to_csv('campaign_results.csv', index=False)
