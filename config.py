import os

class Config:
    def __init__(self):
        
        #data
        self.datanames = 'RSNA'
        self.data_folder = '../../autodl-tmp/FirstRotate/archive/masked_1K_fold/fold_1/'
        self.do_aug = True
        self.num_works = 4
        
        # train
        self.batch_size = 16
        self.lr = 1e-3
        self.epochs = 200
        self.use_multiple_gpu=False
        self.device_ids=[0,1] if self.use_multiple_gpu else [0]
        self.pre_epoch = 0
        self.pre_iter = 0
        self.accuracy_threshold = 5
        self.do_multiscale=False
        self.mode='train' if self.batch_size>1 else 'test'
        self.save_folder='../../autodl-tmp/DAA/models/{}'.format(self.datanames)
        
        #net
        self.backbone = 'resnet18' #['c3ae','resnet18']
        self.input_size = 512 #96
        
        self.feat_dim=32
        self.min_age = 1
        self.max_age = 228
        self.num_classes = self.max_age - self.min_age + 1
        self.da_type = 'binary' #['binary','decimal', 'image_template']
        self.image_template_path=''

        self.pretrained_fn=''
        self.pretrained_ex_params=[]
       
