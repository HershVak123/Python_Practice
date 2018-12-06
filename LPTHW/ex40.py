class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With a pocket full of shells"])

clarity_lyrics = ["You are the piece of me",
                  "I wish i didn't need",
                  "Chasing relentlessly",
                  "And I still don't know why"]

clarity = Song(clarity_lyrics)

# happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()

clarity.sing_me_a_song()
