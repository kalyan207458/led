from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# =========================================================
# TV DATABASE
# =========================================================

tvs = [
    # ---------------- LG ----------------
    {
        "id": 1,
        "brand": "LG",
        "model": "32LB653",
        "price": 19000,
        "leastprice": 17300,
        "resolution": "HD",
        "refresh_rate": "60 Hz",
        "processor": "α5 AI Processor 4K Gen6",
        "hdr": "HDR10 Pro",
        "sound": "20W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },
    {
        "id": 2,
        "brand": "LG",
        "model": "LG 55nu880bpl",
        "price": 54999,
        "leastprice": 47000,
        "size": "55 inch",
        "resolution": "4K Ultra HD",
        "display": "LED",
        "refresh_rate": "60 Hz",
        "processor": "α5 AI Processor 4K Gen6",
        "hdr": "HDR10 Pro",
        "sound": "20W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    # ---------------- Samsung ----------------
    {
        "id": 3,
        "brand": "Samsung",
        "model": "43U8400H",
        "price": 39500,
        "leastprice": 35400,
        "size": "43 inch",
        "resolution": "4K Ultra HD",
        "display": "Crystal UHD",
        "refresh_rate": "60 Hz",
        "processor": "Crystal Processor 4K",
        "hdr": "HDR10+",
        "sound": "20W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },
    {
        "id": 4,
        "brand": "Samsung",
        "model": "55U880H",
        "price": 53999,
        "leastprice": 47000,
        "size": "55 inch",
        "resolution": "4K Ultra HD",
        "display": "QLED",
        "refresh_rate": "60 Hz",
        "processor": "Quantum Processor Lite 4K",
        "hdr": "Quantum HDR",
        "sound": "20W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    # ---------------- Hisense ----------------
    {
        "id": 5,
        "brand": "Hisense",
        "model": "Hisense",
        "price": 29999,
        "leastprice": 17300,
        "size": "43 inch",
        "resolution": "4K Ultra HD",
        "display": "LED",
        "refresh_rate": "60 Hz",
        "processor": "Quad Core Processor",
        "hdr": "HDR10+",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },
    {
        "id": 6,
        "brand": "Hisense",
        "model": "Hisense 55A6S",
        "price": 41000,
        "leastprice": 136000,
        "size": "55 inch",
        "resolution": "4K Ultra HD",
        "display": "Mini LED",
        "refresh_rate": "144 Hz",
        "processor": "Hi-View Engine",
        "hdr": "Dolby Vision IQ",
        "sound": "40W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Years"
    },

    # ---------------- Sony ----------------
    {
        "id": 7,
        "brand": "Sony",
        "model": "Bravia 43S25M2",
        "price": 54999,
        "leastprice": 50000,
        "size": "43 inch",
        "resolution": "4K Ultra HD",
        "display": "LED",
        "refresh_rate": "60 Hz",
        "processor": "4K Processor X1",
        "hdr": "HDR10",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },
    {
        "id": 8,
        "brand": "Sony",
        "model": "55XR5",
        "price": 169999,
        "leastprice": 130000,
        "size": "55 inch",
        "resolution": "4K Ultra HD",
        "display": "LED",
        "refresh_rate": "60 Hz",
        "processor": "4K Processor X1",
        "hdr": "Dolby Vision",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    # ---------------- TCL ----------------
    {
        "id": 9,
        "brand": "TCL",
        "model": "TCL 43P6l",
        "price": 28999,
        "leastprice": 19300,
        "size": "43 inch",
        "resolution": "4K Ultra HD",
        "display": "LED",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ Engine",
        "hdr": "HDR10",
        "sound": "24W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },
    {
        "id": 10,
        "brand": "TCL",
        "model": "55P8L",
        "price": 44999,
        "leastprice": 35300,
        "size": "55 inch",
        "resolution": "4K Ultra HD",
        "display": "QLED",
        "refresh_rate": "120 Hz",
        "processor": "AiPQ Engine Gen 3",
        "hdr": "Dolby Vision",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    # ---------------- Haier ----------------
    {
        "id": 11,
        "brand": "Haier",
        "model": "Haier 43K800UX",
        "price": 31999,
        "leastprice": 17300,
        "size": "43 inch",
        "resolution": "4K Ultra HD",
        "display": "LED",
        "refresh_rate": "60 Hz",
        "processor": "Quad Core Processor",
        "hdr": "HDR10",
        "sound": "24W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },
    {
        "id": 12,
        "brand": "Haier",
        "model": "Haier 55S9QT",
        "price": 49999,
        "leastprice": 17300,
        "size": "55 inch",
        "resolution": "4K Ultra HD",
        "display": "QLED",
        "refresh_rate": "120 Hz",
        "processor": "Quad Core Processor",
        "hdr": "Dolby Vision",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Years"
    }
]


# HOME PAGE

@app.route("/")
def home():
    return render_template("index.html")


# BRANDS PAGE

@app.route("/brands")
def brands():
    brands_list = ["LG", "Samsung", "Hisense", "Sony", "TCL", "Haier"]

    return render_template(
        "brands.html",
        brands=brands_list
    )


# MODELS PAGE

@app.route("/models/<brand>")
def models(brand):

    selected_tvs = [
        tv for tv in tvs
        if tv["brand"].lower() == brand.lower()
    ]

    return render_template(
        "models.html",
        brand=brand,
        tvs=selected_tvs
    )



# TV DETAILS

@app.route("/tv/<int:tv_id>")
def tv_details(tv_id):

    tv = next(
        (tv for tv in tvs if tv["id"] == tv_id),
        None
    )

    if tv is None:
        return "TV not found", 404

    return render_template(
        "tv_details.html",
        tv=tv
    )


# COMPARE PAGE

@app.route("/compare", methods=["GET", "POST"])
def compare():

    selected_tvs = []

    if request.method == "POST":

        selected_ids = request.form.getlist("tv_ids")

        for tv_id in selected_ids:

            tv = next(
                (tv for tv in tvs if str(tv["id"]) == tv_id),
                None
            )

            if tv:
                selected_tvs.append(tv)

    return render_template(
        "compare.html",
        tvs=tvs,
        selected_tvs=selected_tvs
    )


# RUN APPLICATION

if __name__ == "__main__":
    app.run(debug=True)