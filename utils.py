def equal_payment(p, rate, years):
    r = rate / 100 / 12
    n = years * 12

    m = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    total = m * n
    interest = total - p

    return m, interest, total


def equal_principal(p, rate, years):
    r = rate / 100 / 12
    n = years * 12

    mp = p / n
    interest = 0

    for i in range(n):
        interest += (p - i * mp) * r

    total = p + interest
    return mp + p * r, interest, total


# ===== 双曲线数据 =====
def dual_curve(p, rate, years):
    r = rate / 100 / 12
    n = years * 12

    # 等额本息
    m1 = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    # 等额本金
    mp = p / n

    b1 = p
    b2 = p

    c1 = []
    c2 = []

    for i in range(n):
        i1 = b1 * r
        p1 = m1 - i1
        b1 -= p1

        i2 = b2 * r
        p2 = mp
        b2 -= p2

        c1.append(max(b1, 0))
        c2.append(max(b2, 0))

    return c1[:120], c2[:120]


# ===== 多年对比 =====
def multi_year_compare(p, rate):
    years_list = [10, 20, 30]
    result = []

    for y in years_list:
        m, i, t = equal_payment(p, rate, y)

        result.append({
            "years": y,
            "month": round(m, 2),
            "interest": round(i, 2),
            "total": round(t, 2)
        })

    return result