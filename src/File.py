import json
import os.path

class File:

	def read(path, file, default):
		jsonFile = None

		if os.path.isfile(path):
			with open(file, 'r') as f:
				jsonFile = json.loads(f.read())
		return jsonFile

	def write(path, name, jsonFile):
		if os.path.isfile(path):
			with open(name, 'w+') as f:
				f.seek(0)
				f.close()

		with open(name, 'w+') as f:
			f.write(json.dumps(jsonFile, ensure_ascii=False, indent=4))
