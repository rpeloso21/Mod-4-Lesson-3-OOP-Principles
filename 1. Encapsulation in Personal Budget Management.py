# Task 1 

class BudgetCategory:
    def __init__(self, category_name, category_budget):
        self.__category_name = category_name
        self.__category_budget = category_budget

        self.__remaining_budget = self.__category_budget

# Task 2

    def get_budget(self):
        return self.__category_budget
    
    def get_name(self):
        return self.__category_name
    
    def get_remaining(self):
        return self.__remaining_budget
    
    def set_budget(self, new_budget):
        if new_budget >= 0:
            self.__category_budget = new_budget
            print(f"\nNew budget set to {new_budget}.\n")
        else:
            print("\nNew budget must be a positive number.\n")

    def set_name(self, new_name):
        self.__category_name = new_name
        print(f"\nName is set to {new_name}.\n")

# Task 3

    def add_expense(self, expense):
        if expense < self.__remaining_budget:
            self.__remaining_budget = (self.__remaining_budget - expense)
            print(f"\nBudget updated. Remaining budget for {self.get_name()} is {self.get_remaining()}.\n")

        else:
            print("\nYou do not have the remaining budget for that expense.\n")

# Task 4

    def display_category_summary(self):
        print(f"\nName: {self.get_name()} \nOriginal Budget: {self.get_budget()} \nRemaining After Expenses: {self.get_remaining()}.\n")



grocery = BudgetCategory("Grocery", 800)
grocery.add_expense(200)
grocery.add_expense(100)
grocery.display_category_summary()

    