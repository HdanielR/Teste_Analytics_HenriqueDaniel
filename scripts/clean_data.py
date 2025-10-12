# clean_data.py

import os
import pandas as pd
if os.path.exists("data_simulated_raw.csv"):
   
    from simulate_and_clean import main as run_sim_clean

    run_sim_clean()
else:
    from simulate_and_clean import main as run_sim_clean
    run_sim_clean()
