import matplotlib.pyplot as plt
import numpy as np

def plot_logistic(df, probs):
    fig,  ax= plt.subplots()
    ax.set_xlim(-0.25, 0.25)
    ax.set_xticks(np.arange(-0.25, 0.251, step=0.05))
    ax.set_yticks(np.arange(0, 1.01, step=0.1))
    ax.set_ylim(0, 1)
    ax.axvline(0, linestyle= ":")
    cond= df["status"] == "below"
    ax.plot(df.loc[cond, "difshare"], probs["below"][:,1], label="logistic fit")
    cond= df["status"] =="above"
    ax.plot(df.loc[cond, "difshare"], probs["above"][:,1], label="logistic fit")
    ax.set_xlabel("vote share of victory, election t")
    ax.set_ylabel("probability of winning election t+1")
    ax.legend()

def plot_bandwidth(bandwidth, result_error):
    fig, ax= plt.subplots()
    ax.plot(bandwidth, result_error)
    ax.set_xlabel("bandwidth")
    ax.set_ylabel("mean squared error")