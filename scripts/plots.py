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