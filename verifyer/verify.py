"""Verifies URLs Passed from Extension."""
# Imported necessary components to make API Calls
import requests

api_key = 'cccad4de0255e2519748244ddf4769090d229808'
# function: verifies links against zimdars lists
# params: a set of arrays containing all the info from scraping
# return: a dictionary of values
response = {'status': '', 'wotinfo': ''}


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
        if url == '' or url == None:
            return 'Unable to Process'
        elif url.lower().find(website.lower()) != -1:
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
    # Check to see if WoT has shortened the URL to the base.
    if wot_score.has_key(u'' + url):
        wot_score = wot_score[u'' + url]
    #Find the shortened URL
    else:
        #The list of keys in the wot_score dictionary
        wot_keys = wot_score.keys()
        for key in wot_keys:
            if url.lower().find(key):
                #The key at the index of the shortened url
                shortened_url = wot_keys[wot_keys.index(key)]
                wot_score = wot_score[u'' + shortened_url]
                break

    # 200 is success, 500 server error, 403 incorrect parameters/invalid
    # API key, 429, exceeded daily request quota
    #Checks to see if   wot_score is a dictionary and if it has a score
    if isinstance(wot_score, dict) and wot_score.has_key(u'0'):
        if wot_response.status_code == 500:
            response['wotinfo'] = 'server error'
            return response['status']
        elif wot_response.status_code == 429:
            response['wotinfo'] = 'error, please try again later'
            return response['status']
        elif wot_score.has_key('blacklists'):
            response['wotinfo'] = 'blacklisted for malware, phishing, or spam'
            return 'unverified'
        elif wot_score[u'0'][0] >= 80:
            response['wotinfo'] = 'excellent'
            return 'verified'
        elif wot_score[u'0'][0] >= 60:
            response['wotinfo'] = 'good'
            return 'verified'
        elif wot_score[u'0'][0] > 50:
            response['wotinfo'] = 'caution'
            return 'verified'
        elif wot_score[u'0'][0] >= 0:
            response['wotinfo'] = 'stay away'
            return 'unverified'
    #If website has never been reviewed by WoT, then display this
    else:
        response['wotinfo'] = 'caution: unknown website'
        return response['status']


def main(url):
    response['status'] = verifyLink(url)
    if response['status'] == 'verified' and url != '' and url != None:
        print 'Test'
        #response['status'] = verifySafety(url)

    return response


def debug(url):
    # Enter function to debug
    print 'Hello!'

if __name__ == "__main__":
    main("latimes.com")
    print response
