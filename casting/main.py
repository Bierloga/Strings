# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print('Leek is '+str(leek_price)+' euro per kilo.')

order = 'leek 4'
amount_index = order.find('4')
order_amount = int(order[amount_index])
sum_total = order_amount*leek_price
print(sum_total)

broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'
amount_index_broc = broccoli_order.find('1.6')
order_amount_broc = broccoli_order[amount_index_broc:]
sum_total_broc = round(float(order_amount_broc)*broccoli_price, 2)
print(order_amount_broc+'kg broccoli costs '+str(sum_total_broc)+'e')