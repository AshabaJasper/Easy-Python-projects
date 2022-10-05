#creating a substring by extracting elements from another string
#[start:stop:step]

name="first_name secona_name third_name"

first_name=name[0:6]
print(first_name)
middle_name=name[7:14]
print(middle_name)
weird_name=name[0:21:2]
print(weird_name)
last_name=name[14:]
print(last_name)
reversed_name=name[::-1]
print(reversed_name)

#slicing(::)
name2="first_name second_name"

slice=slice(7,-4,)
print(name2[slice])
