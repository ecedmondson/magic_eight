from random import choice

class Philosopher:
  philosophical_sounding_questions = [
      "What is the meaning of life?",
      "Does freewill exist?",
      "Is it possible to understand good if evil is absent?",
      "Is true freedom possible?",
      "Is morality objective?",
      "Is truth relative?",
      "Are truth and reality coterminous?",
      "Does the univerise have a single point of incipience?",
      "Are the mind and the brain one and the same?",
      "Are our methods and means of obtaining knowledge valid?",
      "Is it ever acceptable to lie?",
      "Is mind separate from matter?",
      "Can vegetables feel pain?",
      "Can we know with certainty that there is something rather than nothing?",
      "Is our reality just a simulation?",
      "Does the good exist?",
  ]
  
  @property
  def philosophize(self):
    return choice(philosophical_sounding_questions)
