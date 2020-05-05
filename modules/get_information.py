""" Module for class : FaceitAPI """
import json
import requests


class FaceitAPI():
    """ Class for getting info from faceit.com """
    def __init__(self):
        """
        Initialization

        Agruments:
        api_token -- The api token used for the Faceit API (API Keys)
        """
        self.api_token = 'b25030d7-b331-4c47-a8d1-bfe02ab4800a'
        self.base_url = "https://open.faceit.com/data/v4"
        self.headers = {
            'accept': 'application/json',
            'Authorization': F'Bearer {self.api_token}'
        }

    def get_player_id(self, nickname):
        """ Get player_id by nickname """
        api_url = F"{self.base_url}/players?nickname={nickname}"
        res = requests.get(api_url, headers=self.headers)
        if res.status_code == 404:
            print("Wrong nickname")
        else:
            if res.status_code == 200:
                info = json.loads(res.content.decode('utf-8'))
                return info['player_id']
            else:
                print("Some error")
                return None