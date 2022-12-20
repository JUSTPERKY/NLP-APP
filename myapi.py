
# Import
import paralleldots as pdo
# Setting API key
class API:

    def __init__(self):
        pdo.set_api_key('1nfltKiMeKZfKWe7SgzwfT6A2XfOstJivQXQ2UN8r60')

    def sentiment_analysis(self,text):
        response = pdo.sentiment(text)
        return response

    def abuse_analysis(self,text):
        response = pdo.abuse(text)
        return response

    def emotion_analysis(self,text):
        response = pdo.emotion(text)
        return response





