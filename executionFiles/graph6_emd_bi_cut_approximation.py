import os
import pyphi
import numpy as np
import json

f = open(os.path.dirname(__file__) + "/../graphs/graph_6.json")
data = json.load(f)

pyphi.config.load_file(
    os.path.dirname(__file__) + "/../config/pyphi_config_emd_bi_cut_approximation.yml"
)

network = pyphi.Network(data['tpm'], cm=data['cm'], node_labels=data['labels'])
state = data['state']
node_indices = (0, 1, 2, 3 ,4, 5)
subsystem = pyphi.Subsystem(network, state, node_indices)
f.close()
sia = pyphi.compute.sia(subsystem)

print("MIP: \n", sia.cut)
print("Phi: \n Φ = ", sia.phi)
print("Tiempo: \n", sia.time, "s")