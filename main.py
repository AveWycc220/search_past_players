from modules.get_information import FaceitAPI
from datetime import datetime

start_time = datetime.now()
API = FaceitAPI()
print(API.get_past_matches_url('1-abbebee1-f59a-4689-84de-5c3a41a254c4', 'Ave_Wycc220'))
print(datetime.now() - start_time)