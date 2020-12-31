class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)


    @staticmethod
    def chance(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1

        total_points = sum(dice)
        return total_points
#coge como parámetro una lista de los dados y el resultado es el sumatorio de los valores de la lista 


    @staticmethod
    def yatzy(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1
        HOW_MANY_DICE = 5
        if dice.count(dice[0]) == HOW_MANY_DICE:
# esto chequea que todos los elementos de la lista sean como el primero, tmb puedo cambiarlo por ==5 y quizá se lee mejor
            points_total = 50
        else: 
            points_total = 0
        return points_total

    @staticmethod
    def ones(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1

        ONE = 1

        points_total = dice.count(1) * ONE
        return points_total
    

    @staticmethod
    def twos(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1
        TWO = 2
        points_total = dice.count(2) * TWO
        return points_total
    
    
    @staticmethod
    def threes(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1

        THREE = 3

        points_total = dice.count(3) * THREE
        return points_total
    
    


    
    def fours(self, *dice):
        assert len(self.dice)== 5
        assert max(self.dice) <= 6
        assert min(self.dice) >= 1

        FOUR = 4

        points_total = self.dice.count(4) * FOUR
        return points_total

    

    def fives(self, *dice):
        assert len(self.dice)== 5
        assert max(self.dice) <= 6
        assert min(self.dice) >= 1

        FIVE = 5

        points_total = self.dice.count(5) * FIVE

        return points_total
    

    def sixes(self, *dice):
        assert len(self.dice)== 5
        assert max(self.dice) <= 6
        assert min(self.dice) >= 1

        SIX = 6

        points_total = self.dice.count(6) * SIX

        return points_total



    @staticmethod
    def score_pair(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1
        PAIR = 2
        repeated_lst = [0] 
#El acumulador parte con un 0 en lugar de estar vacío porque de esta manera si no hay parejas la puntuación será 0
        for number in dice:
            if dice.count(number) >= 2:
                repeated_lst.append(number)

        points_total = max(repeated_lst) * PAIR
        return points_total
                
    
    @staticmethod
    def two_pair(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1

        PAIR = 2
        repeated_lst = [] 
#aquí no pongo 0 porque si no me cargo la puntuación, si no el 0 sería el min 
        for number in dice:
            if dice.count(number) >= 2:
                repeated_lst.append(number)

        if len(repeated_lst) >= 4:
            points_total = min(repeated_lst) * PAIR + max(repeated_lst) * PAIR
###Nota importante por si vuelvo a revisar el código: seguramente te sientes tentada a querer hacer un sum de la repeated list en vez de esto pero date cuenta de que tal y como montaste el algoritmo si hay un trio se añadirán 3 (de ahí que en el if hayas puesto >= 4 en vez de ==4) a la repeated list, de todos modos, mejor si puedes revisar el algoritmo y mejorarlo
        else:
            points_total = 0

        return points_total

    @staticmethod
    def three_of_a_kind(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1

        points_total = 0
        THREE = 3
#en vez de la lista, aquí ya me aseguro que si no hay trío la puntuación no cambiará y se quedará en 0
        for number in dice:
            if dice.count(number) >= 3:
                points_total = number * THREE
                break #break para que no siga rodando repitiendo números
#aquí no haría falta hacer un acumulador y un if independiente poque solo puede haner un trío

        return points_total
        
    @staticmethod
    def four_of_a_kind(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1

        FOUR = 4

        points_total = 0 
        for number in dice:
            if dice.count(number) >= 4:
                points_total = number * FOUR 
                break 
#esto es calcado al de los tríos

        return points_total


    

    @staticmethod
    def smallStraight(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1


        if sorted(dice) == [1,2,3,4,5]:
            points_total = 15  #sumatorio de los números de la lista (dados)
        else:
            points_total = 0

        return points_total

    

    @staticmethod
    def largeStraight(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1

        if sorted(dice) == [2,3,4,5,6]:
            points_total = 20 #sumatorio de los números de la lista (dados)
        else:
            points_total = 0

        return points_total

    

    @staticmethod
    def fullHouse(*dice):
        assert len(dice)== 5
        assert max(dice) <= 6
        assert min(dice) >= 1

        there_is_pair = False
        there_is_three = False

        for number in dice:
            if dice.count(number) == 2:
                there_is_pair = True
            elif dice.count(number) == 3:
                there_is_three = True


            elif dice.count(number) != 2 and dice.count(number) != 3:
                points_total = 0
                break
            if there_is_three == True and there_is_pair== True:
                points_total = sum(dice)
                break
        return points_total
#vale esto es un bucle que mira de cada dado si hay 2 o 3 de ese mismo número. En cuanto se encuentre un pair y un three el bucle rompe y la puntuación es el sumatorio de los numbers, si encuentra un número de dados repetidos que no sea 2 o 3 el bucle rompe y la puntuación es 0.  

