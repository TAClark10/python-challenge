import csv

counter=0
net_total=0
incease_date = ''
increase_profit =-1000000
prev = 0
decrease_date = ''
decrease_profit = -1000000
changes_sum = 0

with open('Resources/budgetdata.csv','r') as csvdata:
  budgetdata=csv.reader(csvdata)
  next(budgetdata)
  for monthmoney in budgetdata:
    counter+=1
    net_total = net_total + int(monthmoney[1])
    if counter !=1:
      changes_sum = changes_sum + int(monthmoney[1]) - prev 
    if int(monthmoney[1]) - prev > increase_profit and counter !=1:
      incease_date =  monthmoney[0]
      increase_profit = int(monthmoney[1]) - prev
    if  prev - int(monthmoney[1]) > decrease_profit and counter !=1:
      decrease_date =  monthmoney[0]
      decrease_profit = prev - int(monthmoney[1])
    prev = int(monthmoney[1])
# the total number of months included in the dataset
total_months=counter
 # the total number of months included in the dataset

 # the average of the changes in "profit/losses" over the entire period
 # 3a list: date of "profit/losses" from month to month

 #3b list: amount of "profit/losses" from month to month

average = changes_sum/float(total_months-1)

#data = pd.read_csv('test.csv')
#print(data['Profit/Losses'].sum())
# Text
with open('analysis/PyBank.txt', 'w') as txtfile:
    txtfile.write('Financial Analysis')
    txtfile.write("\n-------------------------")
    txtfile.write('\nTotal Months: %d' % total_months)
    txtfile.write('\nNet Profit: %d' %net_total)
    txtfile.write('\nAverage Monthly Change: $%.2f'%average)
    txtfile.write('\nGreatest Increase In Profits: %s ($%d)'%(incease_date,increase_profit))
    txtfile.write('\nGreatest Loss In Profits: %s ($%d)'%(decrease_date,decrease_profit))
       
print('Financial Analysis')
print("-------------------------")
print('Total Months: %d' % total_months)
print('Net Profit: %d' %net_total)
print('Average Monthly Change: $%.2f'%average)
print('Greatest Increase In Profits: %s ($%d)'%(incease_date,increase_profit))
print('Greatest Loss In Profits: %s ($%d)'%(decrease_date,decrease_profit))