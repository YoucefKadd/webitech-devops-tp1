import pandas as pd
import numpy as np

# Créer un DataFrame avec pandas
data = {'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
        'Âge': [25, 30, 35, 40],
        'Score': [90, 85, 88, 92]}

df = pd.DataFrame(data)

# Afficher le DataFrame
print("DataFrame original:")
print(df)

# Ajouter une nouvelle colonne calculée
df['Score multiplié par 2'] = df['Score'] * 2

# Afficher le DataFrame après la modification
print("\nDataFrame après l'ajout de la colonne calculée:")
print(df)

# Utiliser numpy pour effectuer une opération sur une colonne
df['Nouveau Score'] = np.sqrt(df['Score'])

# Afficher le DataFrame après l'opération numpy
print("\nDataFrame après l'opération numpy sur la colonne Score:")
print(df)
