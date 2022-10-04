class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print('**********')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'email: {self.email}')
        print(f'age: {self.age}')
        print(f'Membership: {self.is_rewards_member}')
        print(f'Points: {self.gold_card_points}')

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200

    def earn_points(self):
        self.gold_card_points += 10

    def spend_points(self, ammount):
        self.gold_card_points -= ammount


alan = User('Alan', 'Lytton', 'alytton@hotmail.com', 18)

latte = 100
lavender_latte_points = 150

alan.display_info()
alan.enroll()
alan.display_info()
alan.earn_points()
alan.display_info()
#
alan.spend_points(lavender_latte_points)
alan.display_info()
