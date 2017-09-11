import os
from flask import Flask, json
from flask.wrappers import Response
from _operator import itemgetter
from flask.json import jsonify

app = Flask(__name__)

wsgi_app = app.wsgi_app

class NameSorter():
    @app.route('/unsorted-names-list.txt', methods=['GET'])
    def name_sorter():

            file_name='unsorted-names-list.txt'
            unsorted_filepath = os.path.join(os.path.dirname(__file__), file_name)

            with open(unsorted_filepath) as unsorted_file:
                unsorted_name_list=unsorted_file.readlines()

                unformatted_namelist=[]
                unsorted={}
                
                for name in unsorted_name_list:
                    full_name_split=name.split(" ")
                    last_name=full_name_split[-1].strip('\n')
                    first_name=name.rsplit(' ', 1)[0]
                    unsorted['first_name']=first_name
                    unsorted['last_name']=last_name
                
                    temp_list={unsorted['first_name']:unsorted['last_name']}
                    
                    for unsorted['first_name'],unsorted['last_name'] in temp_list.items():

                        single_name=unsorted['first_name'],unsorted['last_name']
                        unformatted_namelist.append(tuple(single_name))

                sorted_unformatted_list= sorted(unformatted_namelist, key=itemgetter(1,0))
                sorted_formatted_list=json.dumps(sorted_unformatted_list)
                
                for char in [",",'"',"[",']]']:
                    if char in sorted_formatted_list:
                        sorted_formatted_list = sorted_formatted_list.replace(char, "")
                        sorted_formatted_list = sorted_formatted_list.replace("] ", "\n")
                sorted_file=open('sorted-names-list.txt','w+')
                sorted_file.writelines(sorted_formatted_list)
                return Response(sorted_formatted_list,mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
