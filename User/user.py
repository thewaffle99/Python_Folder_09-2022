class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_memeber = False
        self.gold_card_points = 0

    def display_info(self):
        print('***start***')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'email: {self.email}')
        print(f'Card Holder: {self.is_rewards_memeber}')
        print(f'Points: {self.gold_card_points}')

    def enroll(self):
        self.is_rewards_memeber = True
        self.gold_card_points = 100

    def spend_points(self, amount):
        self.gold_card_points -= amount


michael = User('michael', 'jordan', 'mjordan@hotmail.com', 24)

michael.display_info()
michael.enroll()
michael.display_info()
michael.spend_points(50)
michael.display_info()
