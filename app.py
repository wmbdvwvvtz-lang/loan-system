from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    dual = None
    compare = None

    if request.method == "POST":

        p = float(request.form["principal"])
        rate = float(request.form["rate"])
        years = int(request.form.get("years", 30))

        # ===== 基础贷款 =====
        m, i, t = equal_payment(p, rate, years)

        result = {
            "month": round(m, 2),
            "interest": round(i, 2),
            "total": round(t, 2)
        }

        # ===== 双曲线 =====
        c1, c2 = dual_curve(p, rate, years)

        dual = {
            "labels": list(range(len(c1))),
            "equal_payment": c1,
            "equal_principal": c2
        }

        # ===== 多年对比 =====
        compare = multi_year_compare(p, rate)

    return render_template(
        "index.html",
        result=result,
        dual=dual,
        compare=compare
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)