import anvil.server
import anvil.media
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

@anvil.server.callable
def get_plots():
    data = pd.read_csv('C:\\Users\\Gaming-PC\\Desktop\\noctoria_df.csv')  # Path to your dataset
    
    # Create a figure to hold the subplots
    fig, axes = plt.subplots(3, 1, figsize=(10, 18))

    # Plot 1: Distribution of nocturia cases by age and sex
    sns.histplot(data=data, x='age', hue='nocturia', bins=20, ax=axes[0], kde=True)
    axes[0].set_title('Distribution of Nocturia Cases by Age and Sex')

    # Plot 2: Correlation between BMI and nocturia
    sns.boxplot(data=data, x='nocturia', y='bmi', ax=axes[1])
    axes[1].set_title('Correlation between BMI and Nocturia')

    # Plot 3: Effects of smoking, alcohol, and caffeine on nocturia
    sns.boxplot(data=data, x='nocturia', y='smoking', ax=axes[2])
    axes[2].set_title('Effect of Smoking on Nocturia')

    plt.tight_layout()
    
    # Convert plot to PNG image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    return anvil.media.from_file(buffer, 'image/png')

anvil.server.wait_forever()
