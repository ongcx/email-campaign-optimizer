import pandas as pd

def load_data(subscribers_file, campaign_results_file):
    """
    Load subscriber and campaign results data from CSV files.

    Parameters:
    - subscribers_file: Path to the subscribers CSV file.
    - campaign_results_file: Path to the campaign results CSV file.

    Returns:
    - subscribers_data: DataFrame containing subscriber data.
    - campaign_results_data: DataFrame containing campaign results data.
    """
    subscribers_data = pd.read_csv(subscribers_file)
    campaign_results_data = pd.read_csv(campaign_results_file)

    return subscribers_data, campaign_results_data
