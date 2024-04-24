

icecream_txt = open(r"C:\Users\DNY123\Desktop\coding\LabIntermediateProgramming-CelineDavinaMasko\New folder\icecream.txt")
sales_data = {}
while True :
    linecream = icecream_txt.readline()
    for i in linecream:
        list_per_line = linecream.strip().split(':')
        key = list_per_line.pop(0)

        modiflist = [eval(i) for i in list_per_line]
        sum_per_flav = sum(modiflist)
        list_per_line.append(sum_per_flav)

        sales_data[key] = list_per_line
    if not linecream:
        break

print(sales_data, "\n\n")

sum_per_day = []
total_per_day = []

for key, value in sales_data.items():
    value1, value2, value3, value4 = value
    sum_per_day.append(value1)
    modif_list2 = [eval(i) for i in sum_per_day]
    total_per_day.append(sum(modif_list2))


# 4. print in a report
print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('FLAVOR', 'VALUE1', 'VALUE2','VALUE3', 'SUM PER FALVOR' ))
 
# print each data item.
for key, value in sales_data.items():
    value1, value2, value3, value4 = value
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(key, value1, value2, value3, value4))

print("totperday", *total_per_day, sep="  ")
print("\n")
