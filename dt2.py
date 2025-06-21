# #tuples

# days=("sun",["mon"],"tue",(1,2,3)) #defining a tuple

# print(f"size of the tuple is {len(days[3])}") #size of the tuple is 3

# # days[1]="fri" -->accessing elements from tuple

# # print(type(days)) #checking type

# # print(len(days)) #to find the size of the tuple

# # print(days[1][0]) #accessing nested elements in tuple

# # 9845841211002--->harish,suresh

# #sets

# sets={1,2,34,5,5,2,1} #normal set
# print(type(sets))
# print(sets)
# sets.add("hi") # add() method is used to add the element into the set
# print(sets)
# sets.remove(2) #remove() method is used to remove the element from the set
# print(sets)
# #frozenset

# #it is also a collection of unordered elements , but here we can't add/remove elements into the set

# sets1=frozenset([1,3,5,7,8,8]) #here iam defining a frozenset

# # sets1.add(4) # trying to add value 4 into the frozenset

# sets1.remove(5) #trying to remove the value 5 from the frozenset

# print(type(sets1))

realme_info={"name":"realme",
             "model":"5c",
             "price":25000,
             "ram":"8gb",
             "colors_available":["black","green","red","white"],
             "camera":"50mp"
             }

person_info={"name":"akshay",
             "age":25,
             "gender":"male",
             "height":5.7,
             "address":{"d.no":"8/5/258",
                        "streetname":"dollars street",
                        "landmark":"balaji temple",
                        "district":"krishna",
                        "state":"A.p",
                        "pincode":521121
                        },
            "is_he_married":False,
            "skills":["html","css","js","python"]
             }

person_info["height"]=5.6 #updating keys in dictionary

person_info["fav_food"]="biryani" #adding new property into the dictionary


# to store the properties of a particular thing
#collection of key-value pairs
#collection of multiple properties

# print(type(realme_info))

print(person_info)
