def bubble_sort(array): 
     
	length_array = len(array) 

	for i in range(length_array): 
		for j in range(0, length_array - i - 1):
		
			if array[j] > array[j + 1]:
				
				array[j], array[j + 1] = array[j + 1], array[j]
				

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
    print("--------- STATS FOR BUBBLE SORT (SMALL SET OF DATA - 100 ELEMENTS) ---------\n")
    cProfile.run("bubble_sort(small_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('bubble_sort.py')
    
    print("--------- STATS FOR BUBBLE SORT (MEDIUM SET OF DATA - 1000 ELEMENTS) ---------\n")
    cProfile.run("bubble_sort(medium_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('bubble_sort.py')

    print("--------- STATS FOR BUBBLE SORT (LARGE SET OF DATA - 1 000 000 ELEMENTS) ---------\n")
    cProfile.run("bubble_sort(large_data)", 'restats')
    statistics = pstats.Stats('restats')
    statistics.strip_dirs().print_stats('bubble_sort.py')
