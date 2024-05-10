def selection_sort(array):

    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[minimum] > array[j]:
                minimum = j

        array[i], array[minimum] = array[minimum], array[i]


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
    print("--------- STATS FOR SELECTION SORT (SMALL SET OF DATA - 100 ELEMENTS) ---------\n")
    cProfile.run("selection_sort(small_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('selection_sort.py')
    
    print("--------- STATS FOR SELECTION SORT (MEDIUM SET OF DATA - 1000 ELEMENTS) ---------\n")
    cProfile.run("selection_sort(medium_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('selection_sort.py')

    print("--------- STATS FOR SELECTION SORT (LARGE SET OF DATA - 1 000 000 ELEMENTS) ---------\n")
    cProfile.run("selection_sort(large_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('selection_sort.py')