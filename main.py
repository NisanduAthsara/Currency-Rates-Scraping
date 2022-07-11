from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

def getCurrencyRates():
    html_content = requests.get('https://www.seylan.lk/exchange-rates').text
    soup = BeautifulSoup(html_content,'lxml')
    table = soup.find('table',class_='table-style-4').tbody
    rows = table.find_all('tr')

    currency_types = ('USD','GBP','EUR','JPY','CHF','AUD','CAD','SGD')
    date = datetime.now()
    today = date.strftime("%b %d, %Y")
    formated_name = date.strftime("%Y-%m-%d")

    with open(f"logs/{formated_name}.txt","w") as file:
        file.write(f"---------  {today} Currency Rates  ---------\n\n")
        for row in rows:
            cols = row.find_all('td')
            currency_type = cols[1].text.strip()
            if currency_type in currency_types:
                currency_name = cols[0].text.strip()
                buying_rate = float(cols[2].text.strip())
                selling_rate = float(cols[3].text.strip())
                buying_rate = str(round(buying_rate,2))
                selling_rate = str(round(selling_rate,2))
                file.write(f"# {currency_name} ({currency_type})\n")
                file.write(f"Buying : Rs.{buying_rate}\n")
                file.write(f"Selling : Rs.{selling_rate}\n\n")

    print(f'File {formated_name}.txt wrote successfully...!')            

if __name__ == '__main__':
    while True:
        getCurrencyRates()
        sleeping_time = 60*60*24
        time.sleep(sleeping_time)       