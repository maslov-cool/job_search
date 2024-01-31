class Job:
    def __init__(self, profession):
        self.profession = profession
        self.vacancies = {}

    def post_vacancy(self, company, salary, min_exp):
        self.vacancies[company] = [salary, min_exp]

    def close_vacancy(self, company):
        del self.vacancies[company]

    def update_salary(self, company, new_salary):
        self.vacancies[company][0] = new_salary

    def update_exp(self, company, new_exp):
        self.vacancies[company][1] = new_exp

    def show_vacancies(self):
        print(self.profession)
        if not self.vacancies:
            print('Пока нет вакансий на данную профессию')
        else:
            for vacancy in self.vacancies.keys():
                print(f'"{vacancy}": зарплата {self.vacancies[vacancy][0]} тыс, требуемый опыт '
                      f'{self.vacancies[vacancy][1]}')

    def find_best_vacancy(self, exp, profession, min_salary):
        if profession != self.profession:
            print(f'Кажется, вы ищете вакансии {profession} в разделе {self.profession}. Выберите другой раздел.')
        else:
            vacancy_ = ''
            best_vacancy = 0
            for vacancy in self.vacancies.keys():
                if self.vacancies[vacancy][1] <= exp and self.vacancies[vacancy][0] > best_vacancy and \
                        self.vacancies[vacancy][0] >= min_salary:
                    best_vacancy = self.vacancies[vacancy][0]
                    vacancy_ = vacancy
            if not best_vacancy:
                print('Простите, для вас не нашлось вакансий.')
            else:
                print(f'Наилучшая вакансия для вас в компании "{vacancy_}" с зарплатой {self.vacancies[vacancy_][0]} '
                      f'тыс.')
                del self.vacancies[vacancy_]


loyer = Job('loyer')
loyer.post_vacancy('Делу время', 100, 5)
loyer.post_vacancy('BTS', 176, 0)
loyer.show_vacancies()
loyer.find_best_vacancy(10, 'doctor', 200)
loyer.find_best_vacancy(6, 'loyer', 100)
loyer.update_salary('Делу время', 150)
loyer.show_vacancies()
