import os
def get_file_path(root_path, file_list, dir_list):
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        # 获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            # 递归获取所有文件和目录的路径
            get_file_path(dir_file_path, file_list, dir_list)
        else:
            file_list.append(dir_file_path)


if __name__ == "__main__":
    # 根目录路径
    # root_path = r"F:\zhangxiaojing\2019\交付中心\声纹性能测试\Lower20dB_Denoise_cutoff\2.DW_Sel12_NoVCTPUtt5_No1toNo4"
    # root_path = r"F:\zhangxiaojing\2019\交付中心\声纹性能测试\Lower20dB_Denoise_cutoff\2.DW_Sel12_NoVCTPUtt5_No1toNo8_noTP"
    root_path = r"F:\zhangxiaojing\2019\交付中心\声纹性能测试\Lower20dB_Denoise_cutoff\2.DW_Sel12_NoVCTPUtt5_No1toNo10_noTP"
    # root_path = r"F:\zhangxiaojing\2019\交付中心\声纹性能测试\Lower20dB_Denoise_cutoff\2.DW_Sel12_NoVCTPUtt5_No1\1WeiXin"
    # 用来存放所有的文件路径
    file_list = []
    # 用来存放所有的目录路径
    dir_list = []
    get_file_path(root_path, file_list, dir_list)

    with open('list_10.txt','w',encoding='utf-8') as f:
        count = 10
        for i in file_list:
            temp = ''.join(i)
            f.write(temp+ ',' + str(count) +'\n')
            count = count + 20
            if count > 300:
                count = 10




