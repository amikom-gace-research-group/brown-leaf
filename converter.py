import torch
from models import model_dict

import os

path = 'save/models/vgg19/vgg19_cifar100_lr_0.05_decay_0.0005_trial_base/vgg19_last_state_dict.pth'

def get_teacher_name(model_path):
    """parse teacher name"""
    model_segments = model_path.split('/')[-1].split('_')
    
    if model_segments[-1][:-4] == 'pruned':
        return model_segments[0], model_segments[1],model_segments[-3], model_segments[-2],model_segments[-1][:-4]
    elif model_segments[0] == 'wrn':
        return model_segments[0] + '_' + model_segments[1] + '_' + model_segments[2], model_segments[-1]
    else:
        return model_segments[0], model_segments[-1][:-4]

model_name = get_teacher_name(path)
model = model_dict[model_name[0]](num_classes=100)
model.load_state_dict(torch.load(path)['model'])

save_dirs = f'save/full_model/{model_name[0]}/'

os.makedirs(save_dirs, exist_ok=True)

state = {
    'model' : model
}

torch.save(state, f'{save_dirs}/{model_name[0]}_last.pth')