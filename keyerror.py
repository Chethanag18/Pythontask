a = {"name":"Chethana","age":22,"address":"Banglore"}
try:
    value= a["name"]
except KeyError:
    print("Error in key")
else:
    print("No errors")