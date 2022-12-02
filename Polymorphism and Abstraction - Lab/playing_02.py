def start_playing(obj):
    return obj.play()

# Description:
#
# Create a function called start_playing which will receive an instance and will return its play() method.
#
# Test code:
class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))

# Expected output:
# Playing the guitar
#
#
#
# Test code:
class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))

# Expected output:
# Children are playing
