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
        if(url == ''):
            return 'Unable to Process'
        if url.lower().find(website.lower()) != -1:
            return "unverified"

    # if the entire list is searched with no matches
    return "verified"


"""Uses the WoT API to verify links."""


def verifySafety(url):
    # Builds a URL for the Web of Trust API to process
    api_url = 'http://api.mywot.com/0.4/public_link_json2?hosts='
    api_url = api_url + url + \
        '/&key=cccad4de0255e2519748244ddf4769090d229808'
    # Requests the information from WoT and converts it to a python dictionary
    wot_response = requests.get(api_url)
    wot_score = wot_response.json()
    wot_score = wot_score[url]

    print wot_score
    # 200 is success, 500 server error, 403 incorrect parameters/invalid
    # API key, 429, exceeded daily request quota
    if wot_response.status_code == 500:
        return 'server error'
    if wot_response.status_code == 429:
        return 'error, please try again later'
    if wot_score.has_key('blacklists'):
        return 'blacklisted for malware, phishing, or spam'
    if wot_score['0'][0] >= 80:
        return 'excellent'
    if wot_score['0'][0] >= 60:
        return 'good'
    if wot_score['0'][0] >= 40:
        return 'caution'
    if wot_score['0'][0] >= 20:
        return 'warning'
    if wot_score['0'][0] >= 0:
        return 'stay away'


def main():
    url = ''
    print verifyLink(url)


if __name__ == "__main__":
    main()
