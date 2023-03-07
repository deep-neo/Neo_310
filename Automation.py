import os; import re

with open('C:\\Users\\INFINITY-HP\\PycharmProjects\\pythonProject5\\ipad\\red.badge.txt', 'r') as input_file:

    with open('C:\\Users\\INFINITY-HP\\PycharmProjects\\pythonProject5\\ipad\\Output.txt', 'w') as file_1:
        file_1.write('IP Addresses as below >>>\n\n')

        with open('C:\\Users\\INFINITY-HP\\PycharmProjects\\pythonProject5\\ipad\\black.pearl.txt', 'w') as file_2:
            file_2.write('Test Case as below >>>\n\n')

            with open('C:\\Users\\INFINITY-HP\\PycharmProjects\\pythonProject5\\ipad\\Input.txt', 'w') as file_3:
                file_3.write('Phone numbers as below >>>\n\n')

                data = input_file.read()

                pattern_1 = '.*([0-9]{3}\.[0-9]{3}\.[0-9]{1,3}\.[0-9]{1,3}).*'
                pattern_2 = '.*(spbm.*\.test).*'
                pattern_3 = '.*([0-9]{10}\s).*'

                match_obj_1 = re.findall(pattern_1, data)
                match_obj_2 = re.findall(pattern_2, data)
                match_obj_3 = re.findall(pattern_3, data)

                if match_obj_1:
                    file_1.write('\n'.join(match_obj_1))

                if match_obj_2:
                    file_2.write('\n'.join(match_obj_2))

                if match_obj_3:
                    file_3.write('\n'.join(match_obj_3))


os.startfile('C:\\Users\\INFINITY-HP\\PycharmProjects\\pythonProject5\\ipad\\Output.txt')
os.startfile('C:\\Users\\INFINITY-HP\\PycharmProjects\\pythonProject5\\ipad\\black.pearl.txt')
os.startfile('C:\\Users\\INFINITY-HP\\PycharmProjects\\pythonProject5\\ipad\\Input.txt')