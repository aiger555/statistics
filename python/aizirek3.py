# Importing necessary libraries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


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

# Simlpe linear reg
# Define independent variable (X) and dependent variable (Y)
X = df['Work Experience']
Y = df['Salary']

# Add a constant to the independent variable (for the intercept)
X = sm.add_constant(X)

# Perform the regression
model = sm.OLS(Y, X).fit()

# Print the summary of the regression
print(model.summary())

# Scatter plot and regression line for Salary vs. Work Experience
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Work Experience'], y=df['Salary'], color='blue')
sns.lineplot(x=df['Work Experience'], y=model.predict(X), color='red')  # Regression line
plt.title('Linear Regression: Salary vs. Work Experience')
plt.xlabel('Work Experience')
plt.ylabel('Salary')
plt.show()

# Residuals (errors)
residuals = model.resid

# Plotting residuals to check for homoscedasticity
plt.figure(figsize=(8, 6))
sns.scatterplot(x=model.fittedvalues, y=residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs Fitted Values')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.show()

# Plotting the histogram of residuals to check for normality
plt.figure(figsize=(8, 6))
sns.histplot(residuals, kde=True, color='purple')
plt.title('Histogram of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

