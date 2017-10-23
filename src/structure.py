import os
import json

API_VERSION = "0.0.1"

def make_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def remove_directory(directory_name):
    os.removedirs(directory_name)

def add_requirements(directory_name):
    try:
        with open(directory_name+"requirements.txt", 'w+') as requirement_file:
            requirement_file.write("")
    except Exception as e:
        print e


if __name__ == '__main__':
    

    with open('data/tracks.json') as data_file:
        data = json.load(data_file)
    
    event_details_list = data[API_VERSION]
    for each_event in event_details_list:
        for key, value in each_event.iteritems():
            event_type = value['type']
            if event_type == 'talk' or event_type == 'workshop':
                title = value['title'].replace(" ", "_")
                make_directory('./requirements/{}s/{}'.format(event_type, title))
                add_requirements("./requirements/{}s/{}/".format(event_type, title))
