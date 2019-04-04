class Human(object):

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def myInfo(self):
        print('我叫%s,我今年%s岁,性别:%s'%(self.name,self.age,self.sex))
class zhiXingCeShi(Human):

      def zhiXing(self):
       print(self.name)
       print('哦哦哦哦哦哦哦哦')
       self.myInfo()


if __name__ == '__main__':
    # human = Human('宗',18,'男')
    # human.myInfo()
    zhixing1 = zhiXingCeShi('zong',18,'男')
    zhixing1.zhiXing()



