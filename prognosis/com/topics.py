# -*- coding: utf-8 -*-
"""
Created on Fri May 20 16:08:29 2022

@author: oriol
"""
import pandas as pd
topic_tickers = {
    'national_accounts':
        ['RGDP%s', 'RPRC%s', 'RPUC%s', 'RGFCF%s', 'REXP%s','RIMP%s'],
    'national_accounts_nominal':
        ['GDP%s', 'PRC%s', 'PUC%s', 'GFCF%s', 'EXP%s','IMP%s'],
    'prices': ['CPI%s', 'PPI%s'],
    'government': ['GSPE%s', 'GREV%s', 'GBAL%s', 'GDEBT%s'],
    'monthly_trade': ['EXPMON%s', 'IMPMON%s'],
    'yield_curve': ['M3YD%s', 'Y10YD%s'],
    'retail_sales': ['RETA%s'],
    'ip': ['IP%s'],
    'energy':
        ['OILPROD%s', 'OILDEM%s', 'GASODEM%s', 'GASOPROD%s', 'GASDEM%s',
         'GASPROD%s'],
}


topic_df = pd.DataFrame([
 ('GDP', 'Gross domestic product'),
 ('PRC', 'Private consumption'),
 ('PUC', 'Public consumption'),
 ('CON', 'Total consumption'),
 ('GCF', 'Gross capital formation'),
 ('GFCF', 'Gross fixed capital formation'),
 ('CI', 'Change in inventories'),
 ('CBAL', 'Commercial balance (goods + services)'),
 ('EXP', 'Exports of goods and services'),
 ('IMP', 'Imports of goods and services'),
 ('PI', 'Personal income'),
 ('RGDP', 'Real gross domestic product'),
 ('RPRC', 'Real private consumption'),
 ('RPUC', 'Real public consumption'),
 ('RCON', 'Real total consumption'),
 ('RGCF', 'Real gross capital formation'),
 ('RGFCF', 'Real gross fixed capital formation'),
 ('RCI', 'Real change in inventories'),
 ('REXP', 'Real exports of goods and services'),
 ('RIMP', 'Real imports of goods and services'),
 ('GDPPC', 'GDP per capita'),
 ('RGDPPC', 'Real GDP per capita'),
 ('GDPD', 'GDP (current US dollars)'),
 ('GDPDEF', 'GDP deflator'),
 ('CPI', 'Consumer price index'),
 ('CORE', 'Core consumer price index'),
 ('PPI', 'Producer price index'),
 ('URATE', 'Unemployment'),
 ('JVR', 'Job vacancy rate'),
 ('JQR', 'Job quits rate'),
 ('JLR', 'Job layoffs rate'),
 ('JHR', 'Job hires rate'),
 ('WAGE', 'Wages/Earnings'),
 ('WAGEMAN', 'Hourly wage manufacturing'),
 ('EMP', 'Total employment'),
 ('ACPOP', 'Active population'),
 ('PAY', 'Total payroll'),
 ('EMRATIO', 'Employment to working age population'),
 ('PART', 'Participation rate'),
 ('CLAIMS', 'Weekly unemployment insurance claims'),
 ('RETA', 'Retail trade'),
 ('IP', 'Industrial production'),
 ('CP', 'Construction production'),
 ('INVER', 'Investment rate'),
 ('SENT', 'Sentiment index'),
 ('CONF', 'Consumer confidence index'),
 ('UTIL', 'Utilization rate'),
 ('DWPE', 'Dwelling permits'),
 ('NFCI', 'Non-financial corporations investment rate'),
 ('CAR', 'Passenger car sales'),
 ('ELE', 'Production electricity'),
 ('ARIV', 'Tourist arrivals'),
 ('OIL', 'Oil production'),
 ('MANU', 'Manufacturing production'),
 ('CLI', 'OECD CLI'),
 ('TB', 'Trade balance'),
 ('NY', 'Net income from abroad (Primary Income)'),
 ('NCT', 'Net current transfers (Secondary Income)'),
 ('CA', 'Current account balance'),
 ('KA', 'Capital account'),
 ('CKA', 'Net foreign investment'),
 ('IIPA', 'International investment position: Assets'),
 ('IIPL', 'International investment position: Liabilities'),
 ('NIIP', 'Net international investment position'),
 ('EXPMON', 'Monthly exports'),
 ('IMPMON', 'Monthly imports'),
 ('GBAL', 'Government balance'),
 ('GSPE', 'General government total expenditure'),
 ('GREV', 'General government total revenue'),
 ('GDEBT', 'Government debt'),
 ('GDEBTN', 'Government net debt'),
 ('POP', 'Population'),
 ('HHS', 'Household saving'),
 ('HHDIR', 'Household debt to income ratio'),
 ('HOU', 'House price'),
 ('TFRT', 'Fertility rate'),
 ('LE00', 'Life expectancy at birth'),
 ('CRED', 'Domestic credit'),
 ('NFCLOAN', 'Lending to non-financial corporations'),
 ('PRIDEBT', 'Private debt'),
 ('NPL', 'Non performing loans'),
 ('MB', 'Monetary base'),
 ('M3', 'Money supply'),
 ('Y10YD', 'Long term yield'),
 ('M3YD', '3 month yield'),
 ('IBD1', 'Interbank lending overnight rate'),
 ('POLIR', 'Policy rate - short term'),
 ('XUSD', 'Exchange rate v dollar'),
 ('SEI', 'Stock exchange index'),
 ('REER', 'Real effective exchange rate'),
 ('EQYCAP', 'Market capitalization'),
 ('OILPROD', 'Oil production'),
 ('OILDEM', 'Oil demand'),
 ('GASPROD', 'Gas production'),
 ('GASDEM', 'Gas demand'),
 ('GASOPROD', 'Gasoline production'),
 ('GASODEM', 'Gasoline demand')
     ], columns=['code', 'name'])
