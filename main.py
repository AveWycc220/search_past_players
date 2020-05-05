from modules.get_information import FaceitAPI

API = FaceitAPI()
player_id = API.get_player_id("Ave_Wycc220")
print(player_id)
