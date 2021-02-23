

ques = input("I think you're really sweet and pretty darn cute...wanna go on a date? [y] for yes [n] for no: ")

if ques == 'y':

    print()
    print("I was expecting you to say no but this is a pleasent surprise :)")

    print()
    date = input("What would you want to do? [m] for movie in the dorm or [l] for literally anything else because I have no more ideas: ")

    if date == 'm':
        print()
        print("Cool! What kind of movies do you like?") 
        movie = input("[f] for fantasy, [d] for drama, or [fav] ps THIS ONE IS PRETTY COOL?: ")

        if movie == 'f':
            print()
            print("Lord of The Rings? You can pick which one :)")

        if movie == 'd':
            print()
            print("Perks of Being a Wallflower? I read it in high school and its a really good book!")

        if movie == 'fav':
            print()
            print("Black Mirror: Bandersnatch?? It is a choose your own adventure movie and it SUPER INTERESTING!")

        print()
        print("Just pick a date and its a date! (haha pun!)")


    if date == 'l':
        print()
        nfc = input("Netflix and chill without the netflix? [y] for hell yeah or [n] for nah: ")
        
        if nfc == 'y':
            print()
            print("Slow your roll buddy! Lets first watch a movie! Pick a date and its a date! :) ")

        if nfc == 'n':
            print()
            print("Yeah if you hit yes you would of found out this was a joke")
            print()
            print("...")
            print()
            print("well kinda...anyway lets watch a movie! Pick a date and its a date :) ")


if ques == 'n':
    print()
    print("HAHA THIS WAS A JOKE IM TOTALLY KIDDING THIS NEVER HAPPEND OKAY COOL")