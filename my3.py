print(__name__)


class woman():

    def create(name, height, weight, iq):
        person = woman()
        person.name = name
        person.weight = weight
        person.height = height
        person.iq = iq

        return person

    def eat(self):
        self.weight += 11

        print("{}가 먹어서 {}kg이 되었다 키는{}cm 아이큐는{} ".format(self.name, self.weight, self.height, self.iq))

    def sleep(self):
        self.height -= 1

        print("{}가 잠을 자서 {}CM가 되었다 몽무게는{}kg 아이큐는{}".format(self.name, self.height, self.weight, self.iq))

    def study(self):
        self.iq += 100

        print("{}가 아이큐 {}로 되었다 몸무게는{}kg 키는{}cm ".format(self.name, self.iq, self.weight, self.height))