"""Verifies URLs Passed from Extension."""
# Imported necessary components to make API Calls
import requests

api_key = 'cccad4de0255e2519748244ddf4769090d229808'
# function: verifies links against zimdars lists
# params: a set of arrays containing all the info from scraping
# return: string unverified or verified


def verifyLink(url):
    # list of untrustworthy website
    zimdarsList = ["100PercentFedUp.com", "EnduringVision.com", "21stCenturyWire.com", "70news.wordpress.com", "The Free Thought Project", "Abcnews.com.co", "Politicalo", "ActivistPost.com", "Addicting Info",
                   "AmericanNews.com", "AnonNews.co", "Private-eye.co.uk", "Huzlers", "Indecision Forever", "RealNewsRightNow.com", "Bipartisan Report", "Infowars.com", "Red State", "Blue Nation Review", "Reductress",
                   "Breitbart", "RileNews.com", "Call the Cops", "Cap News", "Sportspickle.com", "ChristWire.org", "The Free Thought Project", "CivicTribune.com", "Borowitz Report", "ClickHole.com", "The Onion",
                   "CoastToCoastAM.com", "The Other 98%", "CollectiveEvolution", "MediaMass.net", "ConsciousLifeNews.com", "MegynKelly.us", "ConservativeOutfitters.com", "MSNBC.com.co", "ConspiracyWire (WideAwakeAmerica.com)",
                   "MSNBC.website", "CountdownToZeroTime.com", "Naha Daily", "NationalReport.net", "CreamBMP.com", "NaturalNews.com", "Twitchy.com", "News-Hound.com", "NewsBiscuit.com", "US Uncut", "DCGazette.com", "Newslo",
                   "NewsMutiny.com", "DrudgeReport.com.co", "DuffleBlog.com", "World News Daily Report", "Empire News", "Occupy Democrats"]
    # loop through every website on zimdar's list
    for website in zimdarsList:
        # if the url is found in zimdar's list
        if website.lower().find(url.lower()) != -1:
            return "unverified"

    # if the entire list is searched with no matches
    return "verified"


"""Uses the WoT API to verify links."""


def verifySafety(url):
    #Builds a URL for the Web of Trust API to process
    api_url = 'http://api.mywot.com/0.4/public_link_json2?hosts='
    api_url = api_url + url + \
        '/&key=cccad4de0255e2519748244ddf4769090d229808'
    #Requests the information from WoT and converts it to a python dictionary
    json_data = requests.get(api_url).json()

    return json_data


def main():
    url = 'facebook.com'
    print verifySafety(url)


if __name__ == "__main__":
    main()
