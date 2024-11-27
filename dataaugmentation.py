import numpy as np
import pandas as pd
import random as rd

# load dataset
df = pd.read_excel('./datasets/eleve2eme.xlsx')
print(df.head)

# define data augmentation function
## Augment numeric columns
def augment_numeri(value, noise_factor=0.05):
    noise = np.random.uniform(-noise_factor, noise_factor)
    return round(value * (1 + noise), 1)

## Augment textual columns
def augment_text(text):
    synonyms = {
        'Developer': ['Ingenieur informatique', 'Fullstack developer', 'Securité ingenieur', 'Project manager', 'QA Testeur', 'Frontend developer'],
        'Médicin': ['Médicin Generaliste', 'Radiologiste', 'Médecin orthopédiste', 'Gynécologue', 'Nutritionniste', 'médecin neurologue'],
        'Chercheur': ['Professeur', 'Animatrice', 'Gestionaire ecole', 'Professeur universitaire'],
        'Écrivain': ['Chanteur', 'Danceur', 'peinture professionnelle', 'Acteur'],
        'Ingénieur': ['Mécanicien', 'Electricien', 'Genie civil', 'Architect', 'Chauffeur', 'Chef projet construction'],
        'Designer': ['Concepteur', 'Photographeur', 'Interior designed', 'Fashion designed']
    }
    words = text.split()
    for i, word in enumerate(words):
        if word in synonyms and rd.random() > 0.5:
            words[i] = rd.choice(synonyms[word])
    return ' '.join(words)

## Augment categorical columns 
def augment_categorical(value, choices, change_prod=0.3):
    categories = {
        'Genre': ['M', 'F'],
        'Niveau Scolaire': ['Deuxième'],
        'Comportement': ['Exemplaire', 'Correct', 'Moyen', 'Bon'],
        'Participation en Classe': ['Très bonne', 'Bonne', 'Moyenne', 'Excellente'],
        'Clubs/Associations': ['Club Informatique', 'Club Art', 'Club Sport', 'Club Science', 'Club Mathématiques'],
        'Projet humanitaire': ['Événement sportif', 'Projet humanitaire', 'Concours de dessin', 'Projet Robotique'],
        'Compétence Créativité': ['Moyenne', 'Très Élevée', 'Élevée'],
        'Certification Langue': ['Non', 'TOEFL', 'DELF B2'],
        'Certification Internationale': ['Non', 'Oui']
    }
    if rd.random() < change_prod:
        return rd.choice(choices)
    
# Removal of unessesary columns 
print("Shape: ", df.shape)
df = df.drop(['ID Élève', 'Nom/Prénom', 'Date Naissance'])