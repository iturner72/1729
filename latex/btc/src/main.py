#import requests
#import seaborn as sns
#import pandas as pd
#from matplotlib import pyplot as plt
#import numpy as np
#
#data_url = "https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/4_ThreeNum.csv"
#
#r = requests.get(data_url)
#
#with open("gdp-life.txt", "w") as f:
#    f.write(r.text)
#
#df = pd.read_csv("gdp-life.txt")
#print(df.head())
#
#print("___")
#print("The correlation is: ", np.corrcoef(df["gdpPercap"], df["lifeExp"])[0, 1])
#print("___")
#
#sns.lmplot("gdpPercap", "lifeExp", df).set_axis_labels(
#    "Life expectancy", "GDP per capita"
#)
#
#plt.title("People live longer in richer countries")
#plt.tight_layout()
#plt.show()
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
import requests
from bs4 import BeautifulSoup

def scrape_data(url):

    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find_all('table')[1]

    rows = table.select('tbody > tr')

    header = [th.text.rstrip() for th in rows[1].find_all('th')]

    with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in rows[1:]:
            data = [th.text.rstrip() for th in row.find_all('td')]
            writer.writerow(data)

if __name__=="__main__":
    url = "https://en.wikipedia.org/wiki/Lists_of_Olympic_medalists"
    scrape_data(url)
