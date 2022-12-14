/*
 * 데이터베이스 연결 전 설정
 */
const { Sequelize } = require('sequelize');
const { Corporation } = require('./corporation');
const { Investor } = require('./investor');
const { Marketprice } = require('./marketprice');

const env = process.env.NODE_ENV || 'development';
const config = require('../config/config')[env];

const db = {};
module.exports = db;
const sequelize = new Sequelize(config.database, config.username, config.password, config);

db.Corporation = Corporation;
db.Investor = Investor;
db.Marketprice = Marketprice;

//Corporation.init(sequelize);
Investor.init(sequelize);
Marketprice.init(sequelize);



sequelize.sync({force:false})
    .then(() => {
        console.log('데이터 베이스 연결 성공');
    })
    .catch((err) => {
        console.error(err);
    });

db.sequelize = sequelize;

// {
//     foreignKey: "stk_code", // change column name
//     onDelete: "RESTRICT", // ON DELETE config
//     onUpdate: "RESTRICT", // ON UPDATE config
//     constraints: false, // remove ON DELETE and ON UPDATE constraints
//   }