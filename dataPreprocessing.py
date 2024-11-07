import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# read our excel dataset
df = pd.DataFrame(pd.read_excel('./datasets/eleve_dataset_Premier.xlsx'))

# Data Visualization
print("dataframe          :")
print(df)

# Check for NaN values 
nan_summary = df.isna().sum()
print(nan_summary)

# Change Niveauscolaire to number : 1 for "Premier année"
# Implicit categorical encoding 
df["Niveau Scolaire"] = 1 

# For the remaining textual catagorical columns we'll use label encoder from sklearn
# encoding of Genre column
encoder = OneHotEncoder(drop='first')
encoded_genre = encoder.fit_transform(df[['Genre']]).toarray()
encoded_df = pd.DataFrame(encoded_genre, columns=encoder.get_feature_names_out(['Genre']))
df = pd.concat([df.drop('Genre', axis=1), encoded_df], axis=1)

# encoding of Clubs column
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_clubs = encoder.fit_transform(df[['Clubs']])
encoded_df = pd.DataFrame(encoded_clubs, columns=encoder.get_feature_names_out(['Clubs']))
df = pd.concat([df.drop('Clubs', axis=1), encoded_df], axis=1)
#print(encoder.categories_)

# encoding of aspiration professionelle column
encoder = OneHotEncoder(sparse_output=False, drop='first')
encoded_AspirProf = encoder.fit_transform(df[['Aspiration Professionnelle']])
encoded_df = pd.DataFrame(encoded_AspirProf, columns=encoder.get_feature_names_out(['Aspiration Professionnelle']))
df = pd.concat([df.drop('Aspiration Professionnelle', axis=1), encoded_df], axis=1)

# encoding of target column orientation affectue
label_encoder = LabelEncoder()
df['Orientation Affectue encoded'] = label_encoder.fit_transform(df['Orientation Affectuee '])


#print(df.columns)
# Convert the excel dataset into csv
#df.to_csv("Dataset.csv",
#          index= None,
#          header= True)

# read csv file and convert  
# into a dataframe object
#df = pd.DataFrame(pd.read_csv("Dataset.csv"))

# display result
#print("dataframe csv:")
print(df)