import csv
import os

f_name = input ("enter your first name: ")
l_name = input ("enter your last name: ")
job_title = input ("enter your job title: ")
company_name = input ("enter your company name: ")

details_dict = {"First name":f_name, "Last name":l_name, "Job title":job_title, "Company name":company_name}
print(details_dict)

headers = ["First name", "Last name", "Job title", "Company name"]

if not os.path.exists('./my_detail.csv'):
    with open('./my_detail.csv','w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerow(details_dict)
else:
    with open('./my_detail.csv','a') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writerow(details_dict)
    
     

#with open('./my_detail.csv','a') as f:
  #  writer = csv.DictWriter(f, details_dict.keys())
   # writer.writeheader()
  #  writer.writerow(details_dict)
  
#with open('./my_detail.csv','r') as f :
 #   reader = csv.reader(f)
   # for row in reader:
      #  print(row)