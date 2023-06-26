"""debug by printing"""


def check_sorted_list(sorted_list):
    is_list_sorted = True
    for i in range (len(sorted_list)-1):
        if sorted_list[i+1] < sorted_list[i]:
            is_list_sorted = False
    return is_list_sorted
    


mylist = [12, 13, 14, 16, 12, 17]
print(mylist, "sorted", check_sorted_list(mylist))
# [12, 13, 14, 16, 12, 17] sorted False



