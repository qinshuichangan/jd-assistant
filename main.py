#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    asst = Assistant()      # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    asst.clear_cart()       # 清空购物车（可选）
    asst.add_item_to_cart(sku_ids='100011293950')  # 根据商品id添加购物车（可选）
    asst.submit_order_by_stock(sku_ids='100011293950', area='27_2376_50230_53680')  # 监控的商品id和地址id
    # 3个参数：
    # sku_ids: 商品id
    # area: 地区id
    # interval: 查询库存间隔，可选参数，默认为3秒/次
