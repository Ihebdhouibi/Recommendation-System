import pandas as pd

# read dataset
df = pd.DataFrame(pd.read_excel('./datasets/eleve_dataset_avec tout les champs-Premiere Essai.xlsx'))

# data visualization
print(df.head())
print("number rows: ", df.count())

# drop lines where "Niveau scolaire = Premier"
df = df[df['Niveau Scolaire'] != 'Premier']
print("number rows: ", df.count())

# save locally
#df.to_csv('./datasets/eleve2eme.csv', index=False)
df.to_excel('./datasets/eleve2eme.xlsx', index=False)