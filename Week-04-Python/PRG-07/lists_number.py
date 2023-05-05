#Exercise-02
num_list = [9,80,16,67,35]
#l = len(num_list)
#print(l)
sum_list = []
for i in range(len(num_list)):
    #print(i)
    if  i == (len(num_list) - 1):
        num_sum = num_list[i] + num_list[0]
        sum_list.append(num_sum)
    else:
         num_sum = num_list[i] + num_list[i+1]
         #print(num_sum)
         sum_list.append(num_sum)
print(sum_list)