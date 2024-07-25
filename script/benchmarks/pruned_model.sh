#!/bin/bash

models=(
    "vgg8"
    "vgg11"
    "vgg13"
    "vgg16"
    "vgg19"
)

methods=(
    "l1"
    "l2"
    "random"
)

sparcities=(
    "0.2"
    "0.5"
    "0.8"
)

for model in "${models[@]}"
do
    for method in "${methods[@]}"
    do
        for sparcity in "${sparcities[@]}"
        do
            path="save/pruned/${model}/${model}_cifar100_prune_${method}_${sparcity}_none.pth"
            python3 -m cifar100_benchmark --path "${path}" --save 1 --iter 1
        done
    done
done