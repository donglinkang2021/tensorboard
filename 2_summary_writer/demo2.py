from torch.utils.tensorboard import SummaryWriter

# create a summary writer with automatically generated folder name.
# writer = SummaryWriter()
# folder location: runs/May04_22-14-54_s-MacBook-Pro.local/

# create a summary writer using the specified folder name.
# writer = SummaryWriter("my_experiment")
# folder location: my_experiment

# create a summary writer with comment appended.
# writer = SummaryWriter(comment="LR_0.1_BATCH_16")
# folder location: runs/May04_22-14-54_s-MacBook-Pro.localLR_0.1_BATCH_16/
