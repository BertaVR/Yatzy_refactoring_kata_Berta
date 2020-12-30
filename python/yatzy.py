class Yatzy:

    @staticmethod
    def chance(dice_lst):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1

        total = sum(dice_lst)
        return total 
#coge como parámetro una lista de los parámetros de los dados y el resultado es el sumatorio de los valores de la lista (antes cogía los valores uno por uno)


    @staticmethod
    def yatzy(dice_lst):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1


        check_if_all_same = dice_lst.count(dice_lst[0]) == len(dice_lst) 
# esto chequea que todos los elementos de la lista sean como el primero, !!!!!!plantéate si se ve más claro poniéndolo en dos variables separadas (una que sea el count y otra que sea la que chequee si es igual a la longitud de la lista)
        if check_if_all_same == True:
            points_total = 50
        else: 
            points_total = 0
        return points_total

    def __init__(self, dice_lst, number):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1

        self.count = dice_lst.count(number)
        self.points_total = self.count * number

    @staticmethod
    def ones(dice_lst):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1


        points_total = dice_lst.count(1)
        return points_total
    

    @staticmethod
    def twos(dice_lst):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1

        points_total = dice_lst.count(2) * 2
        return points_total
    
    
    @staticmethod
    def threes(dice_lst):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1

        
        points_total = dice_lst.count(3) * 3
        return points_total
    
    


    
    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4): 
                sum += 4
        return sum
    

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                s = s + 5
        return s
    

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def score_pair(dice_lst):
        assert len(dice_lst)== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1

        repeated_lst = [0] 
#El acumulador parte con un 0 en lugar de estar vacío porque de esta manera si no hay parejas la puntuación será 0
        for dice in dice_lst:
            if dice_lst.count(dice) >= 2:
                repeated_lst.append(dice)

        points_total = max(repeated_lst) * 2
        return points_total
                
    
    @staticmethod
    def two_pair(dice_lst):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1

        repeated_lst = [] 
#aquí no pongo 0 porque si no me cargo la puntuación, si no el 0 sería el min 
        for dice in dice_lst:
            if dice_lst.count(dice) >= 2:
                repeated_lst.append(dice)

        if len(repeated_lst) >= 4:
            points_total = min(repeated_lst) * 2 + max(repeated_lst) * 2 
###Nota importante por si vuelvo a revisar el código: seguramente te sientes tentada a querer hacer un sum de la repeated list en vez de esto pero date cuenta de que tal y como montaste el algoritmo si hay un trio se añadirán 3 (de ahí que en el if hayas puesto >= 4 en vez de ==4) a la repeated list, de todos modos, mejor si puedes revisar el algoritmo y mejorarlo
        else:
            points_total = 0

        return points_total

    @staticmethod
    def three_of_a_kind(dice_lst):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1

        points_total = 0 
#en vez de la lista, aquí ya me aseguro que si no hay trío la puntuación no cambiará y se quedará en 0
        for dice in dice_lst:
            if dice_lst.count(dice) >= 3:
                points_total = dice * 3
                break #break para que no siga rodando repitiendo números
#aquí no haría falta hacer un acumulador y un if independiente poque solo puede haner un trío

        return points_total
        
    @staticmethod
    def four_of_a_kind(dice_lst):
        assert len(dice_lst )== 5
        assert max(dice_lst) <= 6
        assert min(dice_lst) >= 1

        points_total = 0 
        for dice in dice_lst:
            if dice_lst.count(dice) >= 4:
                points_total = dice * 4 
                break 
#esto es calcado al de los tríos

        return points_total


    

    @staticmethod
    def smallStraight(dice_lst):
        is_small_straight = sorted(dice_lst) == [1,2,3,4,5]
        if is_small_straight == True:
            points_total = 15  #sumatorio de los números de la lista (dados)
        else:
            points_total = 0

        return points_total

    

    @staticmethod
    def largeStraight(dice_lst):
        is_large_straight = sorted(dice_lst) == [2,3,4,5,6]
        if is_large_straight == True:
            points_total = 20 #sumatorio de los números de la lista (dados)
        else:
            points_total = 0

        return points_total
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
