class FirstClass:
    def __init__(self,name_list,age_list, position_list):
        self.name_list = name_list
        self.age_list = age_list
        self.position_list = position_list
        self.average_age = 0

    def readfile(self, filename):
        text_list = []
        myfile = open(filename,"r",encoding="utf-8")
        full_list = myfile.readlines()
        myfile.close()
        for i in range (1, len(full_list)):
            line = full_list[i].strip()
            split_list = line.split(";")
            self.name_list.append(split_list[0]) 
            self.age_list.append(int(split_list[1]))  
            self.position_list.append(split_list[2])

    def calculate_average_age(self):
        sum = 0
        for i in range(len(self.age_list)):
            sum += self.age_list[i]
        average_age = sum / len(self.age_list)
        self.average_age = average_age
        


FirstObject = FirstClass(name_list=[],age_list = [],position_list = [])
FirstObject.readfile("text.txt")
print(FirstObject.age_list)
FirstObject.calculate_average_age()
print(FirstObject.average_age)