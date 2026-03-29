from matplotlib import pyplot as plt
import powerlaw
from tqdm import tqdm

# Set seed for reproducibility
import numpy as np
np.random.seed(0)

# Note that due to the nature of the error, the error
# becomes smaller with increasing number of samples in the data.
# Therefore, we choose a relatively small dataset size
datasetSize = 20
number_of_trials = [1e1,1e2,1e3,1e4,1e5]
xmin=1
alpha=1.5
pl = powerlaw.Power_Law(xmin=xmin, alpha=alpha, use_old_cdf=True)
avg_old_d = []
avg_new_d = []
for trials in number_of_trials:
    print(f"Running {trials} trials")
    old_d = []
    new_d = []
    for _ in tqdm(range(int(trials))):
        data = pl.generate_random(datasetSize)

        old = powerlaw.Power_Law(data=data, xmin=xmin, use_old_cdf=True)
        new = powerlaw.Power_Law(data=data, xmin=xmin, use_old_cdf=False)

        old_d.append(old.D)
        new_d.append(new.D)

    avg_old_d.append(sum(old_d)/trials)
    avg_new_d.append(sum(new_d)/trials)

print("Done")
plt.plot(number_of_trials, avg_old_d, label="Old CDF")
plt.plot(number_of_trials, avg_new_d, label="new CDF")
plt.legend()
plt.xscale("log")
plt.xlabel("Nr trials")
plt.ylabel("Average KS distance")
plt.show()