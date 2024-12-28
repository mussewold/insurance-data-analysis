import matplotlib.pyplot as plt
import seaborn as sns
class Plots:
    def __init__(self, df):
        self.df = df

    def histogram(self, column):
        plt.hist(self.df[column])
        plt.xlabel(column)
        plt.title(f'Distribution of {column}')
        plt.ylabel('Frequency')
        plt.show()
        
    def scatter_plot(self, data, x, y, hue, title):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x=x, y=y, hue=hue, style=hue)
        plt.axhline(0, color='gray', linestyle='--', linewidth=0.7)
        plt.axvline(0, color='gray', linestyle='--', linewidth=0.7)
        plt.title(title)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.legend(title=hue)
        plt.show()

    def boxplot_two_columns(self, column1, column2):
        # Create box plots for column1 and column2
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

        # Box plot for column1
        self.df.boxplot(column=column1, ax=ax1)
        ax1.set_title(f'Box Plot of {column1}')
        ax1.set_ylabel(column1)

        # Box plot for column2  
        self.df.boxplot(column=column2, ax=ax2)
        ax2.set_title(f'Box Plot of {column2}')
        ax2.set_ylabel(column2)

        plt.tight_layout()
        plt.show()