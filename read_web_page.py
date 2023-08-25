import requests 
from bs4 import BeautifulSoup

# data form 
# pagina: domenii
# cod: 48190392
# captcha: dew
# B1: VIZUALIZARE

# URL of the target page
search_url = 'https://mfinante.gov.ro/domenii/informatii-contribuabili/persoane-juridice/info-pj-selectie-dupa-cui'
sorter_url = 'https://www.google.com/'#'https://mfinante.gov.ro/apps/infocodfiscal.html'
destination_url ='https://mfinante.gov.ro/apps/infocodfiscal.html;jsessionid=ztHxEIUcR8-o3JqG_Osi727iZvHZWsWoZrgoo9jo.apps4'



# # Sample data for ID and CAPTCHA (replace with actual data)
id_value = '48190392' #"your_id_here"
captcha_value = "captcha_solution_here"

# Set up the session
with requests.Session() as s:
    # Perform an initial request to retrieve the page content
    response = s.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(response)
    
# # Find the ID input element by class name and set its value
# id_input = soup.find('input', class_='form2')
# if id_input:
#     id_input['value'] = id_value

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

