
from wildgaussians import train

if __name__ == "__main__":
    train.train_command()


#直接运行train.py存在顶层模块的相对导入问题，所以只能新建一个main.py来相对导入原本的顶层模块train.py
#python main.py --data /data/wangzhaohui/github/dataset/trevi_fountain/dense