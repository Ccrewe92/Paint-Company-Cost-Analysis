#Clinton Crewe
#November - 12 - 2022
#SAIT CRPG216
#A program for Shiny Paint(SP) to calculate amount of paint and cost needed for specific room.



# INDEPENDENT VARIABLES ($CDN / sq FEET) #

current_price_gallon = 42
coverage_of_gallon_paint = 350
price_of_labour = 0.15
profit_margin = .30


# FUNCTIONS #

def computePaintPrice(gallons):
	total_gallon_cost = gallons * current_price_gallon
	return total_gallon_cost

def computeGallons(area):
	total_gallons = area/coverage_of_gallon_paint
	return total_gallons

def computeCustomWallsArea():
	walls = eval(input("How many walls are there in the room? "))
	total_area = 0
	for w in range(1, walls + 1):
		length = eval(input(f'Enter the length of wall {w} in feet:'))
		width = eval(input(f'Enter the width of wall {w} in feet: '))
		
		total_area += length * width
	return total_area

def computeSquareArea(length):
	return length ** 2

def computeSquareWallsArea():
	length = eval(input("Enter one side length of the room: "))
	height = eval(input("Enter the height of the room in feet: "))
	area_per_wall = computeRectangleArea(length, height)
	return 4 * area_per_wall

def computeRectangleArea(length, width):
	area = length * width
	return area

def computeWindowsDoorsAreas():
	windows_doors = eval(input("How many windows and doors are in the room? "))
	total_area = 0
	for win_do in range(1, windows_doors + 1):
		length = eval(input(f'Enter window/door length for window/door {win_do} in feet: '))
		width = eval(input(f'Enter window/door width for window/door {win_do} in feet: '))
		total_area += width * length
	return total_area
	

def computeRectangleWallsArea():
	length = eval(input("Enter the length of the room in feet: "))
	width = eval(input("Enter the width of the room in feet: "))
	height = eval(input("Enter the height of the room in feet: "))
	
	area_length = computeRectangleArea(length, height)
	area_width = computeRectangleArea(width, height)
	
	return 2 * area_length + 2 * area_width


def computeRoomArea(room_no):
	
	
	
	print("Room:", room_no)
	print("Select the shape of the room: \n 1 - Rectangle \n 2 - Square \n 3 - Custom ((more or less than 4 walls, all square or rectangles)")
	option = input("Option: ")
	
	if option == "1":
		area = computeRectangleWallsArea()
		window_area = computeWindowsDoorsAreas()
		
		area_to_be_painted = area - window_area
		gallons_required = computeGallons(area_to_be_painted)
		paint_price = computePaintPrice(gallons_required)
		
		
		print(f'For Room: {room}, Area to be painted is {area_to_be_painted:.2f} square ft'
		      f'and will require {gallons_required:.2f} gallons to paint. '
		      f'The paint will cost approximately ${paint_price:2f}')
		
	if option == "2":
		area = computeSquareWallsArea()
		window_area = computeWindowsDoorsAreas()
		
		area_to_be_painted = area - window_area
		gallons_required = computeGallons(area_to_be_painted)
		paint_price = computePaintPrice(gallons_required)

		
		print(f'For Room: {room}, Area to be painted is {area_to_be_painted:.2f} square ft'
		      f'and will require {round(gallons_required, 2)} gallons to paint. '
		      f'The paint will cost approximately ${paint_price:.2f}')
	
	if option == "3":
		area = computeCustomWallsArea()
		window_area = computeWindowsDoorsAreas()
		
		area_to_be_painted = area - window_area
		gallons_required = computeGallons(area_to_be_painted)
		paint_price = computePaintPrice(gallons_required)
		
		print(f'For Room: {room}, Area to be painted is {area_to_be_painted:.2f} square ft'
		      f'and will require {gallons_required:.2f} gallons to paint. '
		      f'The paint will cost approximately ${paint_price:.2f}')
			
	return area_to_be_painted
	
	

# START OF PROGRAM #

print("Welcome to Shiny Paint Company for indoor painting!")

rooms = eval(input("How many Rooms do you want to paint?: "))
total_area = 0
for room in range(1, rooms+1):
	
	
	area = computeRoomArea(rooms)
	total_area += area

total_gallons = round(computeGallons(total_area), 0)
total_paint_price = computePaintPrice(total_gallons)
labour_cost = total_area * 0.15
profit = (total_paint_price + labour_cost) * profit_margin

total_price = total_paint_price + labour_cost + profit

print(f'Total area to be painted is {total_area} square ft and will require {total_gallons} gallons to paint.')
print(f'The total customer estimate including paint, labor, and overhead is ${total_price:.2f}')
