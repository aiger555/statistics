# Importing necessary librariesimport pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Sample data creation (replace this with actual data loading if required)data = {
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

# 1. Visualization: Histograms for Age, Work Experience, and Salary
plt.figure(figsize=(12, 6))

# Plotting the histograms
plt.subplot(1, 3, 1)
sns.histplot(df['Age'], kde=True, bins=10, color='blue')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
sns.histplot(df['Work Experience'], kde=True, bins=10, color='green')
plt.title('Histogram of Work Experience')
plt.xlabel('Work Experience (Years)')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
sns.histplot(df['Salary'], kde=True, bins=10, color='red')
plt.title('Histogram of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# 2. Box Plot to detect outliers in Salary
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Salary'], color='purple')
plt.title('Box Plot of Salary')
plt.xlabel('Salary')
plt.show()

# 3. Scatter plot to analyze correlation between Salary and Work Experience
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Work Experience'], y=df['Salary'], color='orange')
plt.title('Scatter Plot of Salary vs Work Experience')
plt.xlabel('Work Experience')
plt.ylabel('Salary')
plt.show()

# 4. Normality Test using Shapiro-Wilk Test for 'Salary'
shapiro_test_stat, shapiro_p_value = stats.shapiro(df['Salary'])
print(f"Shapiro-Wilk Test for Salary: Test Stat = {shapiro_test_stat}, p-value = {shapiro_p_value}")
if shapiro_p_value > 0.05:
    print("The data follows a normal distribution (Fail to reject H0).")
else:
    print("The data does not follow a normal distribution (Reject H0).")

# 5. Normality Test using Anderson-Darling Test for 'Work Experience'
anderson_test_result = stats.anderson(df['Work Experience'])
print(f"Anderson-Darling Test for Work Experience: Statistic = {anderson_test_result.statistic}")
for i in range(len(anderson_test_result.critical_values)):
    print(f"At significance level {anderson_test_result.significance_level[i]}%, critical value = {anderson_test_result.critical_values[i]}")
    if anderson_test_result.statistic < anderson_test_result.critical_values[i]:
        print("The data follows a normal distribution.")
    else:
        print("The data does not follow a normal distribution.")

# 6. Bar plot for 'Do They Like Their Job'
plt.figure(figsize=(6, 4))
sns.countplot(x='Do They Like Their Job', data=df, hue='Do They Like Their Job', palette='coolwarm', legend=False)
plt.title('Bar Plot: Do They Like Their Job')
plt.xlabel('Do They Like Their Job')
plt.ylabel('Count')
plt.show()

# 7. Pie Chart for 'Internship'
internship_counts = df['Internship'].value_counts()
plt.figure(figsize=(6, 6))
internship_counts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightgreen'], startangle=90)
plt.title('Pie Chart: Internship')
plt.ylabel('')
plt.show()

# 8. Grouped Bar Plot for 'Sphere' and 'Company'
plt.figure(figsize=(8, 6))
sns.countplot(x='Sphere', hue='Company', data=df, palette='Set2')
plt.title('Grouped Bar Plot: Sphere and Company')
plt.xlabel('Sphere')
plt.ylabel('Count')
plt.legend(title='Company')
plt.show()
