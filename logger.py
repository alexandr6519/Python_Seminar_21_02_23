import os
from data_create import name_data, surname_data, phone_data, adress_data

file_name = "data.txt"

def print_data():    
    if os.path.exists(file_name):
        print('Вывод данных из файла: ')
        with open(file_name, 'r', encoding="utf-8") as file:
            list_data = file.readlines()
            for element in list_data:
                print(element)
    else:
        print("Файла не существует!!!")

def input_data():
    print('Введите данные для записи в файл: ')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    number_max_lines = int(get_number_max_line())
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{number_max_lines + 1};{name};{surname};{phone};{adress};\n")
     
def filter_data(filter_string):
    if ";" in filter_string:
        list_filter = filter_string.split(";")
    else:
        list_filter = [filter_string] 
    with open(file_name, 'r', encoding = "utf-8") as file:
        list_data = file.readlines()
        is_found = False
        for element in list_data:
            temp_record = element.split(";")
            count = 0
            for record in temp_record:           
                for element_filter in list_filter: 
                    if element_filter.lower() in record.lower() and len(element_filter.lower()) == len(record.lower()):
                        count += 1
      
            if count == len(list_filter):
                print(element)
                is_found = True
    if not is_found:
        print("Таких записей не нашли!")

def update_data(number_line):
    with open(file_name, "r", encoding="utf-8") as file:
        list_data = file.readlines()        
        result_record = list_data[number_line - 1].split(";")  
        
        name = input("Если не хотите менять имя, то введите пустую строку, иначе введите новое значение: ")
        if len(name) > 0:
            result_record[1] = name
             
        surname = input("Если не хотите менять фамилию, то введите пустую строку, иначе введите новое значение: ")
        if len(surname) > 0:
            result_record[2] = surname

        phone = input("Если не хотите менять телефон, то введите пустую строку, иначе введите новое значение: ")
        if len(phone) > 0:
            result_record[3] = phone

        adress = input("Если не хотите менять адрес, то введите пустую строку, иначе введите новое значение: ")
        if len(adress) > 0:
            result_record[4] = adress  

        list_data.pop(number_line - 1)  
        new_record =  (f"{number_line};{result_record[1]};{result_record[2]};{result_record[3]};{result_record[4]};\n")
        list_data.insert(number_line - 1, new_record)

    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(len(list_data)):
            temp_record = list_data[i].split(";")
            file.write(f"{temp_record[0]};{temp_record[1]};{temp_record[2]};{temp_record[3]};{temp_record[4]};\n")

def delete_data(number_line):
    with open(file_name, "r", encoding="utf-8") as file:
        list_data = file.readlines()
        for i in range(len(list_data)):
            if number_line == int(list_data[i].split(";")[0]):
                list_data.pop(i) 
                break
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(len(list_data)):
            temp_record = list_data[i].split(";")
            file.write(f"{temp_record[0]};{temp_record[1]};{temp_record[2]};{temp_record[3]};{temp_record[4]};\n")

def is_number_line(number_line):
    with open(file_name, 'r', encoding="utf-8") as file:
        list_data = file.readlines()
        
        for i in range(len(list_data)):
            temp_record = list_data[i].split(";")
            if int(temp_record[0]) == number_line:
                return True
    return False   
     
def get_number_max_line():
    with open(file_name, 'r', encoding="utf-8") as file:
        list_data = file.readlines()
        max_number = int(list_data[0].split(";")[0])
        for i in range(1, len(list_data)):
            temp_record = list_data[i].split(";")
            if int(temp_record[0]) > max_number:
                max_number = int(temp_record[0])
        return max_number           


