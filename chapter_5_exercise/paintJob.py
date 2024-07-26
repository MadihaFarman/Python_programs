PER_HOUR_LABOR_COST = 35
STANDARD_WALL_SPACE = 112
def main():
    wall_space_sq_ft = float(input('Enter sq ft of wall space to be painted: '))
    price_per_gallon = float(input('Enter price per gallon: '))
    paint_gallons = gallons_required(wall_space_sq_ft)
    print('Number of paint gallons required for',wall_space_sq_ft,'sq ft wall :',paint_gallons)
    hours = hours_required(wall_space_sq_ft)
    print('Hours required :',hours)
    costOfPaint = paint_cost(paint_gallons,price_per_gallon)
    print('Paint cost :',costOfPaint)
    chargesOfLabor = labor_charges(hours)
    print('Labor charges :',chargesOfLabor)
    print('Total cost of the paint job :',total_job_cost(costOfPaint,chargesOfLabor))

def gallons_required(sq_ft):
   return sq_ft/STANDARD_WALL_SPACE
def hours_required(sq_ft):
    return sq_ft*8/STANDARD_WALL_SPACE
def paint_cost(gallons,priceOf1Gallon):
    return gallons*priceOf1Gallon
def labor_charges(hours):
    return hours * PER_HOUR_LABOR_COST
def total_job_cost(paint_cost,labor_cost):
    return paint_cost + labor_cost
main()