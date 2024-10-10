# Object Oriented Programming 

# class Cat:        # blueprint /class of Cat
#     legs = 4      # property of Cat class
#     tail = True   # property of Cat class

#     # constructor
#     def _init_(self, l, t):
#         self.legs = l
#         self.tail = t

#     def meow(self):  # method of Cat class
#         print('meow meow')

#     def play(self):
#         print('playing') 

#     def fight(self):
#         print('Fighter') 

#     def hunter(self):
#         print('hunting')         


# cat1 = Cat(4, False)  # object of Cat class
# # cat2 = Cat(3, True)

# print(cat1.legs)
# print(cat1.tail)

# # cat1.play()
# # cat2.play()


class Circle:
    PI = 3.14
    
    def area(self, radius):
        print(3.14 * radius * radius)

circle = Circle()

circle.area(4)



