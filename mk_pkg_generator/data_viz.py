import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Data_viz:

    def __init__(self, df):
    #----------------------------------------------------------------
        """ • Initialise self.df
            • Params = dataset
            • Return None """
    #----------------------------------------------------------------
        self.df = df
    
    def infos(self):
    #----------------------------------------------------------------
        """ • Shows infos on self.df(lines, cilumns, nulls) 
            and make sample of features
            • Return dataset """
    #----------------------------------------------------------------
        
        print(f"""
        Nombre de lignes : {self.df.shape[0]} lignes
        Nombre de colonnes : {self.df.shape[1]} colonnes
        Nombre total de celulles non nulles : {self.df.notna().sum().sum()}
        Nombre total de cellules nulles : {self.df.isna().sum().sum()}
        """)

        samples = []
        for i in self.df.columns:
            samples.append(str(list(self.df[i].head(5))))

        obs = pd.DataFrame({
            'name' : self.df.columns,
            'type':self.df.dtypes,
            'sample':samples,
            '% nulls':round((self.df.isnull().sum()/len(self.df))*100)   
            })

        return obs

    #pip install git+https://github.com/anais-15/Exo_package
