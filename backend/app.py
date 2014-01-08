import json

class TextBasedGame(object):
	def __init__(self):
		general_settings = {}
		meta = {}
		steps = []

	@classmethod
	def from_json(cls, json_string):
		data = json.loads(json_string)
		game = cls()
		game.general_settings = data['general_settings']
		game.meta = data['meta']
		game.steps = data['steps']
		return game

def main():
	d = """
	{
   "meta":
   {
      "title": "La cuerda perdida de la guitarra azul",
      "author": "Pablo Lescano"
   },
   "general_settings":
   {
      "theme": "blue"
   },
   "steps": [
      {
         "name": "tipo_en_su_casa",
         "text": "Hay un sandwich. Querés {[comerlo]}(comiendo_sandwich)?"
      },
      {
         "name": "comiendo_sandwich",
         "text": "El sandwich estaba envenenado. Mueres. Fin."
      }
   ]
}
"""
	game = TextBasedGame.from_json(d)
	print(game.general_settings, game.meta, game.steps)

if __name__ == '__main__':
	main()