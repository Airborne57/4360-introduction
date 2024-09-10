import sys

option = sys.argv[1].lower()

if option == "/fact":
    print("I play the trumpet, both of my parents direct bands, and my brother is a music education major at BSU.")
elif option == "/name":
    print("My name is Dawson Dailey and I am a senior this year.")
elif option == "/why":
    print("I chose computer science because I spend too much time on the computer and I am interested in how they work")
elif option == "/what":
    print("I want to do data science since I like statistics, but I am still deciding.")
else:
    print("That is not an option. Enter /fact, /name, /why, or /what.")
