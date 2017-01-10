#Imported necessary components to make API Calls
import requests

#function: verifies links against zimdars lists
#params: a set of arrays containing all the info from scraping
#return: string unverified or verified
def verifyLink(url):
    #list of untrustworthy website
    zimdarsList=["100PercentFedUp.com","EnduringVision.com","21stCenturyWire.com","70news.wordpress.com","The Free Thought Project","Abcnews.com.co","Politicalo","ActivistPost.com","Addicting Info",
    "AmericanNews.com","AnonNews.co","Private-eye.co.uk","Huzlers","Indecision Forever","RealNewsRightNow.com","Bipartisan Report","Infowars.com","Red State","Blue Nation Review","Reductress",
    "Breitbart","RileNews.com","Call the Cops","Cap News","Sportspickle.com","ChristWire.org","The Free Thought Project","CivicTribune.com","Borowitz Report","ClickHole.com","The Onion",
    "CoastToCoastAM.com","The Other 98%","CollectiveEvolution","MediaMass.net","ConsciousLifeNews.com","MegynKelly.us","ConservativeOutfitters.com","MSNBC.com.co","ConspiracyWire (WideAwakeAmerica.com)",
    "MSNBC.website","CountdownToZeroTime.com","Naha Daily","NationalReport.net","CreamBMP.com","NaturalNews.com","Twitchy.com","News-Hound.com","NewsBiscuit.com","US Uncut","DCGazette.com","Newslo",
    "NewsMutiny.com","DrudgeReport.com.co","DuffleBlog.com","World News Daily Report","Empire News","Occupy Democrats"]
    #loop through every website on zimdar's list
    for website in zimdarsList:
        #if the url is found in zimdar's list
        if website.lower().find(url) != -1:
            return "unverified"


    #if the entire list is searched with no matches
    return "verified"

def verifySafety(url):
    #API key
    #cccad4de0255e2519748244ddf4769090d229808
    #otScores = requests.get(" http://api.mywot.com/0.4/public_link_json2?hosts=example.COM/www.EXAMPLE.NET/&callback=process&key=cccad4de0255e2519748244ddf4769090d229808")
	#below is for 1 URL
	wotScores = requests.get("http://api.mywot.com/0.4/public_link_json2=facebook.com/&callback=process&key=<cccad4de0255e2519748244ddf4769090d229808"
	#^had ... + url + ...
	if wotScores.blacklists != null
		return "blacklisted for malware, phishing, or spam"
		
	#200 is success, 500 server error, 403 incorrect parameters/invalid API key, 429, exceeded daily request quota
	if wotScores.status_code == 500
		return "server error"
	if wotScores.status_code == 403 || 429
		return "error, please try again later"
	if wotScores.target.0.r >= 80
		return "excellent"
	if wotScores.target.0.r >= 60
		return "good"
	if wotScores.target.0.r >= 40
		return "caution"
	if wotScores.target.0.r >= 20
		return "warning"
	if wotScores.target.0.r >= 0
		return "stay away"
	#requests.get should retrieve WoT scores like trustworthiness... compare with WoT scoring table
	#decide how to incorporate confidence rating
	
	
	
def main():
#enter URL below before testing
    url = "facebook.com"
    print (verifyLink(url)) #how result vs zimdarsList
    print (verifySafety(url)); #how result vs WoT