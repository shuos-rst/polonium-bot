import wolframalpha
from abc import ABC, abstractmethod
from commands.AbstractCommand import AbstractCommand

#this class is querying the wolfram alpha API
#https://wolframalpha.readthedocs.io/en/latest/?badge=latest#

class wolfram_alpha_search(AbstractCommand):


    def __init__(self, WOLFRAM_APP_ID):
        self.app_id = WOLFRAM_APP_ID
        self.client = wolframalpha.Client(self.app_id)
        return

    def execute(self, query):
        try:
            res = self.client.query(query)
            answer = next(res.results).text
            for pod in res.pods:
                print(pod.plaintext())
                #for sub in pod.subpods:
                #    print(sub.plaintext)
            return(answer) #this only returns the text from the query
        except:
            return('error')
