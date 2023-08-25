import requests 
from bs4 import BeautifulSoup

# data form 
# pagina: domenii
# cod: 48190392
# captcha: dew
# B1: VIZUALIZARE

# URL of the target page
search_url = 'https://mfinante.gov.ro/despre-minister'
sorter_url = 'https://mfinante.gov.ro/apps/infocodfiscal.html'
destination_url ='https://mfinante.gov.ro/apps/infocodfiscal.html;jsessionid=ztHxEIUcR8-o3JqG_Osi727iZvHZWsWoZrgoo9jo.apps4'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
}

# # Sample data for ID and CAPTCHA (replace with actual data)
id_value = '48190392' #"your_id_here"
captcha_value = "captcha"

716

try:
    # Set up the session
    with requests.Session() as s:
        # Perform an initial request to retrieve the page content
        response = s.get(sorter_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        # s.raise_for_status()
        
except requests.exceptions.HTTPError as e:
    print (e.response.text)
    
# Find the ID input element by class name and set its value
id_input = soup.find('input', class_='form2')
if id_input:
    id_input['value'] = id_value

print(id_input)
# # Find the CAPTCHA input element by class name and set its value
# captcha_input = soup.find('input', name='captcha')
# if captcha_input:
#     captcha_input['value'] = captcha_value


# # Submit the form
# form = soup.find('submit')
# if form:
#    response = s.post(sorter_url, data=form)

# # Parse and extract the result
# result_soup = BeautifulSoup(response.content, 'html.parser')
# result_data = result_soup.find('div', {'id': 'content'})

# if result_data:
#     print(result_data.get_text())
# else:
#     print('No result data found.')

