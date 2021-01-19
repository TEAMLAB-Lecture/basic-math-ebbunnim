def get_greatest(number_list):
    return max(number_list)


def get_smallest(number_list):
    return min(number_list)


def get_mean(number_list):
    return sum(number_list)/len(number_list)


def get_median(number_list):
    number_list.sort()
    l=len(number_list)
    if l%2:
        return number_list[l//2]
    a,b=number_list[l//2-1],number_list[l//2]
    return (a+b)/2


print(get_mean([54, 56, 30, 12, 58, 25, 17, 48, 80, 23]))