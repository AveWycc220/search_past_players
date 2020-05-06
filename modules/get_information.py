""" Module for class : FaceitAPI """
import json
import environ
import requests

root = environ.Path(__file__)
env = environ.Env()
env.read_env(env_file='modules/setting_api.env')

class FaceitAPI():
    """ Class for getting info from faceit.com """
    def __init__(self):
        """
        Initialization

        Agruments:
        api_token -- The api token used for the Faceit API (Your API Keys)
        """
        self.__api_token = env.str('API_KEY')
        self.__base_url = "https://open.faceit.com/data/v4"
        self.__headers = {
            'accept': 'application/json',
            'Authorization': F'Bearer {self.__api_token}'
        }

    @staticmethod
    def get_players_names(room_id):
        """ Function for getting players_name from room """
        res = requests.get(F"https://chat-server.faceit.com/v4/meta/match-{room_id}")
        if res.status_code == 404:
            print("Wrong room_id")
        else:
            if res.status_code == 200:
                player_names = json.loads(res.content.decode('utf-8'))
                list_player_name = list()
                for i in range(0, 10):
                    list_player_name.append(player_names['members'][i]['v']['n'])
                return list_player_name
            else: 
                print(F"Error : {res.status_code}")
                return None

    def get_player_id(self, nickname):
        """ Get player_id by nickname """
        api_url = F"{self.__base_url}/players?nickname={nickname}"
        res = requests.get(api_url, headers=self.__headers)
        if res.status_code == 404:
            print("Wrong nickname")
        else:
            if res.status_code == 200:
                info = json.loads(res.content.decode('utf-8'))
                return info['player_id']
            else:
                print(F"Error : {res.status_code}")
                return None