import markovify
import json
import sys
path = 'models/'
model_strings = sys.argv[1:]
suffix = '_model.json'

models = []
# load models from files
for model_string in model_strings:
    with open(path + model_string + suffix) as model_file:
        models.append(markovify.Text.from_json(json.load(model_file)))

model = markovify.combine(models)
i = ""
while i != 'q':
    i = input('Enter t to make me talk or q to quit: ')
    if i == 't':
        print(model.make_short_sentence(140))
    elif i != 'q':
        print('Invalid input')
