
import os
import sys

class cfg:
    def __init__(self, pwd):
        self.pwd = pwd
        self.info = "anomaly_detection"
        self.img_dim = (224, 3)
        self.args = {}
        
    #def set_paths(self):
        self.args['main'] = self.pwd
        self.args['dataset'] = self.args['main'] + 'Dataset_cracks/'
        self.args['images'] = self.args['dataset'] + 'images/'
        self.args['image'] = self.args['dataset'] + 'image/'
        self.args['video'] = self.args['dataset'] + 'video/'
        self.args['grayscale'] = self.args['dataset'] + 'grayscale/'
        self.args['masks'] = self.args['dataset'] + 'masks/'
        self.args['output'] = self.args['main'] + 'output/'
        self.args['output_images'] = self.args['output'] + 'images/'
        self.args['output_videos'] = self.args['output'] + 'videos/'
        self.args['isimage'] = False
        self.args['isvideo'] = True
        self.args['iscamera'] = False
