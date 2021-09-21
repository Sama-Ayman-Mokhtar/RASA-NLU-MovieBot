# RASA-NLU-MovieBot

## Contributors
- Haidy Ahmed
- Salma Ehab
- Sama Ayman
- Yasmin Haitham

## Setup
Create a virtual environment with python 3.6, 3.7, or 3.8 version. Then, activate it.
```
conda create -n [envName] python=3.8 anaconda
activate rasa
```
Install Rasa
```
pip install rasa
```
Change these files to modify the bot's behavior -if needed.
- nlu.yml
- domain.yml
- stories.yml
- actions.py

Train and Test the model
```
rasa train
rasa shell nlu
```
Uncomment the following lines in the ```endpoints.yml``` file
```
action_endpoint:
  url: "http://localhost:5055/webhook"
```  

Run the bot
```
rasa run actions
rasa shell
```

## Sample Output

![action_french](https://user-images.githubusercontent.com/54854067/134097873-9839175a-0630-41e1-95d8-9bc38621e87b.PNG)

![German_mystery](https://user-images.githubusercontent.com/54854067/134097975-e8b7ff01-309f-446c-89b1-d867d734bdda.PNG)

![horror_Italian](https://user-images.githubusercontent.com/54854067/134097992-74661403-c9b9-4ab5-a9b5-2c3d185e2404.PNG)

![fantasy_english](https://user-images.githubusercontent.com/54854067/134097875-561fda93-f9de-4b3c-b6c6-90cee4f15450.PNG)

## Reference

https://www.geeksforgeeks.org/chatbots-using-python-and-rasa/
