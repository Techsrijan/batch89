class Theory:
    def get_theorymarks(self):
        print("theory marks")

class sports:
    def get_sports(self):
        print("sport marks")

class Result(Theory,sports):
    def result(self):
        print("Theory+sports marks")

s=Result()
s.get_theorymarks()
s.get_sports()
s.result()
