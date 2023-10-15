name = "钱睿公司"
stock_price = 19.9
stock_code = "66666"
stock_price_daily_growth_factor = 1.2
growth_day = 7
after_growth = stock_price * stock_price_daily_growth_factor ** growth_day
print(f"公司名:{name},股票代码{stock_code},当前股价{stock_price}")
print("每日增长系数是:%.1f,经过%d天的增长后,股价达到%.2f"
      % (stock_price_daily_growth_factor, growth_day, after_growth))
