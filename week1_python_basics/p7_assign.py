total_land = 80
segments = 5
land = total_land/segments

tomato_30=0.3*land*10*1000
tomato_70=0.7*land*12*1000
tomato_total=tomato_30+tomato_70
tomato_sale=tomato_total*7

potato_total=land*10*1000
potato_sale=potato_total*20

cabbage_total=land*14*1000
cabbage_sale=cabbage_total*24

sunflower_total=land*0.7*1000
sunflower_sale=sunflower_total*200

sugarcane_total=land*45
sugarcane_sale=sugarcane_total*4000 

total_sales = tomato_sale + potato_sale + cabbage_sale + sunflower_sale + sugarcane_sale
sales_after_11_months = tomato_sale + potato_sale + cabbage_sale + sunflower_sale

print("The overall sales achieved by Mahesh from the 80 acres of land = {}".format(total_sales))
print("Sales realisation from chemical-free farming at the end of 11 months = {}".format(sales_after_11_months))
