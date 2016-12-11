import markovify
import json
import sys
path = 'models/'
model_string = str(sys.argv[1])
suffix = '_model.json'
#load model from file
with open(path + model_string + suffix) as model_file:
    model = markovify.Text.from_json(json.load(model_file))
print(model.make_sentence())
