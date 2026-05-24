ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = 'World!'
# l = list(ft_tuple)
# l[1] = "Turkey!"
# ft_tuple = tuple(l)
ft_tuple = ("Hello", "Turkey!")
ft_set.discard("tutu!")
ft_set.add("Istanbul!")
ft_dict["Hello"] = "42Istanbul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
