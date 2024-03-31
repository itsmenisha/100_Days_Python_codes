def format_name(f_name, l_name):
    if f_name == " " or l_name == " ":
        return "You didnt provide valid inputs"
    return ((f_name+l_name).title())


f_name = (input("enter your first name : ")).lower()
l_name = (input("enter your last name : ")).lower()

print(format_name(f_name, l_name))
