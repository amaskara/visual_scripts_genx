#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
import os
from IPython import embed as IP

# In[30]:


year = 2050


# In[31]:


for root, dirs, files in os.walk("/D/PowerGenome_new/PowerGenome/example_system/test_2/2050/", topdown=False):
 for name in files:
    if name == "Generators_data.csv":
        generator = pd.read_csv(os.path.join(root, name), header='infer', sep=',') 
        technology_list = ['utilitypv_losangeles']
        generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource.isin(technology_list)), 'capex'] = generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource.isin(technology_list)), 'capex'] * 1.085
        generator.loc[(generator.region == 'PJM_NJLand')&(generator.Resource.isin(technology_list)), 'capex'] = generator.loc[(generator.region == 'PJM_NJLand')&(generator.Resource.isin(technology_list)), 'capex'] * 1.085
        generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource.isin(technology_list)), 'Inv_cost_per_MWyr'] = generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource.isin(technology_list)), 'Inv_cost_per_MWyr'] * 1.085
        generator.loc[(generator.region == 'PJM_NJLand')&(generator.Resource.isin(technology_list)), 'Inv_cost_per_MWyr'] = generator.loc[(generator.region == 'PJM_NJLand')&(generator.Resource.isin(technology_list)), 'Inv_cost_per_MWyr'] * 1.085
        ### Apply 10% soalr ITC
        technology_list = ['utilitypv_losangeles']
        generator.loc[generator.Resource.isin(technology_list), 'capex'] = generator.loc[generator.Resource.isin(technology_list), 'capex'] * 0.9
        generator.loc[generator.Resource.isin(technology_list), 'Inv_cost_per_MWyr'] = generator.loc[generator.Resource.isin(technology_list), 'Inv_cost_per_MWyr'] * 0.9
        ### Set hydro min
        generator.loc[generator.Resource == 'conventional_hydroelectric', 'Min_power'] = 0.0
        generator.loc[generator.Resource == 'small_hydroelectric', 'Min_power'] = 0.0
        ### Set offshore wind min
        if year==2030:
            generator.loc[generator.cluster == 'NY_East_offshorewind_49', 'Min_Cap_MW'] = 560
            generator.loc[generator.cluster == 'NY_East_offshorewind_51', 'Min_Cap_MW'] = 1200
            generator.loc[generator.cluster == 'NY_East_offshorewind_52', 'Min_Cap_MW'] = 1770
            generator.loc[generator.cluster == 'NY_East_offshorewind_53', 'Min_Cap_MW'] = 2470
            generator.loc[generator.cluster == 'PJM_Delaware_offshorewind_55', 'Min_Cap_MW'] = 1200
            generator.loc[generator.cluster == 'PJM_Dom_offshorewind_56', 'Min_Cap_MW'] = 1180
            generator.loc[generator.cluster == 'PJM_Dom_offshorewind_57', 'Min_Cap_MW'] = 2670
            generator.loc[generator.cluster == 'PJM_NJCoast_offshorewind_58', 'Min_Cap_MW'] = 2380
            generator.loc[generator.cluster == 'PJM_NJCoast_offshorewind_59', 'Min_Cap_MW'] = 1120

        if year==2040:
            generator.loc[generator.cluster == 'NY_East_offshorewind_49', 'Min_Cap_MW'] = 1050
            generator.loc[generator.cluster == 'NY_East_offshorewind_51', 'Min_Cap_MW'] = 1200
            generator.loc[generator.cluster == 'NY_East_offshorewind_52', 'Min_Cap_MW'] = 1770
            generator.loc[generator.cluster == 'NY_East_offshorewind_53', 'Min_Cap_MW'] = 2470
            generator.loc[generator.cluster == 'NY_East_offshorewind_54', 'Min_Cap_MW'] = 2510    
            generator.loc[generator.cluster == 'PJM_Delaware_offshorewind_55', 'Min_Cap_MW'] = 1835  
            generator.loc[generator.cluster == 'PJM_Dom_offshorewind_56', 'Min_Cap_MW'] = 1180
            generator.loc[generator.cluster == 'PJM_Dom_offshorewind_57', 'Min_Cap_MW'] = 3385
            generator.loc[generator.cluster == 'PJM_NJCoast_offshorewind_58', 'Min_Cap_MW'] = 2380
            generator.loc[generator.cluster == 'PJM_NJCoast_offshorewind_59', 'Min_Cap_MW'] = 1620
            generator.loc[generator.cluster == 'PJM_NJCoast_offshorewind_60', 'Min_Cap_MW'] = 3500

        if year==2050:
            generator.loc[generator.cluster == 'NY_East_offshorewind_49', 'Min_Cap_MW'] = 1050
            generator.loc[generator.cluster == 'NY_East_offshorewind_51', 'Min_Cap_MW'] = 1200
            generator.loc[generator.cluster == 'NY_East_offshorewind_52', 'Min_Cap_MW'] = 1770
            generator.loc[generator.cluster == 'NY_East_offshorewind_53', 'Min_Cap_MW'] = 2470
            generator.loc[generator.cluster == 'NY_East_offshorewind_54', 'Min_Cap_MW'] = 2510
            generator.loc[generator.cluster == 'PJM_Delaware_offshorewind_55', 'Min_Cap_MW'] = 1835
            generator.loc[generator.cluster == 'PJM_Dom_offshorewind_56', 'Min_Cap_MW'] = 1180
            generator.loc[generator.cluster == 'PJM_Dom_offshorewind_57', 'Min_Cap_MW'] = 3385
            generator.loc[generator.cluster == 'PJM_NJCoast_offshorewind_58', 'Min_Cap_MW'] = 2380
            generator.loc[generator.cluster == 'PJM_NJCoast_offshorewind_59', 'Min_Cap_MW'] = 1620
            generator.loc[generator.cluster == 'PJM_NJCoast_offshorewind_60', 'Min_Cap_MW'] = 3500

        ### Set min solar
        generator.loc[generator.cluster == 'NY_East_solarpv_2', 'Min_Cap_MW'] = 4500
        generator.loc[generator.cluster == 'NY_West_solarpv_3', 'Min_Cap_MW'] = 1500
        generator.loc[generator.cluster == 'PJM_COMD_solarpv_4', 'Min_Cap_MW'] = 370  
        generator.loc[generator.cluster == 'PJM_Delaware_solarpv_5', 'Min_Cap_MW'] = 210

        ### Set min storage
        if year==2030:
           generator.loc[(generator.region == 'NY_East')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 2250
           generator.loc[(generator.region == 'NY_West')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 750    
           generator.loc[(generator.region == 'PJM_Dom')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 1440
           generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 395
           generator.loc[(generator.region == 'PJM_NJLand')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 1185
        if year==2040:
           generator.loc[(generator.region == 'NY_East')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 2250
           generator.loc[(generator.region == 'NY_West')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 750    
           generator.loc[(generator.region == 'PJM_Dom')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 2300
           generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 395
           generator.loc[(generator.region == 'PJM_NJLand')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 1185
        if year==2050:
           generator.loc[(generator.region == 'NY_East')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 2250
           generator.loc[(generator.region == 'NY_West')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 750     
           generator.loc[(generator.region == 'PJM_Dom')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 2300
           generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 395
           generator.loc[(generator.region == 'PJM_NJLand')&(generator.Resource == 'battery'), 'Min_Cap_MW'] = 1185

        ### Set min nuclear
        if year==2030:    
           generator.loc[(generator.region == 'NY_West')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'New_Build'] = -1     
           generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'New_Build'] = -1
           generator.loc[(generator.region == 'PJM_COMD')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'Min_Cap_MW'] = 2.969
        if year==2040:    
           generator.loc[(generator.region == 'NY_West')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'New_Build'] = 0     
           generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'New_Build'] = 0
           generator.loc[(generator.region == 'PJM_COMD')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'Min_Cap_MW'] = -1
        if year==2050:  
           generator.loc[(generator.region == 'NY_West')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'New_Build'] = 0  
           generator.loc[(generator.region == 'PJM_NJCoast')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'New_Build'] = 0
           generator.loc[(generator.region == 'PJM_COMD')&(generator.Resource == 'nuclear')&(generator.capex == 0), 'Min_Cap_MW'] = -1

        ### Set negative OM cost to 0
        generator.loc[generator['Fixed_OM_cost_per_MWyr'] < 0] = 0

        ### Replace negative heat rate with average of the technology
        generator.loc[(generator.Resource == 'natural_gas_fired_combustion_turbine')&(generator.Heat_rate_MMBTU_per_MWh < 0), 'Heat_rate_MMBTU_per_MWh'] = 16.84
        generator.loc[(generator.Resource == 'natural_gas_fired_combined_cycle')&(generator.Heat_rate_MMBTU_per_MWh < 0), 'Heat_rate_MMBTU_per_MWh'] = 8.7

        ### Save the data as csv
        generator.to_csv(os.path.join(root, name),encoding='utf-8',index=False)
        print(os.path.join(root, name))


# In[ ]:





# In[ ]:




