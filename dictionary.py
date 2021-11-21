
'''
sehirler= ["istanbul","sakarya","kocaeli"]
plakalar = [34,41,54]

x = plakalar[sehirler.index("kocaeli")]
print(x) '''


plakalar = {"istanbul" : 34 , "sakarya" : 54 , "kocaeli" : 41}
print(plakalar["istanbul"])

users = {"abdulkadir" : 
                    {"age" : 18,
                    "roles" : ['admin'],
                    "surname" : "tastemel" ,
                    "phone" : "0555 555 55 55",
                    "email" : "tastemelapo@gmail.com"
        } ,

        "rahman" : 
        {
                    "age" : 18,
                    "roles" : ['admin','users'],
                    "surname" : "tastemel" ,
                    "phone" : "0555 555 55 55",
                    "email" : "tastemelapo@gmail.com"   
        }


}

print(users["abdulkadir"]["surname"])
print(users["abdulkadir"]["age"])
print(users["abdulkadir"]["phone"])
print(users["abdulkadir"]["email"])
print(users["rahman"]["roles"][0])