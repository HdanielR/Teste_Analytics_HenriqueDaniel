# clean_data.py
"""
Wrapper to (re)generate data_clean.csv from data_simulated_raw.csv or by running simulation.
"""
import os
import pandas as pd
if os.path.exists("data_simulated_raw.csv"):
    # run a lightweight cleaning similar to earlier script
    from simulate_and_clean import main as run_sim_clean
    # simulate_and_clean.main will regenerate both raw and clean if needed
    run_sim_clean()
else:
    from simulate_and_clean import main as run_sim_clean
    run_sim_clean()
