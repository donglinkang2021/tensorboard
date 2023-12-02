from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("add_scalar")
x = range(100)
for i in x:
    writer.add_scalar('scalar', i * 2, i)
writer.close()