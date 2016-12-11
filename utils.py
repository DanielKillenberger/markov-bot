import json
import markovify


def export_model(model, model_name):
    text_model_json = model.to_json()

    with open('models/' + model_name + '_model.json', 'w') as outfile:
        json.dump(text_model_json, outfile)
