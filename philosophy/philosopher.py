from random import choice

class Philosopher:
  philosophical_sounding_questions = [
      "What is the meaning of life?",
      "Does freewill exist?",
  ]
  
  @property
  def philosophize(self):
    return choice(philosophical_sounding_questions)
