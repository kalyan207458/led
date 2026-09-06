from flask import Flask, render_template, request

app = Flask(__name__)


# TV DATABASE

tvs = [

    # LG TVs

    {
        "id": 1,
        "brand": "LG",
        "model": "32LB653",
        "price": 20000,
        "leastprice": 17300,
        "resolution": "HD",
        "refresh_rate": "60 Hz",
        "processor": "α5 AI Processor",
        "hdr": "HDR10 / HLG",
        "sound": "10W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "2",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 2,
        "brand": "LG",
        "model": "32LB659",
        "price": 21100,
        "leastprice": 18000,
        "resolution": "HD",
        "refresh_rate": "60 Hz",
        "processor": "α5 AI Processor",
        "hdr": "HDR10 / HLG",
        "sound": "10W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "2",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 3,
        "brand": "LG",
        "model": "43NU880",
        "price": 37500,
        "leastprice": 32700,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "α7 AI Processor 4K",
        "hdr": "HDR10 / HLG",
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
        "id": 4,
        "brand": "LG",
        "model": "43QNED70",
        "price": 45000,
        "leastprice": 40400,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "α7 AI Processor 4K Gen9",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 5,
        "brand": "LG",
        "model": "50NU880B",
        "price": 45000,
        "leastprice": 40600,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "α7 AI Processor 4K Gen9",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 6,
        "brand": "LG",
        "model": "55NU880",
        "price": 48000,
        "leastprice": 43000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "α7 AI Processor 4K",
        "hdr": "HDR10 / HLG",
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
        "id": 7,
        "brand": "LG",
        "model": "55QNED70",
        "price": 57000,
        "leastprice": 51500,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "α7 AI Processor 4K Gen9",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 8,
        "brand": "LG",
        "model": "55QNED82B",
        "price": 65000,
        "leastprice": 57000,
        "resolution": "4K UHD",
        "refresh_rate": "120 Hz",
        "processor": "α8 AI Processor 4K",
        "hdr": "Dolby Vision / HDR10 / HLG",
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
        "id": 9,
        "brand": "LG",
        "model": "55QNED85B",
        "price": 72000,
        "leastprice": 66000,
        "resolution": "4K UHD",
        "refresh_rate": "120 Hz",
        "processor": "α8 AI Processor 4K Gen3",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 10,
        "brand": "LG",
        "model": "55C6",
        "price": 125000,
        "leastprice": 116000,
        "resolution": "4K UHD OLED",
        "refresh_rate": "120 Hz",
        "processor": "α11 AI Processor 4K Gen3",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "40W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "3",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 11,
        "brand": "LG",
        "model": "65NU880",
        "price": 71000,
        "leastprice": 63000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "α7 AI Processor 4K",
        "hdr": "HDR10 / HLG",
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
        "id": 12,
        "brand": "LG",
        "model": "65QNEDQ82B",
        "price": 91900,
        "leastprice": 84000,
        "resolution": "4K UHD",
        "refresh_rate": "120 Hz",
        "processor": "α8 AI Processor 4K",
        "hdr": "Dolby Vision / HDR10 / HLG",
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
        "id": 13,
        "brand": "LG",
        "model": "65QNED85B",
        "price": 110000,
        "leastprice": 94800,
        "resolution": "4K UHD",
        "refresh_rate": "120 Hz",
        "processor": "α8 AI Processor 4K Gen3",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 14,
        "brand": "LG",
        "model": "65C6",
        "price": 190000,
        "leastprice": 159800,
        "resolution": "4K UHD OLED",
        "refresh_rate": "120 Hz",
        "processor": "α11 AI Processor 4K Gen3",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "40W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "3",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 15,
        "brand": "LG",
        "model": "75NU880",
        "price": 96000,
        "leastprice": 86000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "α7 AI Processor 4K",
        "hdr": "HDR10 / HLG",
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
        "id": 16,
        "brand": "LG",
        "model": "75QNED85",
        "price": 150000,
        "leastprice": 129900,
        "resolution": "4K UHD",
        "refresh_rate": "120 Hz",
        "processor": "α8 AI Processor 4K",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 17,
        "brand": "LG",
        "model": "75C6",
        "price": 350000,
        "leastprice": 330000,
        "resolution": "4K UHD OLED",
        "refresh_rate": "120 Hz",
        "processor": "α11 AI Processor 4K Gen3",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "40W",
        "smart_tv": "webOS",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "3",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },


    # SAMSUNG TVs

    {
        "id": 18,
        "brand": "Samsung",
        "model": "32H4610",
        "price": 19500,
        "leastprice": 17100,
        "resolution": "HD",
        "refresh_rate": "60 Hz",
        "processor": "Crystal Processor",
        "hdr": "HDR",
        "sound": "20W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "2",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 19,
        "brand": "Samsung",
        "model": "43U8400H",
        "price": 41000,
        "leastprice": 35400,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "Crystal Processor 4K",
        "hdr": "HDR",
        "sound": "30W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 20,
        "brand": "Samsung",
        "model": "43M71H",
        "price": 45000,
        "leastprice": 40600,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR",
        "sound": "30W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 21,
        "brand": "Samsung",
        "model": "50U8300H",
        "price": 47000,
        "leastprice": 40700,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "Crystal Processor 4K",
        "hdr": "HDR",
        "sound": "20W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 22,
        "brand": "Samsung",
        "model": "55U8300H",
        "price": 57000,
        "leastprice": 47000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "Crystal Processor 4K",
        "hdr": "HDR",
        "sound": "20W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 23,
        "brand": "Samsung",
        "model": "55M70H",
        "price": 61000,
        "leastprice": 54200,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR",
        "sound": "30W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 24,
        "brand": "Samsung",
        "model": "55M80H",
        "price": 70000,
        "leastprice": 60400,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR",
        "sound": "40W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 25,
        "brand": "Samsung",
        "model": "55QN70H",
        "price": 81000,
        "leastprice": 71600,
        "resolution": "4K QLED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR",
        "sound": "40W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 26,
        "brand": "Samsung",
        "model": "55QN80H",
        "price": 91000,
        "leastprice": 82700,
        "resolution": "4K Neo QLED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR+",
        "sound": "40W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 27,
        "brand": "Samsung",
        "model": "65U880H",
        "price": 72900,
        "leastprice": 66800,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "Crystal Processor 4K",
        "hdr": "HDR",
        "sound": "20W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 28,
        "brand": "Samsung",
        "model": "65M70H",
        "price": 90000,
        "leastprice": 77700,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR",
        "sound": "30W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 29,
        "brand": "Samsung",
        "model": "65M80H",
        "price": 110000,
        "leastprice": 90000,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR",
        "sound": "40W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 30,
        "brand": "Samsung",
        "model": "65QN70H",
        "price": 125000,
        "leastprice": 103000,
        "resolution": "4K QLED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR",
        "sound": "40W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 31,
        "brand": "Samsung",
        "model": "65QN80H",
        "price": 145000,
        "leastprice": 117000,
        "resolution": "4K Neo QLED",
        "refresh_rate": "120 Hz",
        "processor": "NQ4 AI Gen2",
        "hdr": "Neo Quantum HDR+",
        "sound": "40W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 32,
        "brand": "Samsung",
        "model": "75U8300H",
        "price": 102900,
        "leastprice": 90300,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "Crystal Processor 4K",
        "hdr": "HDR",
        "sound": "20W",
        "smart_tv": "Tizen",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },


    # SONY TVs

    {
        "id": 33,
        "brand": "Sony",
        "model": "43S22M2",
        "price": 60000,
        "leastprice": 48000,
        "resolution": "4K UHD",
        "refresh_rate": "50 Hz",
        "processor": "4K Processor X1",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 34,
        "brand": "Sony",
        "model": "43S25M2",
        "price": 71900,
        "leastprice": 50000,
        "resolution": "4K UHD",
        "refresh_rate": "50 Hz",
        "processor": "4K Processor X1",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 35,
        "brand": "Sony",
        "model": "55S25M2",
        "price": 69900,
        "leastprice": 59200,
        "resolution": "4K UHD",
        "refresh_rate": "50 Hz",
        "processor": "4K Processor X1",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 36,
        "brand": "Sony",
        "model": "55XR35M2",
        "price": 86900,
        "leastprice": 76000,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "Cognitive Processor XR",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 37,
        "brand": "Sony",
        "model": "55XR55",
        "price": 125000,
        "leastprice": 117000,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "Cognitive Processor XR",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 38,
        "brand": "Sony",
        "model": "65S25M2",
        "price": 89900,
        "leastprice": 76800,
        "resolution": "4K UHD",
        "refresh_rate": "50 Hz",
        "processor": "4K Processor X1",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 39,
        "brand": "Sony",
        "model": "65XR35M2",
        "price": 120000,
        "leastprice": 102700,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "Cognitive Processor XR",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 40,
        "brand": "Sony",
        "model": "75S30",
        "price": 130000,
        "leastprice": 118000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "4K HDR Processor X1",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 41,
        "brand": "Sony",
        "model": "75XR35M2",
        "price": 159000,
        "leastprice": 138200,
        "resolution": "4K UHD Mini LED",
        "refresh_rate": "120 Hz",
        "processor": "Cognitive Processor XR",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },


    # TCL TVs

    {
        "id": 42,
        "brand": "TCL",
        "model": "32S4K",
        "price": 17500,
        "leastprice": 15200,
        "resolution": "HD",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "HDR10",
        "sound": "16W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "2",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 43,
        "brand": "TCL",
        "model": "43P6L",
        "price": 36700,
        "leastprice": 31600,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 44,
        "brand": "TCL",
        "model": "43P7L",
        "price": 40000,
        "leastprice": 35300,
        "resolution": "4K QLED",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 45,
        "brand": "TCL",
        "model": "43T69D",
        "price": 35200,
        "leastprice": 31600,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "HDR10",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 46,
        "brand": "TCL",
        "model": "43Q6S",
        "price": 35000,
        "leastprice": 30400,
        "resolution": "4K QLED",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 47,
        "brand": "TCL",
        "model": "55P6L",
        "price": 42700,
        "leastprice": 37600,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 48,
        "brand": "TCL",
        "model": "55P7L",
        "price": 50000,
        "leastprice": 45400,
        "resolution": "4K QLED",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 49,
        "brand": "TCL",
        "model": "55P8L",
        "price": 55000,
        "leastprice": 50800,
        "resolution": "4K QLED",
        "refresh_rate": "120 Hz",
        "processor": "AiPQ",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 50,
        "brand": "TCL",
        "model": "55T69D",
        "price": 45000,
        "leastprice": 40000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "HDR10",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 51,
        "brand": "TCL",
        "model": "65P7L",
        "price": 65000,
        "leastprice": 58600,
        "resolution": "4K QLED",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 52,
        "brand": "TCL",
        "model": "65T69D",
        "price": 60000,
        "leastprice": 54000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "HDR10",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 53,
        "brand": "TCL",
        "model": "75P7L",
        "price": 81000,
        "leastprice": 74300,
        "resolution": "4K QLED",
        "refresh_rate": "60 Hz",
        "processor": "AiPQ",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },

    {
        "id": 54,
        "brand": "TCL",
        "model": "75P8L",
        "price": 90000,
        "leastprice": 81200,
        "resolution": "4K QLED",
        "refresh_rate": "120 Hz",
        "processor": "AiPQ",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "1 Year"
    },


    # HAIER TVs

    {
        "id": 55,
        "brand": "Haier",
        "model": "32K82GX",
        "price": 19500,
        "leastprice": 17300,
        "resolution": "HD",
        "refresh_rate": "60 Hz",
        "processor": "Quad Core",
        "hdr": "HDR",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "2",
        "usb": "1",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 56,
        "brand": "Haier",
        "model": "43P7PRO",
        "price": 40000,
        "leastprice": 34000,
        "resolution": "4K UHD QLED",
        "refresh_rate": "120 Hz",
        "processor": "AI Processor",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "50W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 57,
        "brand": "Haier",
        "model": "50P7PRO",
        "price": 50000,
        "leastprice": 43200,
        "resolution": "4K UHD QLED",
        "refresh_rate": "120 Hz",
        "processor": "AI Processor",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "50W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 58,
        "brand": "Haier",
        "model": "50P7GTP",
        "price": 39000,
        "leastprice": 345000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "Quad Core",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "20W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 59,
        "brand": "Haier",
        "model": "55P7PRO",
        "price": 56000,
        "leastprice": 48800,
        "resolution": "4K UHD QLED",
        "refresh_rate": "120 Hz",
        "processor": "AI Processor",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "50W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },

    {
        "id": 60,
        "brand": "Haier",
        "model": "65P7GT",
        "price": 61000,
        "leastprice": 52000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "Quad Core",
        "hdr": "Dolby Vision / HDR10 / HLG",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 61,
        "brand": "Haier",
        "model": "65P7PRO",
        "price": 71000,
        "leastprice": 64000,
        "resolution": "4K UHD QLED",
        "refresh_rate": "120 Hz",
        "processor": "AI Processor",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "50W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "4",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "3 Year"
    },


    # HISENSE TVs

    {
        "id": 62,
        "brand": "Hisense",
        "model": "55A65",
        "price": 41900,
        "leastprice": 36000,
        "resolution": "4K UHD",
        "refresh_rate": "60 Hz",
        "processor": "Hi-View Engine",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "24W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 63,
        "brand": "Hisense",
        "model": "55Q6S",
        "price": 49000,
        "leastprice": 39700,
        "resolution": "4K QLED",
        "refresh_rate": "60 Hz",
        "processor": "Hi-View Engine",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 64,
        "brand": "Hisense",
        "model": "65Q65",
        "price": 63000,
        "leastprice": 53500,
        "resolution": "4K QLED",
        "refresh_rate": "60 Hz",
        "processor": "Hi-View Engine",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    },

    {
        "id": 65,
        "brand": "Hisense",
        "model": "75Q6S",
        "price": 86990,
        "leastprice": 74200,
        "resolution": "4K QLED",
        "refresh_rate": "60 Hz",
        "processor": "Hi-View Engine",
        "hdr": "Dolby Vision / HDR10+",
        "sound": "30W",
        "smart_tv": "Google TV",
        "dolby": "Yes",
        "hdmi": "3",
        "usb": "2",
        "wifi": "Yes",
        "bluetooth": "Yes",
        "warranty": "2 Year"
    }
]


# BRAND LIST

brands_list = [
    "LG",
    "Samsung",
    "Hisense",
    "Sony",
    "TCL",
    "Haier"
]


# HOME PAGE

@app.route("/")
def home():
    return render_template(
        "index.html",
        brands=brands_list,
        tvs=tvs
    )


# BRANDS PAGE

@app.route("/brands")
def brands():
    return render_template(
        "brands.html",
        brands=brands_list
    )


# MODELS BY BRAND

@app.route("/models/<brand>")
def models(brand):

    brand_tvs = [
        tv for tv in tvs
        if tv["brand"].lower() == brand.lower()
    ]

    return render_template(
        "models.html",
        brand=brand,
        tvs=brand_tvs
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
        "details.html",
        tv=tv
    )


# COMPARE TVs

@app.route("/compare", methods=["GET", "POST"])
def compare():

    selected_tvs = []

    if request.method == "POST":

        selected_ids = request.form.getlist("tv_ids")

        for tv_id in selected_ids:

            tv = next(
                (
                    tv for tv in tvs
                    if tv["id"] == int(tv_id)
                ),
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