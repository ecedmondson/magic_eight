from random import choice


class MagicEightBall:
  affirmatives = [
      "It is Certain",
      "It is decidely so.",
      "Without a doubt.",
      "Yes, definitely.",
      "You may rely on it.",
      "As I see it, yes.",
      "Most likely.",
      "Outlook good.",
      "Yes.",
      "Signs point to yes.",
  ]
  non_comittals = [
      "Reply hazy, try again.",
      "Ask again later.",
      "Better not tell you now.",
      "Cannot predict now.",
      "Concentrate and ask again.",
  ]
  negatives = [
      "Don't count on it.",
      "My reply is no.",
      "My sources say no.",
      "Outlook not so good.",
      "Very doubtful.",
  ]
  answers = [*affirmatives, *non_comittals, *negatives]
  
  @property
  def get_magic_eight_answer(self):
    return choice(answers)
