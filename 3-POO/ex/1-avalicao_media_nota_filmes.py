class Movie :
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes) :
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.totalEvaluation = 0
        self.duartionMinutes = durationMinutes
        self.evaluators = 0
    
    def __str__(self) :
        return f"Filme: {self.name}"
    
    def technical_sheet(self) :
        print("Dados do Filme")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Duração do Filme: {self.duartionMinutes}")
        print(f"Avaliação do Filme: {self.totalEvaluation}")
        print(f"Total de Avaliadores: {self.evaluators}")
        
    def evaluate(self, note) :
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self) :
        print(f"Média do Filme {self.name}: {self.totalEvaluation / self.evaluators}")
        
mario = Movie("Super Mario Bros", 2023, False, 135)
avatar = Movie("Avatar", 2023, False, 180)

mario.evaluate(9.5)
mario.evaluate(10)
mario.technical_sheet()
mario.average()

avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.technical_sheet()
avatar.average()