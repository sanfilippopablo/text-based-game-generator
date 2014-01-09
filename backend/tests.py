# -*- coding: utf-8 -*-

import unittest
from app import Step, TextBasedGame

class TestStep(unittest.TestCase):
	def setUp(self):
		self.raw_step_text = u"Hay un sándwich. Puedes <$comerlo$>(comiendo_sandwich) o <$tirarlo$>(tirando_el_sandwich) por la ventana."
		self.name = u'in_the_room'
		self.step = Step(self.raw_step_text, self.name)

	def test_name(self):
		self.assertEqual(self.step.name, self.name)

	def test_text(self):
		self.assertEqual(self.step.html, u'<p>Hay un sándwich. Puedes <a href="comiendo_sandwich.html">comerlo</a> o <a href="tirando_el_sandwich.html">tirarlo</a> por la ventana.</p>')

	def test_choices(self):
		self.assertEqual(self.step.choices, [(u'comerlo', u'comiendo_sandwich'), (u'tirarlo', u'tirando_el_sandwich')])

class TestTextBasedGame(unittest.TestCase):
	def setUp(self):
		self.json_data = """
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
			} """
		self.game = TextBasedGame.from_json(self.json_data)

if __name__ == '__main__':
	unittest.main()