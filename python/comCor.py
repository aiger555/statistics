# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Sample data creation (replace this with actual data loading if required)
data = {
    'Name': [
             "Aigerim", "Priyanka Khan", "Aiperi", "Madina Shakeeva", "Karachach", "Galina Kim",
             "Dinara", "Aigerim", "Gulshayir Samatova", "Tamerlan", "Saikal", "Rafhat",
             "Dilbara", "Yuliya", "Jibek", "Gulnaz", "Cholpon", "Begimai", "Guliza",
             "Anipa Samatova", "Kubanych", "Asylbek", "Nurbek", "Aigul Beisheeva","Mohammad Imtiyaz Gulbarga",
             "Nurzhigit", "Kulpunai A.", "Talant", "Nemat", "Adina", "Kalicha", "Kanyshai",
             "Aiganym", "Аkinai", "Bermet", "Ranelia", "Guliza", "Nurbek", "Beksultan", "Anarbek", "Bektur", "Nuraly", "Diana",
             "Aigerim", "Aizirek I.", "Nurken", "Aruuke", "Aiperi", "Azamat", "Dina", "Meerim", "Viktor"],

    'Age': [22, 20, 21, 20, 30, 19, 31, 21, 30, 22, 19, 20, 20, 20, 19, 22, 38, 36, 34, 40, 38, 30, 34, 35,
            31, 29, 28, 30, 36, 22, 22, 6, 21, 21, 22, 23, 39, 50, 17, 18, 21, 29, 25, 21, 20, 40, 17, 27,
            21, 19, 29, 20],

    'Gender': [
               "Женский / female", "Женский / female", "Женский / female", "Женский / female",
               "Женский / female","Женский / female", "Женский / female", "Женский / female", "Женский / female", #9
               "Мужской / male", "Женский / female", "Мужской / male",
               "Женский / female", "Женский / female", "Женский / female", "Женский / female", "Женский / female",
               "Женский / female", "Женский / female", "Женский / female", #8
               "Мужской / male", "Мужской / male", "Мужской / male", "Женский / female",
               "Мужской / male", "Мужской / male", "Женский / female", "Мужской / male", "Мужской / male", "Женский / female",
               "Женский / female", "Женский / female", "Женский / female", "Женский / female", "Женский / female",
               "Женский / female", "Женский / female", "Мужской / male", "Мужской / male", "Мужской / male", "Мужской / male", "Мужской / male",
               "Женский / female", "Женский / female", "Женский / female",
               "Мужской / male", "Женский / female", "Женский / female", "Мужской / male", "Женский / female", "Женский / female", "Мужской / male"
    ],

    'Company': ["Malaysia IT", "INDUStrix", "Saratan", "The Canvas Hotel Dubai", "Ayten",
                "NURTelecom", "Умра компания «Ибрахим тревел»", "в мбанк", "Международный университет Ала-Тоо",
                "Не работаю", "Enactus KG, Mercy Corps KG", "Северсталь", "A1 Cometa",
                "Продавец-консультант в оптике Jops", "online technology", "Ala-too university",
                "Lights Academy International school", "OpsWorks", "Кафе", "Сапат учреждение",
                "Отель", "Бизнес Ассоциация", "ОАО Кыргызнефтегаз", "Ала-Тоо Университет","AIU", "Mood coffee", "Mood coffee", "Этно кофе", "Кофейня", "Apex Global community",
                "Ала-тоо ресторан", "Vienna Hous", "Частная компания", "чип карт", "Optima bank", "В отеле",
                "Web wellness", "Электроламповый завод", "Capito кофейня", "Love Juice", "Гос.служба", "Exclusive.kg",
                "Таатан", "IT technologies", "Kaufhaus Martin Stolz", "Гос.больница", "Свой интернет магазин",
                "Sunlight", "Свой малый бизнес", "Apex", "Санлайт", "Свой цех"
                ],
    'Country': ["Malaysia", "India", "Kyrgyzstan", "Dubai", "Kyrgyzstan", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan",
                "Russia", "Bishkek", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan",#22
                "Kyrgyzstan", "Kyrgyzstan","Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Singapore", "Kyrgyzstan",
                "Germany", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Dubai", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Germany", "Kazakhstan", "Kyrgyzstan",
                "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan", "Remote", "Kyrgyzstan", "Kyrgyzstan", "Kyrgyzstan"
                ],
    'Sphere': ["Data Engineer", "IT", "Marketing", "Marketing", "IT", "IT",
               "Бухгалтерия", "IT", "Education", "IT", "SMM", "IT", "Frontend",
               "Sales", "Retail Sales", "Education", "Education", "Remote",
               "Общепит", "Образование", "Гостиница", "НКО", "Добыча нефти", "Образование","Teaching", "Catering", "Catering", "Sales", "Cafeteria", "Education, trainings, HR", "Accounting",
               "Hospitality", "HR Management", "Card Manufacturing", "Banking", "Tourism", "Wellness", "Manufacturing", "Catering", "Catering",
               "Accounting", "Automotive", "Linguistics", "Sales", "Trade and Service",
               "Medicine, Surgery", "SMM", "Medicine", "Marketing", "Consultant-Marketing", "Dentistry", "Business"],

    'Work Experience': [2, 2, 0.02, 0.8, 2, 1.2, 8, 0.1, 6, 0.6,
                        2, 0.3, 0.03, 2, 0.3, 3, 7, 12, 15, 18,
                        5, 4, 12, 13, 10, 4, 3, 1, 3, 4,
                        0.5, 11, 1.5, 0.1, 0.2, 5, 5, 25, 3, 0.3,
                        2, 3.5, 4, 0.3, 0.3, 14, 2, 7, 1, 0.5, 10, 1],

    'Salary': [2000, 1000, 100, 700, 1000, 700, 800, 400, 580, 500,
               580, 300, 0, 410, 300, 400, 600, 1100, 1500, 580,
               300, 700, 1500, 500, 1500, 2300, 470, 700, 2300, 1000,
               350, 1650, 410, 300, 235, 600, 1400, 3000, 750, 600,
               300, 1700, 500, 240, 3500, 1200, 530, 1700, 760, 200,
               2000, 1100],

    'Hours of Work': ["7-8", "5-6", "3-4", "7-8", "7-8", "7-8", "7-8", "7-8", "7-8","1-2",
                      "3-4", "10", "1-2", "12", "7-8", "24", "7-8", "7-8", "12", "7-8",
                      "14", "7-8", "7-8", "7-8", '5-6', '5-6', '12-13', '1-2', '7-8', '12',
                      '7-8', '7-8', '7-8', '7-8', '12', '9', '5-6', '7-8', '10', '7-8',
                      '7-8', '7-8', '7-8', '7-8', '7-8', '9-10', '7-8', '5-6', '10', '12', '7-8', '12'],

    'Do They Like Their Job': [
        "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
        "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
        "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
        "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes",
        "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes","Yes", "Yes", "No", "Yes"],

    'Internship': [
        "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes",
        "Yes", "No", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "Yes",
        "No", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
        "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "No", "No",
        "No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes",
        "Yes", "No", "Yes", "No"]

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
