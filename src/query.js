var concepts = ['区块链','横琴新区'];
var condition = {
    "type" : "小盘股",
    "$and" : []   
};
for(var i = 0; i < concepts.length; i++){
    var concept = {
        "$or" : []
    };
    for(var j = 0; j < 6; j++){
        cond = {}
        cond["concepts." + j] = concepts[i];
        concept['$or'].push(cond);
    }
    condition['$and'].push(concept);
}
db.getCollection('concepts').find(condition);