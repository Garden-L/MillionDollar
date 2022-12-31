/*
 * 데이터베이스 연결 전 설정
 */
const { Investor }          = require('./Investor');
const { Sequelize }         = require('sequelize');
const { Corporation }       = require('./corporation');
const { Marketprice }       = require('./marketprice');
const StockOfIndex      = require('./stockOfIndex');
const IndexInfo = require('./IndexInfo');
const PrefixSumNetPurchase  = require('./PrefixSumNetPurchase');
const User = require('./user');

const env = process.env.NODE_ENV || 'development';
const config = require('../config/config')[env];

const db = {};
module.exports = db;

const sequelize = new Sequelize(config.database, config.username, config.password, config);

db.User = User
db.Investor = Investor;
db.Marketprice = Marketprice;
db.Corporation = Corporation;
db.StockOfIndex = StockOfIndex;
db.IndexInfo = IndexInfo;
db.PrefixSumNetPurchase = PrefixSumNetPurchase;

User.init(sequelize);
Investor.init(sequelize);
Marketprice.init(sequelize);
StockOfIndex.init(sequelize);
PrefixSumNetPurchase.init(sequelize);
IndexInfo.init(sequelize);


// sequelize.sync({force:false})
//     .then(() => {
//         console.log('데이터 베이스 연결 성공');
//     })
//     .catch((err) => {
//         console.error(err);
//     });

db.sequelize = sequelize;