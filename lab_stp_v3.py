import time
# import random
def bubble_sort(nums):
	# Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
	start_time = time.time_ns()
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				# Меняем элементы
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
				# Устанавливаем swapped в True для следующей итерации
				swapped = True
	stop_time = time.time_ns()
	return (stop_time - start_time)/1000000000
	# print('Пузырьковая сортировка', (stop_time - start_time)/1000000000, 'секунд')#"--- %s seconds ---" % (time.time()*1000 - start_time*1000))

def selection_sort(nums):
	# Значение i соответствует кол-ву отсортированных значений
	start_time = time.time_ns()
	for i in range(len(nums)):
		# Исходно считаем наименьшим первый элемент
		lowest_value_index = i
		# Этот цикл перебирает несортированные элементы
		for j in range(i + 1, len(nums)):
			if nums[j] < nums[lowest_value_index]:
				lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
		nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
	stop_time = time.time_ns()
	return (stop_time - start_time)/1000000000
	# print('Сортировка выборкой', (stop_time - start_time)/1000000000, 'секунд')#"--- %s seconds ---" % (time.time()*1000 - start_time*1000))

def insertion_sort(nums):
	# Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
	start_time = time.time_ns()
	for i in range(1, len(nums)):
		item_to_insert = nums[i]
		# Сохраняем ссылку на индекс предыдущего элемента
		j = i - 1
		# Элементы отсортированного сегмента перемещаем вперёд, если они больше
		# элемента для вставки
		while j >= 0 and nums[j] > item_to_insert:
			nums[j + 1] = nums[j]
			j -= 1
		# Вставляем элемент
		nums[j + 1] = item_to_insert
	stop_time = time.time_ns()
	return (stop_time - start_time)/1000000000
	# print('Сортировка вставками', (stop_time - start_time)/1000000000, 'секунд')#"--- %s seconds ---" % (time.time()*1000 - start_time*1000))

def partition(nums, low, high):
	# Выбираем средний элемент в качестве опорного
	# Также возможен выбор первого, последнего
	# или произвольного элементов в качестве опорного
	pivot = nums[(low + high) // 2]
	i = low - 1
	j = high + 1
	while True:
		i += 1
		while nums[i] < pivot:
			i += 1

		j -= 1
		while nums[j] > pivot:
			j -= 1

		if i >= j:
			return j

		# Если элемент с индексом i (слева от опорного) больше, чем
		# элемент с индексом j (справа от опорного), меняем их местами
		nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
	# Создадим вспомогательную функцию, которая вызывается рекурсивно
	start_time = time.time_ns()
	def _quick_sort(items, low, high):
		if low < high:
			# This is the index after the pivot, where our lists are split
			split_index = partition(items, low, high)
			_quick_sort(items, low, split_index)
			_quick_sort(items, split_index + 1, high)

	_quick_sort(nums, 0, len(nums) - 1)
	stop_time = time.time_ns()
	return (stop_time - start_time)/1000000000
	# print('Быстрая сортировка', (stop_time - start_time)/1000000000, 'секунд')#"--- %s seconds ---" % (time.time()*1000 - start_time*1000))

def heapify(nums, heap_size, root_index):
	# Индекс наибольшего элемента считаем корневым индексом
	largest = root_index
	left_child = (2 * root_index) + 1
	right_child = (2 * root_index) + 2

	# Если левый потомок корня — допустимый индекс, а элемент больше,
	# чем текущий наибольший, обновляем наибольший элемент
	if left_child < heap_size and nums[left_child] > nums[largest]:
		largest = left_child

	# То же самое для правого потомка корня
	if right_child < heap_size and nums[right_child] > nums[largest]:
		largest = right_child

	# Если наибольший элемент больше не корневой, они меняются местами
	if largest != root_index:
		nums[root_index], nums[largest] = nums[largest], nums[root_index]
		# Heapify the new root element to ensure it's the largest
		heapify(nums, heap_size, largest)

def heap_sort(nums):
	start_time = time.time_ns()
	n = len(nums)

	# Создаём Max Heap из списка
	# Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
	# перед первым элементом списка
	# 3-й аргумент означает повторный проход по списку в обратном направлении, 
	# уменьшая счётчик i на 1 
	for i in range(n, -1, -1):
		heapify(nums, n, i)

	# Перемещаем корень Max Heap в конец списка
	for i in range(n - 1, 0, -1):
		nums[i], nums[0] = nums[0], nums[i]
		heapify(nums, i, 0)
	stop_time = time.time_ns()
	return (stop_time - start_time)/1000000000
	# print('Сортировка кучей', (stop_time - start_time)/1000000000, 'секунд')#"--- %s seconds ---" % (time.time()*1000 - start_time*1000))