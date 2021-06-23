class AnalizeSmokers:
    def __init__(self, ages_array, sexes_array, bmis_array, num_children_array, smoker_statuses_array, regions_array, charges_array):
        self.ages_array = ages_array
        self.sexes_array = sexes_array
        self.bmis_array = bmis_array
        self.num_children_array = num_children_array
        self.smoker_statuses_array = smoker_statuses_array
        self.regions_array = regions_array
        self.charges_array = charges_array

    def analize_ages(self):
        yes_count = 0
        yes_total = 0
        no_count = 0
        no_total = 0
        i = 0
        while i < len(self.ages_array):
            if self.smoker_statuses_array[i] == 'yes':
                yes_total += int(self.ages_array[i])
                yes_count += 1
            else:
                no_total += int(self.ages_array[i])
                no_count += 1
            i += 1
        avg_yes = int(yes_total / yes_count)
        avg_no = int(no_total / no_count)
        print(f"The average age of non-smokers is {avg_no} while the average age for smokers is {avg_yes}.")

    def analize_sexes(self):
        male_yes = 0
        male_count = 0
        female_yes = 0
        female_count = 0
        i = 0
        while i < len(self.sexes_array):
            if self.smoker_statuses_array[i] == 'yes':
                if self.sexes_array[i] == 'male':
                    male_yes += 1
                    male_count += 1
                else:
                    female_yes += 1
                    female_count += 1
            else:
                if self.sexes_array[i] == 'male':
                    male_count += 1
                else:
                    female_count += 1
            i += 1
        male_rate = int(male_yes / male_count * 100)
        female_rate = int(female_yes / female_count * 100)
        print(f"{male_rate}% of males are smokers while {female_rate}% of females are smokers.")