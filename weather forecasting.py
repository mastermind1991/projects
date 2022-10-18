#weather report
#importing BeautifulSoup Library
from bs4 import BeautifulSoup
#importing requests
import requests

#header user agent is a string allows the server to identify the OS and application
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


#define the weather function
def weather(city):
    city = city.replace(" ","+")
    #Requests and get function to get the information from the url provided
    res=requests.get(f'https://www.google.com/search?q={city}&oq={city}'
                f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid='
                       f'chrome&ie=UTF-8',headers=headers)
    #searches the information from google                   
    print("Searching in google.....\n")

    #navigates on that particular website, extract and store the data in a soup object
    soup = BeautifulSoup(res.text,'html.parser')

    #get the information of location
    location = soup.select('#wob_loc')[0].getText().strip()

    #gets the information of time
    time = soup.select('#wob_dts')[0].getText().strip()

    #gets the desired information
    info = soup.select('#wob-dc')[0].getText().strip()

    #gets the weather information
    weather = soup.select('#wob-tm')[0].getText().strip()

    #prints location
    print(location)

    #prints time
    print(time)

    #prints info
    print(info)

    #prints the weather in degree celsius
    print(weather+"°C")

    #enter the city name
    print("enter the city name")
    city = input()

    #concatenating the city name and weather
    city = city+"weather"
weather('houston')








