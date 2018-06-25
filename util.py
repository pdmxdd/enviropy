import os


def enviropy_in_gitignore():
    if os.path.isfile("{}/.gitignore".format(os.getcwd())):
        data = []
        with open("{}/.gitignore".format(os.getcwd())) as readfile:
            data = readfile.read()
        if ".enviropy" in data:
            # print(".enviropy found in .gitignore!")
            return True
        else:
            # print(".enviropy not found in .gitignore!")
            return False
    else:
        # print(".gitignore doesn't exist!")
        return False

def delete_enviropy_from_gitignore():
    if os.path.isfile("{}/.gitignore".format(os.getcwd())):
        data = []
        with open("{}/.gitignore".format(os.getcwd())) as readfile:
            data = readfile.readlines()
        remove_rows = []
        row_counter = 0
        for row in data:
            if ".enviropy" in row:
                remove_rows.append(row_counter)
            row_counter += 1
        with open("{}/.gitignore".format(os.getcwd()), 'w') as overwritefile:
            row_counter = 0
            for row in data:
                if row_counter not in remove_rows:
                    overwritefile.write(row)
                row_counter += 1

def update_gitignore():
    if not enviropy_in_gitignore():
        if not os.path.isfile("{}/.gitignore".format(os.getcwd())):
            with open("{}/.gitignore".format(os.getcwd()), "w") as writefile:
                writefile.write(".enviropy\n")
        else:
            with open("{}/.gitignore".format(os.getcwd()), "a") as appendfile:
                appendfile.write(".enviropy\n")

def add_enviropy(env_vars):
    update_gitignore()
    if not os.path.isfile("{}/.enviropy".format(os.getcwd())):
        with open("{}/.enviropy".format(os.getcwd()), "w") as writefile:
            for k, v in env_vars.items():
                writefile.write("{}={}\n".format(k, v))
    else:
        with open("{}/.enviropy".format(os.getcwd()), "a") as appendfile:
            for k, v in env_vars.items():
                appendfile.write("{}={}\n".format(k, v))

def get_enviropy():
    data = []
    enviropy = {}
    if os.path.isfile("{}/.enviropy".format(os.getcwd())):
        with open("{}/.enviropy".format(os.getcwd()), "r") as readfile:
            for line in readfile:
                data.append(line[0:-1].split("="))
        for row in data:
            enviropy[row[0]] = row[1]

    return enviropy

def delete_enviropy():
    if os.path.isfile("{}/.enviropy".format(os.getcwd())):
        os.remove("{}/.enviropy".format(os.getcwd()))
        delete_enviropy_from_gitignore()
