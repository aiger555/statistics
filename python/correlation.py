# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Sample data creation (replace this with actual data loading if required)
data = {
    'Name': ["Mohammad Imtiyaz Gulbarga", "Nurzhigit", "Kulpunai A.", "Talant", "Nemat", "Adina", "Kalicha", "Kanyshai",
             "Aiganym",
             "Аkinai", "Bermet", "Ranelia", "Guliza", "Nurbek", "Beksultan", "Anarbek", "Bektur", "Nuraly", "Diana",
             "Aigerim", "Aizirek I.",
             "Nurken", "Aruuke", "Aiperi", "Azamat", "Dina", "Meerim", "Viktor"],

    'Age': [31, 29, 28, 30, 36, 22, 22, 6, 21, 21, 22, 23, 39, 50, 17, 18, 21, 29, 25, 21, 20, 40, 17, 27, 21, 19, 29,
            20],

    'Gender': [
        "Мужской / male", "Мужской / male", "Женский / female", "Мужской / male", "Мужской / male", "Женский / female",
        "Женский / female", "Женский / female", "Женский / female", "Женский / female", "Женский / female",
        "Женский / female",
        "Женский / female", "Мужской / male", "Мужской / male", "Мужской / male", "Мужской / male", "Мужской / male",
        "Мужской / male", "Женский / female", "Женский / female", "Женский / female", "Мужской / male",
        "Женский / female",
        "Женский / female", "Женский / female", "Мужской / male", "Женский / female"
    ],

    'Company': ["AIU", "Mood coffee", "Mood coffee", "Этно кофе", "Кофейня", "Apex Global community",
                "Ала-тоо ресторан", "Vienna Hous", "Частная компания", "чип карт", "Optima bank", "В отеле",
                "Web wellness", "Электроламповый завод", "Capito кофейня", "Love Juice", "Гос.служба", "Exclusive.kg",
                "Таатан", "IT technologies", "Kaufhaus Martin Stolz", "Гос.больница", "Свой интернет магазин",
                "Sunlight",
                "Свой малый бизнес", "Apex", "Санлайт", "Свой цех"
                ],
    'Country': ["Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Singapore", "Kyrgyzstan",
                "Germany", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Dubai", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Germany", "Kazakhstan", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Remote", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan"
                ],
    'Sphere': ["Teaching", "Catering", "Catering", "Sales", "Cafeteria", "Education, trainings, HR", "Accounting",
               "Hospitality", "HR Management", "Card Manufacturing", "Banking", "Tourism", "Wellness", "Manufacturing",
               "Catering", "Catering", "Accounting", "Automotive", "Linguistics", "Sales", "Trade and Service",
               "Medicine, Surgery", "SMM", "Medicine", "Marketing", "Consultant-Marketing", "Dentistry", "Business"],

    'Work Experience': [10, 4, 3, 1, 3, 4, 0.5, 11, 1.5, 0.1, 0.2, 5, 5, 25,
                        3, 0.3, 2, 3.5, 4, 0.3, 0.3, 14, 2, 7, 1, 0.5, 10, 1],

    'Salary': [1500, 2300, 470, 700, 2300, 1000, 350, 1650, 410, 300,
               235, 600, 1400, 3000, 750, 600, 300, 1700, 500,
               240, 3500, 1200, 530, 1700, 760, 200,
               2000, 1100],

    'Hours of Work': ['5-6', '5-6', '12-13', '1-2', '7-8', '12', '7-8', '7-8', '7-8', '7-8',
                      '12', '9', '5-6', '7-8', '10', '7-8', '7-8', '7-8', '7-8', '7-8',
                      '7-8', '9-10', '7-8', '5-6', '10', '12', '7-8', '12'],

    'Do They Like Their Job': [
        "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes",
        "Да / Yes", "Да / Yes", "Нет / No", "Да / Yes", "Да / Yes", "Нет / No",
        "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes",
        "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes",
        "Да / Yes", "Да / Yes", "Нет / No", "Да / Yes"],

    'Internship': [
        "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes",
        "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes", "Да / Yes",
        "Да / Yes", "Нет / No", "Нет / No", "Нет / No", "Нет / No", "Да / Yes",
        "Нет / No", "Да / Yes", "Нет / No", "Да / Yes", "Нет / No", "Да / Yes",
        "Да / Yes", "Нет / No", "Да / Yes", "Нет / No"]

}
# Convert to DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the dataframe to inspect it
print(df.head())

# Correlation matrix
correlation_matrix = df[['Age', 'Work Experience', 'Salary']].corr()
print(correlation_matrix)

# Visualizing the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
