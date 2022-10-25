import sqlite3
import requests
import threading
from bs4 import BeautifulSoup
import re

URL = "https://realpython.github.io/fake-jobs/"

web_page = requests.get(URL)

print(web_page.text)

soup = BeautifulSoup(web_page.content, 'html.parser')

results = soup.find(id="ResultsContainer")

print(results.prettify())

jobs = results.find_all("div", class_="card-content")

for job in jobs:
    print(job)

for job in jobs:
    company_element = job.find("h3", class_="company")
    title_element = job.find("h2", class_="title")
    print(company_element)
    print(title_element)
    print()

company_names = results.find_all("h3")

titles = results.find_all("h2")

for title in titles:
    print(title.text)

for company in company_names:
    print(company.text)

python_titles = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

for titles in python_titles:
    print(titles.text)

keys = ['Payne, Roberts and Davis',
        'Vasquez-Davidson',
        'Jackson, Chambers and Levy',
        'Savage-Bradley',
        'Ramirez Inc',
        'Rogers-Yates',
        'Kramer-Klein',
        'Meyers-Johnson'
        'Hughes-Williams'
        'Jones, Williams and Villa'
        'Garcia PLC',
        'Gregory and Sons',
        'Clark, Garcia and Sosa',
        'Bush PLC',
        'Salazar-Meyers',
        'Parker, Murphy and Brooks',
        'Cruz-Brown',
        'Macdonald-Ferguson',
        'Williams, Peterson and Rojas',
        'Smith and Sons',
        'Moss, Duncan and Allen',
        'Gomez-Carroll',
        'Manning, Welch and Herring',
        'Lee, Gutierrez and Brown',
        'Davis, Serrano and Cook',
        'Smith LLC',
        'Thomas Group',
        'Silva-King',
        'Pierce-Long',
        'Walker-Simpson',
        'Cooper and Sons',
        'Donovan, Gonzalez and Figueroa',
        'Morgan, Butler and Bennett',
        'Snyder-Lee',
        'Harris PLC',
        'Washington PLC',
        'Brown, Price and Campbell',
        'Mcgee PLC',
        'Dixon Inc',
        'Thompson, Sheppard and Ward',
        'Adams-Brewer',
        'Schneider-Brady',
        'Gonzales-Frank',
        'Smith-Wong',
        'Pierce-Herrera',
        'Aguilar, Rivera and Quinn',
        'Lowe, Barnes and Thomas',
        'Lewis, Gonzalez and Vasquez',
        'Taylor PLC',
        'Oliver, Jones and Ramirez'
        'Rivera and Sons',
        'Garcia PLC',
        'Johnson, Wells and Kramer',
        'Gonzalez LLC',
        'Morgan, White and Macdonald',
        'Robinson-Fitzpatrick',
        'Waters, Wilson and Hoover',
        'Hill LLC',
        'Li-Gregory',
        'Fisher, Ryan and Coleman',
        'Stewart-Alexander',
        'Abbott and Sons',
        'Bryant, Santana and Davenport',
        'Smith PLC',
        'Patterson-Singh',
        'Martinez-Berry',
        'May, Taylor and Fisher',
        'Bailey, Owen and Thompson',
        'Vasquez Ltd',
        'Leblanc LLC',
        'Jackson, Ali and Mckee',
        'Blankenship, Knight and Powell',
        'Patton, Haynes and Jones',
        'Wood Inc',
        'Collins Group',
        'Flores-Nelson',
        'Mitchell, Jones and Olson',
        'Howard Group',
        'Kramer-Edwards',
        'Berry-Houston',
        'Mathews Inc',
        'Riley-Johnson',
        'Spencer and Sons',
        'Camacho-Sanchez',
        'Oliver and Sons',
        'Eaton PLC',
        'Stanley-Frederick',
        'Bradley LLC',
        'Parker, Goodwin and Zavala',
        'Kim-Miles',
        'Moreno-Rodriguez',
        'Brown-Ortiz',
        'Hartman PLC',
        'Brooks Inc',
        'Washington-Castillo',
        'Nguyen, Yoder and Petty',
        'Holder LLC',
        'Yates-Ferguson',
        'Ortega-Lawrence',
        'Fuentes, Walls and Castro']

values = ['Senior Python Developer',
          'Software Engineer (Python)'
          'Python Programmer (Entry-Level)'
          'Python Programmer (Entry-Level)'
          'Software Developer (Python)'
          'Python Developer'
          'Back-End Web Developer (Python, Django)'
          'Back-End Web Developer (Python, Django)'
          'Python Programmer (Entry-Level)'
          'Software Developer (Python)']

new_keys = list(set(keys))

titles_in_python = dict({"Titles": values})

companies_in_python = dict({"Companies": new_keys})

jobs_in_python = {**companies_in_python, **titles_in_python}
print(jobs_in_python)

result_url = re.findall('[0-9]', URL)
print(result_url)


def db_establish(company, title):
    conn = sqlite3.connect('Python_jobs.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS JOBS(
                           JOB_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           JOB_TITLE VARCHAR(45),
                           COMPANY VARCHAR(45)); """)


threads = []
thread_connection_1 = threading.Thread(target=db_establish, args=['Savage-Bradley', 'Senior Python Developer'])
thread_connection_2 = threading.Thread(target=db_establish, args=['Salazar-Meyers', 'Software Engineer (Python)'])
thread_connection_3 = threading.Thread(target=db_establish, args=['Smith and Sons', 'Python Programmer (Entry-Level)'])
thread_connection_1.start()
thread_connection_2.start()
thread_connection_3.start()