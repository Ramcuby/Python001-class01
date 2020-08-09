from abc import ABCMeta, abstractmethod

class Zoo(object):
    def __init__(self, name):
        self.animal = []
        self.zoo_name = name

    def add_animal(self, animal):
        if animal in self.animal:       #同一只动物只能被添加一次
            return self.animal[animal]
        else:
            self.animal.append(animal)
            self.__dict__[type(animal).__name__] = animal


class Animal(metaclass=ABCMeta):
    is_carnivore = {
        '食肉': True,
        '食草': False,
        '杂食': False
    }
    size = {
        '小型': 1,
        '中型': 2,
        '大型': 3
    }
    character = {
        '凶猛': True,
        '温顺': False
    }

    @abstractmethod     #抽象类不能被实例化，动物类不允许被实例化
    def __init__(self, is_carnivore, size, character):
        self.size = size
        self.is_carnivore = is_carnivore
        self.character = character

        if self.size >= '2' and self.is_carnivore == True and self.character == True:
            self.is_fierce_animal = True
        else:
            self.is_fierce_animal = False


class Cat(Animal):   #猫类继承自动物类
    bark = 'meow'     #“叫声”作为类属性

    def __init__(self, name, is_carnivore, size, character):
        super(Cat, self).__init__(is_carnivore, size, character)
        self.name = name
        self.is_suited_for_pet = 'YES'


if __name__ == '__main__':
    #实例化动物园
    z = Zoo('时间动物园')
    #实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小型', '温顺')
    print(f'Cat sounding: {Cat.bark}')
    print(f'cat is good for pet: {cat1.is_suited_for_pet}')
    #增加一只猫到动物园
    z.add_animal(cat1)
    #动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    #z.add_animal(cat1)    #再次添加会报错
    print(f'zoo has cat: {bool(have_cat)}')
