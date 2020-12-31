from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/

def test_chance(): #el resultado de chance es la suma de todos los dados
        assert Yatzy.chance(1,1,1,1,1) == 5
        assert Yatzy.chance(2,3,4,5,1) == 15
        assert Yatzy.chance(3,3,4,5,1) == 16


def test_yatzy(): #si todos son iguales devuelve 50, si no 0
        assert Yatzy.yatzy(4,4,4,4,4) == 50
        assert Yatzy.yatzy(6,6,6,6,6) == 50
        assert Yatzy.yatzy(6,6,6,6,3) == 0


def test_ones(): #suma todos los unos
        assert Yatzy.ones(1,2,3,4,5) == 1
        assert Yatzy.ones(1,2,1,4,5) == 2
        assert Yatzy.ones(6,2,2,4,5) == 0
        assert Yatzy.ones(1,2,1,1,1) == 4


def test_twos(): #suma todos los doses (el valor, no la cuenta)
        assert Yatzy.twos(1,2,3,2,6) == 4
        assert Yatzy.twos(2,2,2,2,2) == 10
        assert Yatzy.twos(1,6,3,6,6) == 0



def test_threes():
        assert Yatzy.threes(1,2,3,2,3) == 6
        assert Yatzy.threes(2,3,3,3,3) == 12
        assert Yatzy.threes(2,1,1,1,1) == 0


def test_fours_test():
        assert Yatzy(4,4,4,5,5).fours() == 12
        assert Yatzy(4,4,5,5,5).fours() == 8
        assert Yatzy(4,5,5,5,5).fours() == 4
        assert Yatzy(2,1,1,1,1).fours() == 0



def test_fives():
        assert Yatzy(4,4,4,5,5).fives() == 10
        assert Yatzy(4,4,5,5,5).fives() == 15
        assert Yatzy(4,5,5,5,5).fives() == 20
        assert Yatzy(4,4,4,4,4).fives() == 0


def test_sixes_test():
        assert Yatzy(4,4,4,5,5).sixes() == 0
        assert Yatzy(4,4,6,5,5).sixes() == 6
        assert Yatzy(6,5,6,6,5).sixes() == 18


def test_one_pair():
        assert Yatzy.score_pair(1,4,3,5,6) == 0
        assert Yatzy.score_pair(3,4,3,5,6) == 6
        assert Yatzy.score_pair(5,3,3,3,5) == 10
        assert Yatzy.score_pair(5,3,6,6,5) == 12
        assert Yatzy.score_pair(5,3,6,6,3) == 12


def test_two_Pair():
        assert Yatzy.two_pair(3,3,5,4,5) == 16
        assert Yatzy.two_pair(3,3,6,6,6) == 18
        assert Yatzy.two_pair(3,3,6,5,4) == 0

def test_three_of_a_kind():
        assert Yatzy.three_of_a_kind(3,3,3,4,5) == 9
        assert Yatzy.three_of_a_kind(5,3,5,4,5) == 15
        assert Yatzy.three_of_a_kind(3,3,3,3,5) == 9


def test_four_of_a_knd():
        assert Yatzy.four_of_a_kind(3,3,3,3,5) == 12
        assert Yatzy.four_of_a_kind(5,5,5,4,5) == 20
        assert Yatzy.four_of_a_kind(3,3,3,3,3) == 12
        assert Yatzy.four_of_a_kind(3,3,3,2,1) == 0






def test_smallStraight():
        assert Yatzy.smallStraight(1,2,3,4,5) == 15
        assert Yatzy.smallStraight(2,3,4,5,1) == 15
        assert Yatzy.smallStraight(1,2,2,4,5) == 0
        assert Yatzy.smallStraight(2,3,4,5,6) == 0
        assert Yatzy.smallStraight(4,1,5,2,3) == 15




def test_largeStraight():
        assert Yatzy.largeStraight(6,2,4,5,3) == 20
        assert Yatzy.largeStraight(6,2,3,4,5) == 20
        assert Yatzy.largeStraight(2,3,4,5,6) == 20
        assert Yatzy.largeStraight(1,2,2,4,5) == 0
        assert Yatzy.largeStraight(4,1,5,2,3) == 0



def test_fullHouse():
        assert Yatzy.fullHouse(6,2,2,2,6) == 18
        assert Yatzy.fullHouse(2,3,4,5,6) == 0
        assert Yatzy.fullHouse(6,2,1,2,6) == 0
        assert Yatzy.fullHouse(6,2,6,1,6) == 0
        assert Yatzy.fullHouse(6,6,2,2,2) == 18
        assert Yatzy.fullHouse(6,6,6,2,2) == 22
        assert Yatzy.fullHouse(1,2,3,1,6) == 0

