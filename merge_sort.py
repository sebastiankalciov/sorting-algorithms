def merge_sort(array):

    if len(array) <= 1:
        return array
    

    middle = len(array)//2

    left_side = array[:middle]
    right_side = array[middle:]

    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    return merge(left_side, right_side)

def merge(left_side, right_side):

    sorted_array = []
    left_index, right_index = 0, 0
 

    while left_index < len(left_side) and right_index < len(right_side):

        if left_side[left_index] <= right_side[right_index]:
            sorted_array.append(left_side[left_index])
            left_index += 1

        else:
            sorted_array.append(right_side[right_index])
            right_index += 1

    sorted_array.extend(left_side[left_index:])
    sorted_array.extend(right_side[right_index:])
    
    return sorted_array


def extract_data(file_name, array):

    with open(file_name, "r") as file:
        for item in file:
            array.append(int(item))

small_data = []
medium_data = []
large_data = []

extract_data("data/small_data.txt", small_data)
extract_data("data/medium_data.txt", medium_data)
extract_data("data/extremly_large_data.txt", large_data)

if __name__ == '__main__':

    import cProfile, pstats
    print("\n")
    print("--------- STATS FOR MERGE SORT (SMALL SET OF DATA - 100 ELEMENTS) ---------\n")
    cProfile.run("merge_sort(small_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('merge_sort.py')
    
    print("--------- STATS FOR MERGE SORT (MEDIUM SET OF DATA - 1000 ELEMENTS) ---------\n")
    cProfile.run("merge_sort(medium_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('merge_sort.py')

    print("--------- STATS FOR MERGE SORT (LARGE SET OF DATA - 1 000 000 ELEMENTS) ---------\n")
    cProfile.run("merge_sort(large_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('merge_sort.py')
