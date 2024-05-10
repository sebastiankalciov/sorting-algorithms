def insertion_sort(array):

	for iteration in range(1, len(array)):
	
		current_item = array[iteration]
	
		j = iteration - 1
	
		while j >= 0 and current_item < array[j]:
		
			array[j + 1] = array[j]
			j = j - 1
	
		array[j + 1] = current_item

  
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

	print("--------- STATS FOR INSERTION SORT (SMALL SET OF DATA - 100 ELEMENTS) ---------\n")
	
	cProfile.run("insertion_sort(small_data)", 'restats')
	
	statistics = pstats.Stats('restats')
	
	statistics.strip_dirs().print_stats('insertion_sort.py')
	
	print("--------- STATS FOR INSERTION SORT (MEDIUM SET OF DATA - 1000 ELEMENTS) ---------\n")
	
	cProfile.run("insertion_sort(medium_data)", 'restats')
	
	statistics = pstats.Stats('restats')
	
	statistics.strip_dirs().print_stats('insertion_sort.py')
	
	
	print("--------- STATS FOR INSERTION SORT (LARGE SET OF DATA - 1 000 000 ELEMENTS) ---------\n")
	
	cProfile.run("insertion_sort(large_data)", 'restats')
	
	statistics = pstats.Stats('restats')
	
	statistics.strip_dirs().print_stats('insertion_sort.py')