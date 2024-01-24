const dbName = "ugc_db";
const conn = new Mongo();
const db = conn.getDB(dbName);
const collectionName = "content";

const collection = {
    name: "content",
    shardKey: "relation_uuid",
    indexFields: [
        "user_uuid",
        "object_type"
    ]
};

sh.enableSharding(dbName);
const shardKey = collection.shardKey;
const indexFields = collection.indexFields;

db.createCollection(collectionName);

sh.shardCollection(`${dbName}.${collectionName}`, { [shardKey]: "hashed" });

