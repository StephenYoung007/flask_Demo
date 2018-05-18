import os
import time

backup_time = time.strftime("%m%d%H%M%S", time.localtime())

def run():
    source_path = 'G:\\'
    dic = os.listdir(source_path)
    # print(dic)
    # print(len(dic), type(dic))
    i = 0
    gcode_list = []
    while i < len(dic):
        if dic[i].find('.') != -1:
            if dic[i].split('.')[1] == 'gcode':
                # print(dic[i])
                gcode_list.append(dic[i])
        i = i + 1

    m = len(gcode_list)
    if m != 0:
        # print('gcode_list', gcode_list)

        j = 0
        origen_path = 'F:\\3D打印备份\\' + backup_time + '\\'
        os.mkdir(origen_path)
        for code in gcode_list:
            code_path = source_path + code
            # print('code_path', code_path)
            with open(code_path, 'r', encoding='utf-8') as f:
                content = f.read()
                save_path = origen_path + code
                # print(save_path)
                with open(save_path, 'w',encoding='utf-8') as new:
                    new.write(content)
            os.remove(code_path)
            j = j + 1
            print('file {} copied'.format(code_path))

        # print(backup_time,j)

        # push test





if __name__ == '__main__':
    run()