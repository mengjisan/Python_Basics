class Washer():
    def __init__(self):
        self.width = 200

    def __del__(self):
        print('对象已经删除')

haier = Washer()
