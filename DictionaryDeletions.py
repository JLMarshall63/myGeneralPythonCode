try:
    
    zoo_animals = {'Unicorn' : 'Cotton Candy House', 'Sloth' : 'Rainforest Exhibit','Bengal Tiger' : 'Jungle House', 'Atlantic Puffin' : 'Arctic Exhibit', 'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
    del zoo_animals['Unicorn']

# Your code here!

    del zoo_animals['Bengal Tiger']
    del zoo_animals['Sloth']
    new_value = "Antarctic Ice Sheet"
    zoo_animals["Rockhopper Penguin"] = new_value


    print zoo_animals
except Exception, e:
    print str(e)