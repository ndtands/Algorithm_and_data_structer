from utils import *
"""
ClassName: Main
Atribute: Dataset
Method: 
    + Menu, load_Dataset, Insert_Persion
    + Inorder_Traverse,Breadth_First_Traversal 
    + Search_Persion, Delete_Persion, Save_Dataset
    + Selection
"""
class Main:
    def __init__(self):
        self.Dataset = MyBSTree()
    
    def Menu(self):
        menu ="""
+-------------------Menu------------------+
    Person Tree:
    1. Load the data from the file.
    2. Insert a new Person.
    3. Inorder traverse
    4. Breadth-First Traversal traverse
    5. Search by Person ID
    6. Delete by Person ID
    7. Save Dataset
    Exit:
    0. Exit
+-----------------------------------------.+
            """
        print(menu)
        return input("Your Choice is: ")

    def load_Dataset(self):
        file_dir =input("Please enter the find path: ")
        #file_dir ='file.txt'
        Data=[]
        try:
            f = open(file_dir,"r")
            print("The file is loaded successfully !")
            for line in f:
                Data.append([i.strip() for i in line.split(",")])
            f.close()
            Data=Data[1:]

        except FileNotFoundError:
            print("File-path is not correct!")
            return False

        for persion in Data:
            self.Dataset.AddData(int(persion[0]),persion[1],persion[2],persion[3])

    def Insert_Persion(self):
        ID = int(input("Please insert the New ID: "))
        while(True):
            if ID in self.Dataset.idsave:
                print("This ID has been chosen, please choose another ID!")
                ID = int(input("Please insert the New ID: "))
            else:
                break
        name = input("Please insert the Name: ")
        Birthplace=input("Please insert the Birthplace: ")
        Birth = input("Please insert the Birth of Date: ")
        self.Dataset.AddData(ID,name,Birth,Birthplace)
        print("New ID: ",ID)
        print("Name: ",name)
        print("Birthplace: ",Birthplace)
        print("Day of birth: ",Birth)
        while(True):
            key = input("Please type anything to come back to the main menu!\n")
            break
    
    def Inorder_Traverse(self):
        self.Dataset.inOrder()
        while(True):
            key = input("Please type anything to come back to the main menu!\n")
            break
    
    def  Breadth_First_Traversal (self):
        self.Dataset.levelOrder()
        while(True):
            key = input("Please type anything to come back to the main menu!\n")
            break
    
    def Search_Persion(self):
        ID =int(input("Please insert the ID: "))
        node = self.Dataset.Search(ID)
        print("Search for ID = ",ID)
        if node == -1:
            print("The searched ID is not valid")
        else:
            print("ID | Name | Day of Birth | Birthplace")
            print("   ".join([str(node.ID),str(node.Name),str(node.DoB),str(node.Birthplace)]))
        while(True):
            key = input("Please type anything to come back to the main menu!\n")
            break
    
    def Delete_Persion(self):
        ID =int(input("Please insert the ID: "))
        self.Dataset.delete(ID)
        while(True):
            key = input("Please type anything to come back to the main menu!\n")
            break
             
    def Save_Dataset(self):
        file_dir = input("Please enter the output path: ")
        #file_dir = "out.txt"
        if self.Dataset.root is None:
            print("Dataset is Empty")
            return 
        else:
            with open(file_dir,"w") as f:
                f.write(" , ".join(["ID","Title","Quantity","Price"])+"\n")
                queue = MyQueue()
                queue.enqueue(self.Dataset.root)
                while queue.isEmpty():
                    node  = queue.dequeue()
                    f.write(" , ".join([str(node.ID),str(node.Name),str(node.DoB),str(node.Birthplace)])+"\n")
                    if node.left:
                        queue.enqueue(node.left)
                    if node.right:
                        queue.enqueue(node.right)
                print("The Dataset is saved successfully!")                  

    def Selection(self):
        while True:
            choice= self.Menu()
            if choice=='1':
                print("Choice 1: Load data from file to BST")
                self.load_Dataset()
            elif choice=='2':
                print("Choice 2: Insert a new Person")
                self.Insert_Persion()
            elif choice=='3':
                print("Choice 3: Inorder traverse")
                print("ID | Name | Day of Birth | Birthplace")
                self.Inorder_Traverse()
            elif choice=='4':
                print("ID | Name | Day of Birth | Birthplace")
                print("Choice 4: Breadth-First Traversal traverse")
                self.Breadth_First_Traversal()
            elif choice=='5':
                print("Choice 5: Search by Person ID")
                self.Search_Persion()
            elif choice=='6':
                print("Choice 6: Delete by Person ID")
                self.Delete_Persion()
            elif choice=='7':
                print("Choice 7: Save Dataset")
                self.Save_Dataset()
           
            elif choice=='0':
                print("Thanks !")
                break
            else:
                continue
if __name__ == "__main__":
    object = Main()
    object.Selection()
