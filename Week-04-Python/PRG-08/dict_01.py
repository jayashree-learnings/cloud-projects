dict_details = {"First name":"casper", "Last name" : "Velzen", "Job title" :"Lead learning coach", "company":"Techgrounds"}

# first method using items()
for k,v in dict_details.items():
    print (k, "---" ,v)


# second method without using items
for k in dict_details:
    print(k,"----" ,dict_details[k])