import requests,lxml,urllib.request,re,json
from lxml import html

#store important resources so they can be easily called
class Resources():
    locationXpath = '//*[@id="page"]/tbody/tr[3]/td/table/tbody/tr/td[1]/table[7]/tbody/tr[5]/td[2]'
    locationUrl = "https://www.infobyip.com/"
    rainingXpath = '/html/body/div/div/div[1]/h1//text()'
    rainingUrl = "https://isitraining.in/"
    
#Get the users GeoLocation so that we can check their specific area for rain
def GetLocation():
    location = None
    with urllib.request.urlopen("https://geoip-db.com/json") as url:
        data = json.loads(url.read().decode())
        location = data['city']
    IsItRaining(location)
#Check if is raining wherever the user is located
def IsItRaining(location):
    location = location.replace(" ", "-")
    url = Resources.rainingUrl + location
    pageContent=requests.get(url, headers = {'User-agent': 'Location'})
    tree = html.fromstring(pageContent.content)
    caption = tree.xpath(Resources.rainingXpath)
    if "No" in caption:
        print ("It's not currently raining in %s" % location)
    else:
        print ("It's currently raining in %s" % location)

GetLocation()
