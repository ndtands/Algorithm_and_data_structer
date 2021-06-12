"""
class name :  Node
Atribute:Id,Title,quantity,price,next
Method: No method
Description: Save data
"""
class Node :
    def __init__(self,Id,Title,quantity,price):
        self.Id         = Id
        self.Title      = str(Title)
        self.quantity   = int(quantity)
        self.price      = float(price)
        self.next       = None


"""
class name :  Mylist
Atribute:start_node: Lưu vị trí đầu tiên của Linkedlist
Method: insert_at_end, delete_by_Id, Search_by_Id,Display_data,Sorted_mylist,Convert_quantity2binary
Description: Stored information and method with linkedlist
"""        
class Mylist:
    def __init__(self):
        self.start_node = None
    '''
    pesudocode:
        Inset_at_end(start_node,value):
            new_Node = Node(value)
            #Nếu None thì thêm mới
            if start_node is None:
                start_node = new_Node
                return 
            temp = start_node
            # Tìm head của node cuối cùng
            while temp.next is not None:
                temp = temp.next
            temp.next = new_Node
    '''
    def insert_at_end(self,Id,Title,quantity,price):
        new_node = Node(Id,Title,quantity,price)
        if self.start_node is None:
            self.start_node = new_node
            return 
        temp = self.start_node
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    '''
    pesudocode:

        Delete_by_Id(start_node,Id):
            if start_node is None:
                return 
            # Đó là Node đầu tiên thì chỉ cần bỏ qua nó
            if start_node.Id == Id:
                print (****)
                start_node = start_node.next
                return 
            temp = start_node
            while temp.next is not None:
                if temp.next.Id == Id:
                    break
                temp = temp.next
            #Tìm vị trí cần xóa trước đó 1 node
            if temp.next is None:
                print (" No finding ID")
            else:
                temp.next = temp.next.next
                print ("Done for Delete)
    '''
    def delete_by_Id(self,Id):
        if self.start_node is None:
            print("Dataset is Empty")
            return 
        if self.start_node.Id == Id:
            print(" | ".join(["ID","Title","Quantity","Price"]))
            print(" | ".join([str(self.start_node.Id),str(self.start_node.Title),str(self.start_node.quantity),str(self.start_node.price)]))
            self.start_node = self.start_node.next
            print("The product is removed from the dataset successfully!")
            return 
        temp = self.start_node
        while temp.next is not None:
            if temp.next.Id == Id:
                break
            temp  = temp.next
        #return node before Id
        #Node end
        if temp.next is None:
            print("ID is not in the dataset")
        else:
            print(" | ".join(["ID","Title","Quantity","Price"]))
            print(" | ".join([str(temp.Id),str(temp.Title),str(temp.quantity),str(temp.price)]))
            temp.next = temp.next.next
            print("The product is removed from the dataset successfully!")
    '''
    pesudocode:
        Search_by_Id(start_node,Id):
            if start_node is None:
                return 
            temp = start_node
            while temp is not None:
                if temp.Id == Id:
                    print("Fiding Done")
                    return 
                temp = temp.next
            return False
    '''
    def Search_by_Id(self,Id):
        if self.start_node is None:
            print("The dataset is Empty")
            return 
        temp = self.start_node
        while temp is not None:  
            if temp.Id == Id:
                print(" | ".join(["ID","Title","Quantity","Price"]))
                print(" | ".join([str(temp.Id),str(temp.Title),str(temp.quantity),str(temp.price)]))
                return
            temp = temp.next
        print("ID is not in the dataset! ")
        return False
    '''
    pesudocode:
        Display(start_node):
            if start_node is None:
                return 
            temp = start_node
            while temp is not None:
                print("Data")
                temp = temp.next
    '''
    def Display_data(self):
        temp= self.start_node
        if temp is None:
            return 
        print(" | ".join(["ID","Title","Quantity","Price"]))
        while temp is not None:
            print(" | ".join([str(temp.Id),str(temp.Title),str(temp.quantity),str(temp.price)]))
            temp = temp.next
    '''
    Dung sap xep noi bot
        So sanh i va i+1 dung j lam trung gian 
        update end la node cuoi
        i ->start-> node cuoi-1
        vong dau: khac None
    pesudocode:
        for end from n-1 to start_node:
            for i from start_node to end:
                a[i]>a[i+1]:
                    swap(a[i],a[i+1])
    '''
    def Sorted_Mylist(self):
        end = None # init end is a last Node
        while end != self.start_node:
            i = self.start_node
            while i.next != end:
                j= i.next
                if(i.Id > j.Id): # i and i+1
                    i.Id,j.Id=j.Id,i.Id
                    i.Title,j.Title=j.Title,i.Title
                    i.quantity,j.quantity=j.quantity,i.quantity
                    i.price,j.price=j.price,i.price
                i = i.next #i + = 1
            end = i
    
    """
    pesudocode
        Dec2Bin(n):
            if n>1:
                Dec2Bin(n//2)
            print(n%2,end ='')
    """
    def decTobin(self,n):
        if n > 1:
            self.decTobin(n//2)
        print(n % 2,end = '')

    def Convert_quantity2binary(self,Id):
        if self.start_node is None:
            print("The dataset is Empty")
            return 
        temp = self.start_node
        while temp is not None:  
            if temp.Id == Id:
                print(" | ".join(["ID","Title","Quantity","Price"]))
                print(" | ".join([str(temp.Id),str(temp.Title),str(temp.quantity),str(temp.price)]))
                print("Convert quantity to binary:",end=" ")
                self.decTobin(temp.quantity)
                print("")
                return
            temp = temp.next
        print("ID is not in the dataset! ")
        return False

"""
LIFO
class name :  Stack
Atribute: stack: Nơi lưu trữ stack
Method: pop,push,size,top,isempty
Description: information and method with stack
"""    
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.size()>0
"""
FIFO
class name :  Queue
Atribute: queue: Nơi lưu trữ queue
Method: enqueue,dequeue,size,isEmpty
Description: information and method with stack
""" 
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 
        
    def isEmpty(self):
        return self.size()>0

"""
class name : OperationToProduct
Atribute: Dataset,TempDataset,Stack,Queue
Method: 
    + Load_data_and_display,Input_and_Add_data
    + Show_dataset,Save_product,Search,Delete,Sorted
    + Convert2Binary,load_stack_and_display
    + Load_queue_and_display
Description: include all method for this problem
""" 
class OperationToProduct:
    def __init__(self):
        self.Dataset        = Mylist()
        self.TempDataset    = Mylist()
        self.Stack          = Stack()
        self.Queue          = Queue()
    
    def Load_data_and_display(self):
        file_dir =input("Please enter the find path: ")
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
        for product in Data:
            self.Dataset.insert_at_end(product[0],product[1],product[2],product[3])
            self.TempDataset.insert_at_end(product[0],product[1],product[2],product[3])
        self.Dataset.Display_data()
   
    def Input_and_Add_data(self):
        Id      = input("Please enter the new product ID: ")
        Name    = input("Please enter the product's name: ")
        Quantity= input("Please enter the product's quantity: ")
        Price   = input("Please enter the product's price: ")
        self.Dataset.insert_at_end(Id,Name,int(Quantity),float(Price))

    def Show_dataset(self):
        self.Dataset.Display_data()
    
    def Save_product(self):
        file_dir = input("Please enter the output path: ")
        with open(file_dir,"w") as f:
            temp = self.Dataset.start_node
            if temp is None:
                return 
            f.write(" , ".join(["ID","Title","Quantity","Price"])+"\n")
            while temp is not None:
                f.write(" , ".join([str(temp.Id),str(temp.Title),str(temp.quantity),str(temp.price)])+"\n")
                temp = temp.next
        print("The file is saved successfully!")    

    def Search(self):
        Id = input("Please enter the ID: ")
        self.Dataset.Search_by_Id(Id)
    
    def Delete(self):
        Id = input("Please enter the ID: ")
        self.Dataset.delete_by_Id(Id)

    def Sorted(self):
        self.TempDataset.Sorted_Mylist()
        self.TempDataset.Display_data()
    
    def Convert2Binary(self):
        Id = input("Please enter the ID: ")
        self.Dataset.Convert_quantity2binary(Id)

    def Load_stack_and_display(self):
        temp = self.Dataset.start_node
        if temp is None:
            return 
        while temp is not None:
            self.Stack.push([temp.Id,temp.Title,temp.quantity,temp.price])
            temp = temp.next
        print(" | ".join(["ID","Title","Quantity","Price"]))
        while self.Stack.isEmpty():
            out= self.Stack.pop()
            print(" | ".join([str(i) for i in out]))

    def Load_queue_and_display(self):
        temp = self.Dataset.start_node
        if temp is None:
            return 
        while temp is not None:
            self.Queue.enqueue([temp.Id,temp.Title,temp.quantity,temp.price])
            temp = temp.next
        print(" | ".join(["ID","Title","Quantity","Price"]))
        while self.Queue.isEmpty():
            out= self.Queue.dequeue()
            print(" | ".join([str(i) for i in out]))    

"""
class name :  AS2_Main
Atribute: option
Method: menu, main
Description: Finish solving this problem
""" 
class AS2_Main:
    def __init__(self):
        self.option = OperationToProduct()
        
    def Menu(self):
        menu ="""
    +-------------------Menu------------------+
    1.  Load data from file and display
    2.  Input & add to the end
    3.  Display data
    4.  Save product list to file
    5.  Search by ID
    6.  Delete by ID
    7.  Sort by ID
    8.  Convert to Binary 
    9.  Load to stack and display
    10. Load to queue and display

    Exit:
    0.  Exit
    +-----------------------------------------.+
        """
        print(menu)
        return input("Your Choice is: ")

    def main(self):
        while True:
            choice= self.Menu()
            if choice=='1':
                print("Choice 1: Load data from file and display")
                self.option.Load_data_and_display()
            elif choice=='2':
                print("Choice 2: Input & add to the end")
                self.option.Input_and_Add_data()
            elif choice=='3':
                print("Choice 3: Display data")
                self.option.Show_dataset()
            elif choice=='4':
                print("Choice 4: Save product list to file")
                self.option.Save_product()
            elif choice=='5':
                print("Choice 5: Search by ID")
                self.option.Search()
            elif choice=='6':
                print("Choice 6: Deleted by ID")
                self.option.Delete()
            elif choice=='7':
                print("Choice 7: Sorted by ID")
                self.option.Sorted()
            elif choice=='8':
                print("Choice 8: Convert to Binary")
                self.option.Convert2Binary()
            elif choice=='9':
                print("Choice 9: Load to stack and display")
                self.option.Load_stack_and_display()
            elif choice=='10':
                print("Choice 10: Load to queue and display")
                self.option.Load_queue_and_display()
            elif choice=='0':
                print("Thanks !")
                break
            else:
                continue


if __name__ == "__main__":
    Object = AS2_Main()
    Object.main()