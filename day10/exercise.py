def getName_Formatted(fname, lname):
    if fname == "" or lname == "":
        return "Please provide valid names"
    formatted_name = fname.title() + " " + lname.title()
    return formatted_name

output = getName_Formatted("durgesh", "tambe")
print(output)
