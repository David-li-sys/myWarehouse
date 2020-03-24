def binary_search(list,gass):
    head=0
    tail=len(list)-1
    while head<=tail:
        mid=(head+tail)//2
        if list[mid]==gass:
            return mid
        if gass<list[mid]:
            tail=mid-1
        else:
            head=mid+1
    return None

list=[2,3,5,7,9]
print(binary_search(list,0))
