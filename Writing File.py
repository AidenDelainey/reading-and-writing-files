##----------------------##
#) File Writer          (#
#) Aiden Delainey       (#
#) dec, 9/2025          (#
##----------------------##


########## Fucntions ##########
def write_file():
    name = input("what is the name of your character: ")
    race = input("what is the race of your character: ")
    health = input("What is your max hp: ")
    file = name + "'s character sheet.txt"
    save = open(file, 'w')
    save.write("Name: ")
    save.write(name + '\n')
    save.write("Race: ")
    save.write(race + '\n')
    save.write("Health: ")
    save.write(health + '/' + health + '\n')
    save.write("level: 1\n")
    save.write("---inventory---")
    save.close()
def main():
    print(f"Importing data to new character sheet")
    write_file()
    print("file created")

########## Main Code ##########
main()
