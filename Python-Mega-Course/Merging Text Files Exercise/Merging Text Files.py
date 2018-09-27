import glob2
from datetime import datetime

filenames = glob2.glob('*.txt')
print(filenames)
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + '.txt','w') as target_file:
    for filename in filenames:
        with(open(filename)) as f:
            target_file.write(f.read() + '\n')
