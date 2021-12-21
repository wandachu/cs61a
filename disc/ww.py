class Clown:
    nose = 'big and red'
    def dance():
        return 'No thanks'

    def another(self):
        print("haha")

print(type(Clown.dance))
print(type(Clown().another))
print(type(Clown.nose))

# Are these all static sort-of attributes? There's no "self" in it.