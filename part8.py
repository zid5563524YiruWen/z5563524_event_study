from project2 import config
from project2.zid_project2_main import portfolio_main, get_avg, get_cumulative_ret

DM_Ret_dict, Vol_Ret_mrg_df, EW_LS_pf_df = portfolio_main(config.TICMAP, '2000-12-29', '2021-08-31',
                                                          'vol', ['Daily', ], 3)

avg_returns_year_2008 = get_avg(DM_Ret_dict["Daily"], year=2008)
q1_stock = avg_returns_year_2008.idxmin()
q2_average_return = avg_returns_year_2008.min()
print(f"Q1: Which stock in your sample has the lowest average daily return for the year 2008? Answer: {q1_stock}")

print(
    f"Q2: What is the daily average return of the stock in question 1 for the year 2008? Answer: {q2_average_return:.4f}")

q3_stock = get_avg(DM_Ret_dict["Monthly"], year=2019).idxmax()
q3_average_return = get_avg(DM_Ret_dict["Monthly"], year=2019).max()
print(f"Q3: Which stock in your sample has the highest average monthly return for the year 2019? Answer: {q3_stock}")

q4_average_return = get_avg(DM_Ret_dict["Monthly"], year=2019).max()
print(
    f"Q4: What is the average monthly return of the stock in question 3 for the year 2019? Answer: {q4_average_return:.4f}")

q5_average_volatility = get_avg(Vol_Ret_mrg_df[['tsla_vol']], year=2010)['tsla_vol']
print(
    f"Q5: What is the average monthly total volatility for stock 'TSLA' in the year 2010? Answer: {q5_average_volatility:.4f}")

vol_2008 = get_avg(Vol_Ret_mrg_df[['v_vol']], year=2008)
vol_2018 = get_avg(Vol_Ret_mrg_df[['v_vol']], year=2018)
q6_ratio = (vol_2018['v_vol'] / vol_2008['v_vol'])
print(
    f"Q6: What is the ratio of the average monthly total volatility for stock 'V' in the year 2008 to that in the year 2018? Answer: {q6_ratio:.1f}")

tsla_df_2010 = Vol_Ret_mrg_df[['tsla', 'tsla_vol']][Vol_Ret_mrg_df.index.year == 2010].dropna(how='any')
q7_effective_ym = len(tsla_df_2010)
print(f"Q7: How many effective year-month for stock 'TSLA' in year 2010? Answer: {q7_effective_ym}")

q8_rows, q8_cols = EW_LS_pf_df.shape
print(f"Q8: How many rows and columns in the EW_LS_pf_df data frame? Answer: {q8_rows},{q8_cols}")

q9_average_ew_return = EW_LS_pf_df.loc['2019']['ewp_rank_1'].mean()
print(
    f"Q9: What is the average equal weighted portfolio return of the quantile with the lowest total volatility for the year 2019? Answer: {q9_average_ew_return:.4f}")

q10_cumulative_return = get_cumulative_ret(EW_LS_pf_df['ls'])
print(
    f"Q10: What is the cumulative portfolio return of the total volatility long-short portfolio over the whole sample period? Answer: {q10_cumulative_return:.4f}")
