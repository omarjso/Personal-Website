import os


def extract(prb_web, prb_module):
    prb_page = open(prb_web, "r")
    module = open(prb_module, "r")
    contents = prb_page.read()
    module_unit = module.read()
    prb_page.close()
    module.close()
    return [contents, module_unit]


def modify_unit(module_unit, filename, replaced_after, replaced_before):
    end_num = filename.index(".")
    prb_num = filename[2: end_num]
    for i in range(0, len(module_unit) - len(replaced_after) + 1):
        finished = False
        if module_unit[i: i + len(replaced_after)] == replaced_after:
            for j in range(i + len(replaced_after), len(module_unit)):
                if module_unit[j] == replaced_before:
                    module_unit = module_unit.replace(module_unit[i + len(replaced_after): j], prb_num)
                    finished = True
                    break
        if finished:
            break
    return [int(prb_num), module_unit]


def delete_old(current):
    counter = 0
    for i in range(0, len(current) - 3): 
        if current[i: i + 4] == "<tr>":
            if counter == 1:
                start_del = i
                break
            counter += 1
    for j in range(5, len(current)):
        if current[len(current) - j: len(current) - j + 5] == "</tr>":
            end_del = len(current) - j + 5
            break
    current = current.replace(current[start_del: end_del], "")
    return [current, start_del]


def sort_modules(list_of_modules):
    dict_of_modules = {}
    for i in range(0, len(list_of_modules)):
        dict_of_modules[list_of_modules[i][0]] = list_of_modules[i][1]
    final_content = ""
    for i in range(1, 651):
        if i in dict_of_modules:
            final_content += dict_of_modules[i]
    return final_content


extraction = extract("problems.html", "prb_module.html")
template = delete_old(extraction[0])

empty_template = template[0]
index_of_addition = template[1]

list_of_modules = []

for filename in os.listdir("ProjectEulerHTML/"):
    if "PE" in filename:
        list_of_modules.append(modify_unit(extraction[1], filename, "problem=", '"'))

file_addition = sort_modules(list_of_modules)

result = empty_template[:index_of_addition] + file_addition + empty_template[index_of_addition:]

problems_webpage = open("problems.html", "w")
problems_webpage.write(result)

