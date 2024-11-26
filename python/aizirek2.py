# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Sample data creation (replace this with actual data loading if required)

data = {
    'Name': ["Aigerim", "Priyanka Khan", "Aiperi", "Madina Shakeeva", "Karachach", "Galina Kim",
             "Dinara", "Aigerim", "Gulshayir Samatova", "Tamerlan", "Saikal", "Rafhat",
             "Dilbara", "Yuliya", "Jibek", "Gulnaz", "Cholpon", "Begimai", "Guliza",
             "Anipa Samatova", "Kubanych", "Asylbek", "Nurbek", "Aigul Beisheeva"],

    'Age': [22, 20, 21, 20, 30, 19, 31, 21, 30, 22, 19, 20, 20, 20, 19, 22, 38, 36, 34, 40, 38, 30, 34, 35],

    'Gender': ["Женский / female", "Женский / female", "Женский / female", "Женский / female",
               "Женский / female", "Женский / female", "Женский / female", "Женский / female", "Женский / female",
               "Мужской / male", "Женский / female", "Мужской / male",
               "Женский / female", "Женский / female", "Женский / female", "Женский / female", "Женский / female",
               "Женский / female", "Женский / female", "Женский / female",
               "Мужской / male", "Мужской / male", "Мужской / male", "Женский / female"],

    'Company': ["Malaysia IT", "INDUStrix", "Saratan", "The Canvas Hotel Dubai", "Ayten",
                "NURTelecom", "Умра компания «Ибрахим тревел»", "в мбанк", "Международный университет Ала-Тоо",
                "Не работаю", "Enactus KG, Mercy Corps KG", "Северсталь", "A1 Cometa",
                "Продавец-консультант в оптике Jops", "online technology", "Ala-too university",
                "Lights Academy International school", "OpsWorks", "Кафе", "Сапат учреждение",
                "Отель", "Бизнес Ассоциация", "ОАО Кыргызнефтегаз", "Ала-Тоо Университет"],

    'Country': ["Malaysia", "India", "Kyrgyzstan", "Dubai", "Kyrgyzstan", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan",
                "Russia", "Bishkek", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan"],

    'Sphere': ["Data Engineer", "IT", "Marketing", "Marketing", "IT", "IT",
               "Бухгалтерия", "IT", "Education", "IT", "SMM", "IT", "Frontend",
               "Sales", "Retail Sales", "Education", "Education", "Remote",
               "Общепит", "Образование", "Гостиница", "НКО", "Добыча нефти", "Образование"],

    'Work Experience': [2, 2, 0.02, 0.8, 2, 1.2, 8, 0.1, 6, 0.6, 2, 0.3, 0.03, 2, 0.3, 3, 7, 12, 15, 18, 5, 4, 12, 13],

    'Salary': [2000, 1000, 100, 700, 1000, 700, 800, 400, 580, 500,
               580, 300, 0, 410, 300, 400, 600, 1100, 1500, 580, 300, 700, 1500, 500],

    'Hours of Work': ["7-8", "5-6", "3-4", "7-8", "7-8", "7-8", "7-8", "7-8", "7-8",
                      "1-2", "3-4", "10", "1-2", "12", "7-8", "24", "7-8", "7-8", "12", "7-8", "14", "7-8", "7-8",
                      "7-8"],

    'Do They Like Their Job': ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
                               "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
                               "Yes"],

    'Internship': ["Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes",
                   "Yes", "No", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "Yes", "No", "No", "Yes", "Yes"]
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
