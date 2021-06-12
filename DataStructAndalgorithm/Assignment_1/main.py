"""
Tên chương trình: menu_show
Đối số truyền vào: None
Chức năng: Hiển thị menu 
"""
def menu_show():
    a="""
    +-------------------Menu------------------+
    |      1.Manual Input                     |
    |      2.File input                       |
    |      3.Bubble sort                      |
    |      4.Selection sort                   |
    |      5.Insertion sort                   |
    |      6.Search > value                   |
    |      7.Search = value                   |
    |      0.Exit                             |
    +-----------------------------------------+"""
    print(a)
"""
Tên chương trình: Manual_Input
Đối số truyền vào: dir_ (đường dẫn để lưu, mặc định là INPUT.txt)
Chức năng: Nhập mảng giá trị từ bàn phím và lưu vào file
"""
def Manual_Input(dir_):
    print("Nhập giá n số thực:")
    _n=None
    while True:
        try:
            _n=int(input())
            break
        except:
            print("Nhập lại giá trị của n: ")
    _arr=[]
    for i in range(1,_n+1):
        print("Nhập giá trị thứ {}: ".format(i))
        _arr.append(str(input()))
    with open(dir_,"w") as f:
        f.write(" ".join(_arr))

"""
Tên chương trình: File_input
Đối số truyền vào: dir_ (đường dẫn để lấy dữ liệu, mặc định là INPUT.txt)
Chức năng: lấy dữ liệu từ file và lưu thành mảng
"""
def File_input(dir_):
    try:
        f = open(dir_, "r")
        str =f.read()
        f.close()
        print(str)
        return [float(i.strip()) for i in str.split(" ")]
    except FileNotFoundError:
        print("No such file or directory of {}".format(dir_))
        return []

"""
Tên chương trình: Bubble_sort
Đối số truyền vào: dir_ (đường dẫn để lưu dữ liệu, mặc định là OUTPUT1.txt) và mảng giá trị đầu vào
Chức năng: sắp xếp giá trị của mảng tăng dần dùng sắp xếp nổi bọt

Mã giả: 
    Bubble_sort(arr,n):
        for i from 0 to n-2:
            for j from 0 to n-2-i:
                if a[j] > a[j+1]:
                    swap(a[j],a[j+1])
Thời gian thực thi: Tốt và xấu: n*(n-1)/2 = O(n^2)
Memory: O(1)
"""
def Bubble_sort(brr_,dir_):
    if len(brr_)==0:
        print("Quay lại lựa chọn 1")
        return False
    arr_ =brr_.copy()
    with open(dir_,"w") as f:
        for i in range(len(arr_)-1):
            for j in range(len(arr_)-i-1):
                if(arr_[j]>arr_[j+1]):
                    arr_[j],arr_[j+1]=arr_[j+1],arr_[j]
            print(*arr_)
            f.write( " ".join([str(i) for i in arr_])+"\n")

"""
Tên chương trình: Insertion_sort
Đối số truyền vào: dir_ (đường dẫn để lưu dữ liệu, mặc định là OUTPUT2.txt) và mảng giá trị đầu vào
Chức năng: sắp xếp giá trị của mảng tăng dần 

Mã giả: 
    Insertion_sort(a,n):
        for i from 1 to n-1:
            for j from 0 to i:
                if a[i] < a[j]:
                    swap(a[i],a[j])
Thời gian thực thi: O(N^2)
Memory: O(1)
"""
def Insertion_sort(brr_,dir_):
    arr_=brr_.copy()
    if len(arr_)==0:
        print("Quay lại lựa chọn 1")
        return False
    n = len(arr_)
    with open(dir_,"w") as f:
        for i in range(1,n):
            for j in range(i):
                if(arr_[i]<arr_[j]):
                    arr_[j],arr_[i]=arr_[i],arr_[j]
            print(*arr_)
            f.write( " ".join([str(i) for i in arr_])+"\n")

"""
Tên chương trình: Selection_sort
Đối số truyền vào: dir_ (đường dẫn để lưu dữ liệu, mặc định là OUTPUT3.txt) và mảng giá trị đầu vào
Chức năng: sắp xếp giá trị của mảng tăng dần 

Mã giả: 
    Selection_sort(a,n):
        for i from 0 to n-2:
            minIndex = i
            for j from i+1 to n-1:
                if a[j] < a[minIndex]:
                    minIndex = j
            if minIndex != i:
                swap(a[i],a[minIndex])
Thời gian thực thi: O(N^2)
Memory: O(1)
"""
def Selection_sort(brr_,dir_):
    arr_ = brr_.copy()
    if len(arr_)==0:
        print("Quay lại lựa chọn 1")
        return False
    n = len(arr_)
    with open(dir_,"w") as f:
        for i in range(n-1):
            minIndex=i
            for j in range(i+1,n):
                if(arr_[j]<arr_[minIndex]):
                    minIndex = j
            if(minIndex !=i):
                arr_[i],arr_[minIndex]=arr_[minIndex],arr_[i]
            print(*arr_)
            f.write( " ".join([str(i) for i in arr_])+"\n")

"""
Tên chương trình: Linear_search
Đối số truyền vào: dir_ (đường dẫn để lưu dữ liệu, mặc định là OUTPUT4.txt) và mảng giá trị đầu vào
Chức năng: Tìm những giá trị lớn hơn giá trị nhập vào

Mã giả: 
    Linear_search(a,n,key):
        for i from 0 to n-1:
            if a[i] >key:
                save i
Thời gian thực thi: O(N)
"""
def Linear_Search(brr_,dir_):
    arr_=brr_.copy()
    print("Nhập giá trị cần tìm: ")
    _n=None
    while True:
        try:
            _n=int(input())
            break
        except:
            print("Nhập lại: ")
    if len(arr_)==0:
        print("Quay lại lựa chọn 1")
        return False
    
    with open(dir_,"w+") as f:
        arr_index=[]
        for i in range(len(arr_)):
            if arr_[i]>_n:
                arr_index.append(i)
        print(*arr_index)
        f.write( " ".join([str(i) for i in arr_index])+"\n")

"""
Tên chương trình: Binary_search
Đối số truyền vào: left,right,key,arr
Chức năng: Tìm vị trí dầu tiên xuất hiện giá trị cần tìm

Mã giả: 
    Binary_Search(arr,left,right,key):
        if left > right :
            return -1
        mid = left +(right-left)//2
        if key == arr[mid]:
            return mid
        elif key <arr[mid]:
            return mid
        elif key <arr[mid]:
            return Binary_search(arr,left,mid-1,key)
        else:
            return Binary_search(arr,mid+1,right,key)
Thời gian thực thi: O(logN)
Điều kiện: mảng đầu vào phải được sắp xếp rồi
"""
def Binary_Search(arr,left,right,key):
    if(left>right):
        return -1
    mid =left+(right-left)//2
    if key == arr[mid]:
        return mid
    elif key <arr[mid]:
        return Binary_Search(arr,left,mid-1,key)
    elif key >arr[mid]:
        return Binary_Search(arr,mid+1,right,key)
"""
Tên chương trình: Search
Đối số truyền vào: arr
Chức năng: Tìm vị trí dầu tiên xuất hiện giá trị cần tìm
"""
def Search(brr_):
    arr_=brr_.copy()
    print("Nhập giá trị cần tìm: ")
    key=None
    while True:
        try:
            key=int(input())
            if(key not in arr_):
                print("Nhập lại: ")
                continue
            break
        except:
            print("Nhập lại: ")
    if len(arr_)==0:
        print("Quay lại lựa chọn 1")
        return False
    arr_.sort()
    out=Binary_Search(arr_,0,len(arr_),key)
    print(out+1)


"""
Chương trình chính
Chức năng: Thực thi các yêu cầu trước đó
"""
if __name__=="__main__":
    arr=[]
    while (True):
        menu_show()
        key=input("Your Choice is: ")
        if(key=="1"):
            print("Choice 1: Manual Input")
            Manual_Input("INPUT.txt")
        elif(key=="2"):
            print("Choice 2: File Input")
            arr=File_input("INPUT.txt")
        elif(key=="3"):
            print("Choice 3: Bubble sort")
            Bubble_sort(arr,"OUTPUT1.txt")
        elif(key=="4"):
            print("Choice 4: Selection sort")
            Selection_sort(arr,"OUTPUT2.txt")
        elif(key=="5"):
            print("Choice 5: Insertion sort")
            Insertion_sort(arr,"OUTPUT3.txt")
        elif(key=="6"):
            print("Choice 6: Linear Search")
            Linear_Search(arr,"OUTPUT4.txt")
        elif(key=="7"):
            print("Choice 7: Binary Search")
            Search(arr)
        elif(key=="0"):
            print("Thanks !!")
            break
        else:
            continue

"""
Ngoài ra còn Quick sort, Merge sort, count sort
"""