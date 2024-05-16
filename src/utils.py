import matplotlib.pyplot as plt

def plot_open_rates(control_group, treatment_group, data):
    control_open_rates = data.loc[data['subscriber_id'].isin(control_group), 'opened'].mean()
    treatment_open_rates = data.loc[data['subscriber_id'].isin(treatment_group), 'opened'].mean()

    plt.figure(figsize=(10, 6))
    plt.bar(['Control Group', 'Treatment Group'], [control_open_rates, treatment_open_rates], color=['skyblue', 'salmon'])
    plt.title('Open Rates Comparison')
    plt.ylabel('Open Rate')
    plt.ylim(0, 1)
    
    for i, rate in enumerate([control_open_rates, treatment_open_rates]):
        plt.text(i, rate + 0.02, f"{rate:.2%}", ha='center', color='black')

    plt.show()

def plot_conversion_rates(control_group, treatment_group, data):
    control_conv_rates = data.loc[data['subscriber_id'].isin(control_group) & (data['converted'] == 1), 'converted'].mean()
    treatment_conv_rates = data.loc[data['subscriber_id'].isin(treatment_group) & (data['converted'] == 1), 'converted'].mean()

    plt.figure(figsize=(10, 6))
    plt.bar(['Control Group', 'Treatment Group'], [control_conv_rates, treatment_conv_rates], color=['lightgreen', 'coral'])
    plt.title('Conversion Rates Comparison')
    plt.ylabel('Conversion Rate')
    plt.ylim(0, 1)
    
    for i, rate in enumerate([control_conv_rates, treatment_conv_rates]):
        plt.text(i, rate + 0.02, f"{rate:.2%}", ha='center', color='black')

    plt.show()
