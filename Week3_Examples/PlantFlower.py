class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')

class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        #Plant.__init__(self, plant_name, plant_cost)
        # Replace Plant.__init__(self, plant_name, plant_cost) with
        #                       super().__init__(plant_name, plant_cost)

        super().__init__(plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        #print(f'   Plant name: { self.plant_name }')
        #print(f'   Cost: { self.plant_cost }')
        #
        # Replace the above two lines with super().print_info()

        super().print_info()
        print(f'   Annual: { self.is_annual }')
        print(f'   Color of flowers: { self.color_of_flowers }')