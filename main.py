# QuantLight - 轻量AI量化选股框架
# 纯本地运行，无网络请求，无数据爬虫，安全开源

import pandas as pd
import numpy as np

class QuantLight:
    def __init__(self):
        self.version = "1.0.0"
        print(f"✅ QuantLight {self.version} 加载完成")

    def factor_score(self, pe, pb, roe, growth):
        """
        多因子打分模型（简化版）
        """
        score = 0
        if 5 < pe < 30:
            score += 25
        if 1 < pb < 5:
            score += 25
        if roe > 10:
            score += 30
        if growth > 8:
            score += 20
        return round(score, 2)

    def screen_stocks(self):
        """
        A股模拟选股结果（本地模拟数据，非实时）
        """
        stock_list = [
            {"code": "600000", "name": "浦发银行", "pe": 6.2, "pb": 0.58, "roe": 11.2, "growth": 9.1},
            {"code": "601318", "name": "中国平安", "pe": 10.1, "pb": 1.22, "roe": 12.5, "growth": 8.7},
            {"code": "000858", "name": "五粮液", "pe": 22.3, "pb": 4.1, "roe": 18.6, "growth": 12.3},
            {"code": "002594", "name": "比亚迪", "pe": 28.7, "pb": 4.8, "roe": 14.2, "growth": 15.8},
            {"code": "600519", "name": "贵州茅台", "pe": 29.1, "pb": 7.2, "roe": 22.5, "growth": 11.4},
        ]

        df = pd.DataFrame(stock_list)
        df["score"] = df.apply(
            lambda row: self.factor_score(row.pe, row.pb, row.roe, row.growth),
            axis=1
        )
        df["suggest"] = df["score"].apply(lambda s: "买入关注" if s >= 70 else "观望")
        df = df.sort_values(by="score", ascending=False)
        return df

if __name__ == "__main__":
    ql = QuantLight()
    result = ql.screen_stocks()
    print("\n📊 选股结果：")
    print(result.to_string(index=False))
