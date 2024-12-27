import pandas as pd



class InsuranceDataAnalysis:
    def __init__(self, data):
        self.data = data

    def descriptive_statistics(self):
        """Generate descriptive statistics grouped by province and gender."""
        return self.data.groupby(['Province', 'Gender']).agg(
            Avg_Total_Claim=('TotalClaim', 'mean'),
            Avg_Premium=('TotalPremium', 'mean'),
            Count=('TotalClaim', 'size')
        ).reset_index()