class Yatzy:

    @staticmethod
    def chance(dice_list):
        assert len(dice_list )== 5
        assert max(dice_list) <= 6
        assert min(dice_list) >= 1

        total = sum(dice_list)
        return total 
        #coge como parámetro una lista de los parámetros de los dados y el resultado es el sumatorio de los valores de la lista (antes cogía los valores uno por uno)


    @staticmethod
    def yatzy(dice_list):
        assert len(dice_list )== 5
        assert max(dice_list) <= 6
        assert min(dice_list) >= 1


        check_if_all_same = dice_list.count(dice_list[0]) == len(dice_list) 
        #chequea que todos los elementos de la lista sean como el primero, !!!!!!plantéate si se ve más claro poniéndolo en dos variables separadas (una que sea el count y otra que sea la que chequee si es igual a la longitud de la lista)
        if check_if_all_same == True:
            points_total = 50
        else: 
            points_total = 0
        return points_total

    def __init__(self, dice_list, number):
        assert len(self.dice_list )== 5
        assert max(self.dice_list) <= 6
        assert min(self.dice_list) >= 1

        self.count = dice_list.count(number)
        self.points_total = self.count * number

    
    def ones(self, number = 1):
        return self.points_total
    

    @staticmethod
    def twos(dice_list):
        assert len(dice_list )== 5
        assert max(dice_list) <= 6
        assert min(dice_list) >= 1


    count = 
        return points_total
    
    @staticmethod
    def threes(dice_list):
        assert len(dice_list )== 5
        assert max(dice_list) <= 6
        assert min(dice_list) >= 1

        
        threes_count = 0
        for dice in dice_list:
            if dice == 3:
                threes_count += 1
        points_total = threes_count * 3
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
    def score_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        at = 0
        for at in range(6):
            if (counts[6-at-1] == 2):
                return (6-at)*2
        return 0
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

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
