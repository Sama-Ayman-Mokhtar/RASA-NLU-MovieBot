from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionGetMovie(Action):

   def name(self) -> Text:
        return "action_get_movie"

   def run(self, dispatcher, tracker, domain):

       api_key = 'd8f07ca8ede10bebea055c594291db82'

       LangDict = {"Latin": 'la', "Turkish": 'tr', "French": 'fr', "Japanese": 'ja', "Hindi": 'hi',
                    "Arabic": 'ar', "Italian": 'it', "Russian": 'ru', "English": 'en', "Greek": 'el',
                    "German": 'de', "Spanish": 'es', "Korean": 'ko'}

       GenreDict = {"action": 28, "adventure": 12, "animation": 16, "comedy": 35, "crime": 80,
                    "documentry": 99, "drama": 18, "family": 10751, "fantasy": 14, "history": 36,
                    "horror": 27, "musical": 10402, "mystery": 9648, "romance": 10749,
                    "science fiction": 878, "TV movie": 10770, "thriller": 53, "war": 10752, "western": 37}
        

       genre = tracker.get_slot('genre')
       language = tracker.get_slot('language')
       year = tracker.get_slot('year')

       current = requests.get(
           'https://api.themoviedb.org/3/discover/movie?api_key={}&sort_by=vote_average.desc&include_adult=false&include_video=false&primary_release_date.gte={}-01-01&vote_count.gte=1000&with_genres={}&with_original_language={}&with_watch_monetization_types=flatrate'.format(
               api_key,year, GenreDict.get(genre), LangDict.get(language))).json()

      # current = requests.get(
          # 'https://api.themoviedb.org/3/discover/movie?api_key={}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres={}&with_watch_monetization_types=flatrate'.format(
             #  api_key, GenreDict.get(genre))).json()
        
               
       print(current['results'][0]['original_title'])

       response = """The movie currently recommended is {}.""".format(
           current['results'][0]['original_title'])

       dispatcher.utter_message(response)
       
       return [SlotSet('genre', genre)]

