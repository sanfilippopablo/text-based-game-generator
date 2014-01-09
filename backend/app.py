# -*- coding: utf-8 -*-
import text_compiler, json

class Step(object):
   """
   Step object. Representa un step en particular.
   """
   def __init__(self, raw_text, name):
      self.html, self.choices = text_compiler.get_text_and_choices(raw_text)
      self.name = name

class TextBasedGame(object):
   """
   Clase principal. Representa en sí mismo un text based game.
   """

   def __init__(self, meta={}, steps=[]):
      self.meta = meta
      self.steps = steps

   @classmethod
   def from_json(cls, json_data):
      """
      Crea un objeto TextBasedGame y completa sus datos con la data obtenida
      del parámetro json_data. Para más información en la estructura de este
      JSON, check
      https://github.com/giamfreeg/text-based-game-generator/wiki/Implementation
      """
      data = json.loads(json_data)

      # Add meta
      game = cls(meta=data['meta'])

      # Add steps
      for raw_step in data['steps']:
         game.add_step(Step(raw_text=raw_step['text'], name=raw_step['name']))

      return game

   def add_step(self, step):
      if not isinstance(step, Step):
         raise ValueError('Step must be Step instance.')
      self.steps.append(step)

   def is_valid(self):
      """
      Busca errores en el game. Errores pueden ser: steps huérfanos (no
      referenciados por ningún otro step), broken links (steps con referencia
      a steps que no existen), malformed metadata, etc.
      Devuelve True si está todo OK, False en caso contrario.
      """
      raise NotImplementedError


 

def main():
	d = """
	{
   "meta":
   {
      "title": "La cuerda perdida de la guitarra azul",
      "author": "Pablo Lescano",
      "theme": "blue"
   },
   "steps": [
      {
         "name": "in_the_room",
         "text": "Hay un sandwich. Querés <$comerlo$>(comiendo_sandwich)?"
      },
      {
         "name": "comiendo_sandwich",
         "text": "El sandwich estaba envenenado. Mueres. Fin."
      }
   ]
}
"""
	data = json.loads(d)
	print "Title: ", data['meta']['title']
	print "Author: ", data['meta']['author']
	print "====================="

	for step in data['steps']:
		compiled_step, choices = text_compiler.get_text_and_choices(step['text'])
		print "Step Name: ", step['name']
		print "HTML for step: ", compiled_step
		print "Choices: "
		for c in choices:
			print "Acción: ", c[0], "Destino: ", c[1]

if __name__ == '__main__':
	main()