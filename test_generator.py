import random
from string import ascii_lowercases

# [!] in command-line mode, generates a single wish PER USER,
# but allows random duplicate usernames

class TestDataGenerator:

    def __init__(self, username_length=6, path="gen/test/"):
        self.username_length = int(username_length)
        self.path = path
        self.subject_number_max_length = 4

    def generate_users(self, quantity):
        output = []
        minimum_length_factor = 0.7

        def make_username(length):
            n = len(ascii_lowercase)
            return [ ascii_lowercase[random.randint(0,n-1)]
                    for x in range(length) ]

        for i in range(quantity):
            username_length = random.randint(
                int(self.username_length * minimum_length_factor),
                self.username_length
            )
            output.append(
                "".join(make_username(username_length))
            )

        return output

    def generate_tags(self, quantity):
        subject_prefixes = ["INF", "STK", "MAT", "MAT-INF"]
        subject_prefixes = [prefix.upper() for prefix in subject_prefixes]

        def make_subject_code():
            number = "".join([ str(random.randint(0,9))
                for i in range(self.subject_number_max_length)])
            return "%s%s" % (random.choice(subject_prefixes), number)

        return [make_subject_code() for i in range(quantity)]


    def generate_wishes(self, users, max_tag_quantity=6, min_tag_quantity=1):
        for u in users:
            quantity = random.randint( min_tag_quantity, max_tag_quantity )
            yield (u, self.generate_tags(quantity))




if __name__ == "__main__":

    generator = TestDataGenerator( raw_input("Username length: ") )
    users = generator.generate_users( int(raw_input( "User quantity: " )) )

    if "y" in raw_input("Save USERS to file? (y/n): "):
        with open( "./" + generator.path + "users.dat", "w" ) as out:
            for u in users:
                out.write("%s\n" % u)

    tags = generator.generate_tags( int(raw_input( "Tag quantity: " )) )

    if "y" in raw_input("Save TAGS to file? (y/n): "):
        with open( "./" + generator.path + "tags.dat", "w" ) as out:
            for t in tags:
                out.write("%s\n" % t)

    min_tag_n = raw_input("Min-imum number of tags for each user:")
    max_tag_n = raw_input("Max-imum number of tags for each user:")

    if min_tag_n != "" and max_tag_n != "":
        wishes = generator.generate_wishes( users, int(max_tag_n), int(min_tag_n) )
    else:
        wishes = generator.generate_wishes( users )

    if "y" in raw_input("Save WISHES to file? (y/n): "):
        with open( "./" + generator.path + "wishes.dat", "w" ) as out:
            for username,tags in wishes:
                out.write( "%s %s\n" % (username," ".join(tags)) )
