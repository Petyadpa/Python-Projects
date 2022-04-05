from project.lion import Lion


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__budget < price and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for name in self.workers:
            if name.name == worker_name:
                self.workers.remove(name)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = sum(worker.salary for worker in self.workers)
        if sum_salaries >= self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tend_animals_money = sum(animal.money_for_care for animal in self.animals)
        if tend_animals_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= tend_animals_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_count = [x for x in self.animals if type(x).__name__ == 'Lion']
        lions_info = [repr(i) for i in self.animals if type(i).__name__ == 'Lion']
        tigers_count = [x for x in self.animals if type(x).__name__ == 'Tiger']
        tigers_info = [repr(i) for i in self.animals if type(i).__name__ == 'Tiger']
        cheetah_count = [x for x in self.animals if type(x).__name__ == 'Cheetah']
        cheetah_info = [repr(i) for i in self.animals if type(i).__name__ == 'Cheetah']
        result = f"You have {len(self.animals)} animals\n" + f"----- {len(lions_count)} Lions:\n" + "\n".join(
            lions_info)
        result += f"\n" + f"----- {len(tigers_count)} Tigers:\n" + "\n".join(tigers_info) + "\n"
        result += f"----- {len(cheetah_count)} Cheetahs:\n" + "\n".join(cheetah_info)

        return result

    def workers_status(self):
        keepers_count = [x for x in self.workers if type(x).__name__ == 'Keeper']
        keeper_info = [repr(i) for i in self.workers if type(i).__name__ == 'Keeper']
        caretakers_count = [x for x in self.workers if type(x).__name__ == 'Caretaker']
        caretakers_info = [repr(i) for i in self.workers if type(i).__name__ == 'Caretaker']
        vets_count = [x for x in self.workers if type(x).__name__ == 'Vet']
        vets_info = [repr(i) for i in self.workers if type(i).__name__ == 'Vet']
        result = f"You have {len(self.workers)} workers\n" + f"----- {len(keepers_count)} Keepers:\n" + "\n".join(
            keeper_info)
        result += f"\n" + f"----- {len(caretakers_count)} Caretakers:\n" + "\n".join(caretakers_info) + "\n"
        result += f"----- {len(vets_count)} Vets:\n" + "\n".join(vets_info)

        return result


z = Zoo("Zoo", 1500, 1, 1)
res = z.fire_worker("K")
