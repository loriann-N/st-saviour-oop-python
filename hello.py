from culinary_canvas import CulinaryCanvas

if __name__ == '__main__':
    my_canvas = CulinaryCanvas('Pasta Canvas', 'Rasta Pasta', 1.0, True)
    print("Welcome to CulinaryCanvas!")
    print("Today we are cooking " + my_canvas.dish)
    print("Class Duration: " + str(my_canvas.hours) + " hours.")
    if my_canvas.peppers:
        print("WARNING!: Peppers are spicy ")
    else: 
        print ("No peppers no spice, good to go!")

    print(my_canvas.cook())

    print("🚨DISASTER🚨")
    print("Oil splashes into the pan..")
    print("Flames start to blaze up to the celling")
    print("Fire flares around the entire school!! 911 Anybody??!")
    print("Smoke fills the room,Girls  scatter and bum into each other..")
    print("A girl slips on the pasta water and gets her arm burnt to a crisp...")
    print("No one saw though because of the smoke in the air")
    print("The Head cook grabs the fire extingushr to put the fire out. Finally")
    print("Is every one okay.. OMG!!")
    print( "SOMEONE call 911 her arm is falling off...")
    print(" 911 gets called ")
    print("one cheff down..")
    print("the show must go on..somone cross off her area")
