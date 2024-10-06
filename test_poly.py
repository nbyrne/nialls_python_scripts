class Polygon(object):
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input("Enter side"+str(i+1)+" : ")) for i in range(self.n)]


    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        super(Triangle, self).__init__(3)

    def findArea(self):
        a, b, c = self.sides 
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('Area of triangle is:  %0.2f' %area)        

def write_bin_file(filename, filter, args):
   with open(filename, 'wb') as F:
        data = struct.pack(filter, *args)
        F.write(data)
   return

def main():
 
#Input: [3,1,2,4] Output: [2,4,3,1] The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
    # testobj = Triangle()
    # testobj.inputSides()
    # testobj.dispSides()
    # testobj.findArea()
    input_list = [4, 3, 1, 2, 7, 9, 8]
    lenght_list = len(input_list)
    print("original list",input_list)
    print("list lenght",lenght_list)

    for i in range(lenght_list):
        if i <= lenght_list:
            if not(input_list[i] % 2):
                print("input_list[i] even element",input_list[i])
                input_list.append(input_list[i]) # even:
    for i in range(lenght_list):
        if i <= lenght_list:
            if(input_list[i] % 2):
                print("input_list[i] odd element",input_list[i])
                input_list.append(input_list[i]) # odd:

    print ("New list",input_list[lenght_list:])
    return

if __name__ == '__main__':
    main()
