def quick_sort(array, left, right):

    if left < right:

        pivot_value = pivot(array, left, right)

        quick_sort(array, left, pivot_value - 1)
        quick_sort(array, pivot_value + 1, right)

def pivot(array, left, right):

    pivot = array[right]

    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
 
            i += 1
 
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
 
    return i + 1


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
    print("--------- STATS FOR QUICK SORT (SMALL SET OF DATA - 100 ELEMENTS) ---------\n")
    cProfile.run("quick_sort(small_data, 0, len(small_data) - 1)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('quick_sort.py')
    

    print("--------- STATS FOR QUICK SORT (MEDIUM SET OF DATA - 1000 ELEMENTS) ---------\n")
    cProfile.run("quick_sort(medium_data, 0, len(medium_data) - 1)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('quick_sort.py')

    print("--------- STATS FOR QUICK SORT (LARGE SET OF DATA - 1 000 000 ELEMENTS) ---------\n")
    cProfile.run("quick_sort(large_data, 0, len(large_data) - 1)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('quick_sort.py')


