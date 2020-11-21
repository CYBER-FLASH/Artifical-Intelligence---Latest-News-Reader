""""
    This is Artifical Intelligence News Reader......
           Created By Junaid Ahmed -----------

"""


"""
pip install pywin32
pip install newsapi
pip install requests
pip install json

"""



def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)



if __name__ == '__main__':
    from newsapi import NewsApiClient
    speak("welcome sir - This is BBC News. Created By Mister HACKER")


    newsapi = NewsApiClient(api_key='7067179f741445b0b6fd8ebdbfda452e')

    news_source = newsapi.get_sources()
    for source in news_source['sources']:
        print('News Channel Name:', source['name'], )
        # speak(source['name'])

    print("\n\n")
    print("\t\t\t======= DAILY LATEST NEWS PAPER =======")
    print("\n\n")
    top_headline = newsapi.get_top_headlines(q='world war', language='en')

    for article in top_headline['articles']:
        print('Publish Date: ', article['publishedAt'])
        print('Title:', article['title'])
        print('Description: ', article['description'], '\n\n')



    all_article = newsapi.get_everything(q='world war', language='en')

    for article in all_article['articles']:
        print('Source: ', article['source']['name'])
        print('Publish Date: ', article['publishedAt'])
        print('Title: ', article['title'])
        print('Description: ', article['description'], '\n\n')
        speak(article['source']['name'])
        speak(article['title'])
        speak(article['description'])
        speak("Next news")
speak("Thanx for Listing sir")