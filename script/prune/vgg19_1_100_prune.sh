#!/bin/bash

models=(
    # "vgg8"
    # "vgg11"
    # "vgg13"
    # "vgg16"
    "vgg19"
)

datasets=(
    "cifar100"
)

# ratios=(
#     "0.2"
#     "0.5"
#     "0.8"
# )

methods=(
    "l1"
    # "l2"
    # "random"
)



for model in "${models[@]}"
do
    for dataset in "${datasets}"
    do
        for ratio in $(seq 0.1 0.1 1.0);
        do
            for method in "${methods[@]}"
            do
                path="save/full_model/${model}/${model}_last.pth"
                echo "${model} + ${ratio}"
                python3 -m hard_pruning --path "${path}" --dataset "${dataset}" --prune-method "${method}" --ratio "${ratio}" --global-pruning "True"
            done
        done
    done    
done