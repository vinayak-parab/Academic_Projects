import redis                                            # import the redis package use the the Redis SET command
import pandas as pd                                     # import pandas package to read the CSV file and store as a df

r = redis.Redis(host='127.0.0.1', port=6379, db=0)      # Redis Client connectivity

df = pd.read_csv("Bin_color_List.csv",                  # Read the CSV file and store it in df
                 header=0)

for index,row in df.iterrows():                         # iterate over each index,row to fetch row wise data
    key = row['Material Title']
    val = row['Bin']
    r.set(key, value=val)                               # Execute the Redis SET command to store the data in Redis

# provide the Product and get the Bin color
print("Please either enter the material name to get the color of the bin or enter QUIT to quit from the window")

product = ""
while product != "QUIT":
    product = input("Please provide the material to get the color of the bin: ")
    if product == "QUIT":
        break
    elif product == "":
    	print("Only Non-Blank entries are allowed")
    else:	
    	product = r.get(product)
    	if product == None:
    		print("Please enter a valid material name!")
    	elif product.decode() == "No Bin":
    		print("The entered product does not have any specific colored bin associated with it")
    	else:
    		print("The entered material should go into "+product.decode()+" colored bin")

        




