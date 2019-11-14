import json

from mood_model.mood_neural_network import MoodNeuralNetwork

baseModel = MoodNeuralNetwork()
emotions = baseModel.getEmotions()
emotion_map = {}
for i in range(len(emotions)):
    emotion_map[emotions[i]] = i

with open('notifications.txt','r') as file: # Use file to refer to the file object
    data = file.read().splitlines()
print(data)
reminders = {}
curr = ""
for i in range(len(data)):
    if data[i] in emotion_map:
        reminders[data[i]] = []
        curr = data[i]
    else:
        reminders[curr].append(data[i])
print(reminders)
print(reminders['Sad'])
with open('notifications.json', 'w') as fp:
    json.dump(reminders, fp)
