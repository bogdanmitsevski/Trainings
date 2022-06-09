#Dictionary output
myDictionary = {
    "brand":"Apple",
    "model":"iPhone X",
    "color":"Black",
    "memory":"256Gb",
    "price":"$300"
}
print(myDictionary);

#dictionary length
myDictionary1 = {
    "brand":"Apple",
    "model":"iPhone X",
    "color":"Black",
    "memory":"256Gb",
    "price":"$300"
}
print(len(myDictionary1));

#dictionary type
myDictionary2 = {
    "brand":"Apple",
    "model":"iPhone X",
    "color":"Black",
    "memory":"256Gb",
    "price":"$300"
}
print(type(myDictionary1));

#dictionary item output
myDictionary3 = {
    "brand":"Apple",
    "model":"iPhone X",
    "color":"Black",
    "memory":"256Gb",
    "price":"$300"
}

print(myDictionary3["color"]);

#keys, values output
myDictionary4 = {
    "brand":"Apple",
    "model":"iPhone X",
    "color":"Black",
    "memory":"256Gb",
    "price":"$300"
}
print(myDictionary4.keys());
print(myDictionary4.values());

#add new item to dictionary
myDictionary5 = {
    "brand":"Apple",
    "model":"iPhone X",
    "color":"Black",
    "memory":"256Gb",
    "price":"$300"
}

myDictionary5["oldprice"] = "$1000";
print(myDictionary5);