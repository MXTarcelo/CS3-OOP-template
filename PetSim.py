class Pet:
  def __init__(self, name, energy):
    self.__name = name
    self.__energy = energy

  # Define Getter and Setter for name.
  # Setter for Name should should not accept empty string.
  @property

  @name.setter

  # Define Getter and Setter for energy
  # Setter for energy should not be a negative integer number and should not be more than 100
  @property

  @energy.setter

  def play(self):
    # can play if enery is >= 10 to be allowed to play. Each play deducts 10points
    # otherwise give a message that the pet is too tired.
    pass

  def rest(self):
    # when pet is at rest, enery is increased by 20 but makes sure not more than 100.
    # prints <pet> rested and now has <nn> energy
    pass

class PetOwner:
  def __init__(self): # add necessary parameters here
    # intialize the instance variables (attributes) for PetOwner
    pass

  def walk_pet(self):
    # prints that an owner walks the pet
    # the pet will play
    pass

  def let_pet_rest(self):
    # prints that an owner is letting the pet rest
    # the pet should rest
    pass

  def show_pet_status(self):
    # show the pet owner and pet information refer to sample output


# Main Code
owner = PetOwner("Alex", "Nibbles", 50)
owner.show_pet_status()

print("\n--- Walking the Pet ---")
owner.walk_pet()

print("\n--- Resting the Pet ---")
owner.let_pet_rest()

print("\n--- Updating Pet Information ---")
owner.pet.name = "Fluffy"
owner.pet.energy = 80

owner.show_pet_status()

## should display the sample output as shown above
