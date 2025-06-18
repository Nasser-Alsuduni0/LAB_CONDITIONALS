movie = "Dune"
rating_out_of_five:int = 3
popularity:float = 72.65

if rating_out_of_five >= 4 and popularity > 80:
    print("Highly Recommended")
elif rating_out_of_five >= 3 and popularity > 70 :
    print("I recommended it . It is good")
elif rating_out_of_five <= 2 and popularity > 60 :
    print("You should check it out!")    
elif rating_out_of_five <= 2 and popularity < 50 :
    print("Don't watch it. It is a waste of time")    