class Stu:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.che + self.math)/3) +"%"
        
stu1 = Stu(98,99,87)
print(stu1.percentage)

stu1.phy = 88
print(stu1.percentage)