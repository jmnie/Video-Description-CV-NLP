import argparse
import os
import mxnet as mx

class Options():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Video Caption Project")
        #subparsers = self.parser.add_subparsers(title="subcommands", dest="subcommand")

        self.parser.add_argument('--train_folder', type=str,default='/HDD/dl_proj/msr_vtt/TrainValVideo')
        self.parser.add_argument('--val_folder', type=str, default='/HDD/dl_proj/msr_vtt/TrainValVideo')
        self.parser.add_argument('--test_folder', type=str, default='/HDD/dl_proj/msr_vtt/TestVideo')
        self.parser.add_argument('--glove_file', type=str,default='/HDD/dl_proj/glove/glove.6B.50d.txt')
        self.parser.add_argument('--train_dict', type=str,default='./annotation/train_50d.json')
        self.parser.add_argument('--test_dict', type=str,default='./annotation/test_50d.json')
        self.parser.add_argument('--val_dict', type=str, default='./annotation/val_50d.json')
        self.parser.add_argument('--frames', type=int, default=30)
        self.parser.add_argument('--caption_length', type=int, default=50)
        self.parser.add_argument('--cuda', type=int, default=1)
        self.parser.add_argument('--batch_size', type=int, default=16)
        self.parser.add_argument('--lr', type=float, default=1e-3, help='set the learning rate')
        self.parser.add_argument('--epochs', type=int, default=30, help='set the training epochs')

        #self.parser.add_argumen()

    def parse(self):
        return self.parser.parse_args()
    

class args_(object):
    def __init__(self):
        self.train_folder = '/HDD/dl_proj/msr_vtt/TrainValVideo'
        self.test_folder = '/HDD/dl_proj/msr_vtt/TestVideo'
        self.val_folder = '/HDD/dl_proj/msr_vtt/TrainValVideo'
        self.glove_file = '/HDD/dl_proj/glove/glove.6B.50d.txt'
        self.train_dict = './annotation/train_50d.json'
        self.test_dict = './annotation/test_50d.json'
        self.val_dict = './annotation/val_50d.json'
        self.img_size = 224
        self.frames = 50
        self.caption_length = 50
        self.cuda = 0 if len(mx.test_utils.list_gpus())== 0 else 1
        self.batch_size = 16
        self.lr = 1e-4
        self.epochs = 10
        self.load_pretrain = 0
        self.save_model = True
        self.model_path = './saved_model'
        self.log_path = './logs'
        self.log_interval = 2000
        self.model_file = './saved_model/Epoch_9_iters_800_Tue_Apr_23_15:10:23_2019_.params'
        self.mode = 0

    def set_data_path(self,train_folder,test_folder,val_folder):
        self.train_folder = train_folder
        self.test_folder = test_folder
        self.val_folder = val_folder

    def set_glove_file(self,glove_file):
        self.glove_file = glove_file

# test = Options().parse()
# # print(test.add_argument('--batch_size',32))
# # print(test.parse_args().batch_size)
# print(test.batch_size)