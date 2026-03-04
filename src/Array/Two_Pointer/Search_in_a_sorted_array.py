def search_in_a_sorted(lst, element)->int:
    #Assume the list is sorted already
    #[1,5,8,9]
    low = 0; 
    high =len(lst)-1;
    while(low<=high):
        mid = int((low+high)/2)
        if(lst[mid]==element):
            return mid
        elif(lst[mid]>element):
            high = mid-1
        else:
            low = mid+1
    return -1
#Odd Len list
num = [1,3,4,5,5,6,7,8,9]
# Odd len search in left
op = search_in_a_sorted(num , 4)
print(op)
# Odd len search in right
print(search_in_a_sorted(num , 7))
# Odd len search in middle
op = search_in_a_sorted(num , 5)
print(op)
# Odd len search in right
print(search_in_a_sorted(num , 89))




