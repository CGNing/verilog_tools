#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

str_temp = "";

# input
str_input = "";

str_input = raw_input("请输入模块声明：");

while str_input[-1] != ';':
    str_temp = raw_input();
    str_input = str_input + "\n" + str_temp;

# module name
str_module_name = "";

str_module_name = re.findall(r"(?<=module)(.*?)[(]", str_input)[0];
str_module_name = str_module_name.strip(" ");

# interface string


str_interface = re.findall(r"[(][\n]*([\s\S]*?)[\n]*[)]", str_input)[0];

# interface list
list_interface = [];
list_wrap = [];
list_wire = [];

list_interface = str_interface.split(",");

# interface list name
for index,value in enumerate(list_interface):
    # '\n' char
    temp = re.findall(r"[\n]([\n]*).*", value);
    if (len(temp) != 0):
        list_wrap.append(temp[0]);
    else:
        list_wrap.append("");

    #"[]" wire width
    temp = re.findall(r"\[(.*?)\]", value);
    if (len(temp) != 0):
        list_wire.append(temp[0]);
    else:
        list_wire.append("");

    list_interface[index] = re.findall(r"[\s]*(\S*?)$", value)[0];

# print
int_max_len=0;

for value in list_interface:
    if (len(value) > int_max_len):
        int_max_len = len(value);

print ("实例化结果：");
str_out = str_module_name + " " + str_module_name + " (" + "\n";
for index,value in enumerate(list_interface):
    str_temp = list_wrap[index] + "\t." + value.ljust(int_max_len) + "\t(" + value + ")," + "\n";
    str_temp = str_temp.expandtabs(4);
    str_out = str_out + str_temp;
str_out = str_out[:-2] + "\n" + ");";

print (str_out);
