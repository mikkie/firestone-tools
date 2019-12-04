db.mocktrades.insertMany([{
    "code" : "600093",
    "state" : "未开始",
    "result" : "无",
    "userId" : ObjectId("5d905db9fc84d3224b0eb59c"),
    "strategyId" : ObjectId("5da19b7d181fc3600c5544c4"),
    "createDate" : new Date(),
    "deleted" : false,
    "params" : {
        "code" : "600093",
        "volume" : "100",
        "executeDate" : "2019-12-05",
        "monitorTime" : {
            "start" : "09:30",
            "end" : "15:00"
        },
        "index_percent" : {
            "low" : "-1.0",
            "high" : "3.0"
        },
        "percent" : {
            "low" : "-0.5",
            "high" : "2.5"
        },
        "speed" : {
            "time" : "2",
            "percent" : "2",
            "amount" : "300"
        }
    }
},{
    "code" : "002842",
    "state" : "未开始",
    "result" : "无",
    "userId" : ObjectId("5d905db9fc84d3224b0eb59c"),
    "strategyId" : ObjectId("5da19b7d181fc3600c5544c4"),
    "createDate" : new Date(),
    "deleted" : false,
    "params" : {
        "code" : "002842",
        "volume" : "100",
        "executeDate" : "2019-12-05",
        "monitorTime" : {
            "start" : "09:30",
            "end" : "15:00"
        },
        "index_percent" : {
            "low" : "-1.0",
            "high" : "3.0"
        },
        "percent" : {
            "low" : "-0.5",
            "high" : "2.5"
        },
        "speed" : {
            "time" : "2",
            "percent" : "2",
            "amount" : "300"
        }
    }
}])