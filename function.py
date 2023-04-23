# # 1. Postional Argument:
# def person(name,age):#(name,age(known parameter))
#     print(name,age)

# person("sanjeev",25)#(sanjeev,25 known as arguments)


# 2. keyword Arugument

# def test(name,age):
#     print(name,age)

# test(age=25,name="charan")

# 3. *args Argument(if we known that how many arugments are use in the function we use *arug)

# def test(*args):
#     print(args)
#     print(type(args))
# test("india","beneguluru","delhi")

# 4. keyword Arugment(**keyword)if we known that how many keyword are use in the function we use **kwargs
# def test(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# test(country = "india",city="faridabad")


# # 5 default Argument:

# def test(first_name="ram"):
#     print(first_name)

# test("shyam")